/* ==========================================================================
   AMPLIFYME TRAINER — passerelle de données (même logique que ShockDesk)
   Un petit serveur Node sans dépendance qui :
     1. sert l'appli statique,
     2. va chercher les prix RÉELS côté serveur (Yahoo Finance), donc sans CORS,
     3. les met en cache 8 s pour ne pas se faire bloquer,
     4. expose /api/quotes et /api/bars pour le replay.

   Lancer :   node server.js            → http://localhost:8787
              PORT=9000 node server.js
              MOCK=1 node server.js   → prix de test (aucun accès internet requis)

   Si Yahoo est injoignable, l'appli retombe proprement sur le moteur simulé.
   ========================================================================== */
'use strict';

const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');

const PORT = Number(process.env.PORT || 8787);
const MOCK = process.env.MOCK === '1';
const TTL = 8000;
const ROOT = __dirname;

// Les 5 lignes du jeu → leurs symboles réels.
const TICKERS = {
  BABA: { yahoo: 'BABA', name: 'Alibaba ADR', currency: 'USD' },
  MSFT: { yahoo: 'MSFT', name: 'Microsoft', currency: 'USD' },
  VW: { yahoo: 'VOW3.DE', name: 'Volkswagen', currency: 'EUR' },
  HSBC: { yahoo: 'HSBA.L', name: 'HSBC Holdings', currency: 'GBp' },
  BP: { yahoo: 'BP.L', name: 'BP plc', currency: 'GBp' }
};

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.ico': 'image/x-icon'
};

const cache = new Map();

function json(res, code, obj) {
  const body = JSON.stringify(obj);
  res.writeHead(code, {
    'content-type': 'application/json; charset=utf-8',
    'cache-control': 'no-store',
    'access-control-allow-origin': '*',
    'content-length': Buffer.byteLength(body)
  });
  res.end(body);
}

function get(url) {
  return new Promise((resolve, reject) => {
    const req = https.get(url, {
      timeout: 6000,
      headers: {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36',
        accept: 'application/json,text/plain,*/*'
      }
    }, r => {
      let d = '';
      r.setEncoding('utf8');
      r.on('data', c => { d += c; });
      r.on('end', () => resolve({ status: r.statusCode, body: d }));
    });
    req.on('timeout', () => req.destroy(new Error('timeout')));
    req.on('error', reject);
  });
}

function mockQuote(ticker) {
  const base = { BABA: 168.4, MSFT: 512.7, VW: 92.6, HSBC: 9.82, BP: 4.61 }[ticker];
  const jitter = 1 + (Math.random() - 0.5) * 0.004;
  return {
    symbol: ticker, yahoo: TICKERS[ticker].yahoo, name: TICKERS[ticker].name,
    price: Math.round(base * jitter * 100) / 100,
    prevClose: base, currency: TICKERS[ticker].currency,
    ts: Date.now(), mock: true
  };
}

async function yahooChart(yahooSymbol, range, interval) {
  const url = 'https://query1.finance.yahoo.com/v8/finance/chart/' + encodeURIComponent(yahooSymbol) +
    '?range=' + (range || '1d') + '&interval=' + (interval || '1m') + '&includePrePost=false&events=div%2Csplit';
  const key = url;
  const hit = cache.get(key);
  if (hit && Date.now() - hit.at < TTL) return hit.data;

  const r = await get(url);
  if (r.status !== 200) throw new Error('yahoo ' + r.status);
  const body = JSON.parse(r.body);
  const result = body && body.chart && body.chart.result && body.chart.result[0];
  if (!result) throw new Error('yahoo: pas de résultat');
  cache.set(key, { at: Date.now(), data: result });
  return result;
}

function quoteFromResult(ticker, result) {
  const meta = result.meta || {};
  const q = (result.indicators && result.indicators.quote && result.indicators.quote[0]) || {};
  let last = meta.regularMarketPrice;
  if (!last && q.close && q.close.length) {
    for (let i = q.close.length - 1; i >= 0; i--) if (q.close[i]) { last = q.close[i]; break; }
  }
  return {
    symbol: ticker,
    yahoo: meta.symbol || TICKERS[ticker].yahoo,
    name: TICKERS[ticker].name,
    price: last,
    prevClose: meta.chartPreviousClose || meta.previousClose || null,
    currency: meta.currency || TICKERS[ticker].currency,
    marketState: meta.marketState || null,
    exchange: meta.exchangeName || null,
    ts: (meta.regularMarketTime ? meta.regularMarketTime * 1000 : Date.now())
  };
}

async function handleQuotes(url, res) {
  const wanted = (url.searchParams.get('symbols') || Object.keys(TICKERS).join(','))
    .split(',').map(s => s.trim().toUpperCase()).filter(t => TICKERS[t]);
  const items = [];
  for (const t of wanted) {
    try {
      if (MOCK) { items.push(mockQuote(t)); continue; }
      const result = await yahooChart(TICKERS[t].yahoo, '1d', '1m');
      items.push(quoteFromResult(t, result));
    } catch (e) {
      items.push({ symbol: t, error: String(e.message || e) });
    }
  }
  const ok = items.some(i => !i.error && i.price);
  json(res, ok ? 200 : 502, {
    source: MOCK ? 'mock' : 'yahoo',
    at: Date.now(),
    ok: ok,
    items: items
  });
}

async function handleBars(url, res) {
  const t = (url.searchParams.get('symbol') || '').toUpperCase();
  if (!TICKERS[t]) return json(res, 400, { error: 'symbole inconnu' });
  const range = url.searchParams.get('range') || '1d';
  const interval = url.searchParams.get('interval') || '1m';
  if (MOCK) {
    const bars = [];
    let px = mockQuote(t).price;
    const now = Date.now();
    for (let i = 240; i >= 0; i--) {
      px = px * (1 + (Math.random() - 0.5) * 0.0016);
      bars.push({ t: now - i * 60000, c: Math.round(px * 100) / 100 });
    }
    return json(res, 200, { source: 'mock', symbol: t, bars: bars });
  }
  try {
    const result = await yahooChart(TICKERS[t].yahoo, range, interval);
    const ts = result.timestamp || [];
    const close = (result.indicators.quote[0] || {}).close || [];
    const bars = [];
    for (let i = 0; i < ts.length; i++) if (close[i]) bars.push({ t: ts[i] * 1000, c: close[i] });
    json(res, 200, { source: 'yahoo', symbol: t, bars: bars });
  } catch (e) {
    json(res, 502, { error: String(e.message || e) });
  }
}

// Replay : un seul appel qui renvoie les séries alignées prêtes pour le moteur.
async function handleReplay(url, res) {
  const roundSec = Number(url.searchParams.get('roundSec') || 180);
  const need = Math.round(roundSec * 1000 / 620) + 4;
  const series = {}, anchors = {}, errors = {};
  for (const t of Object.keys(TICKERS)) {
    try {
      if (MOCK) {
        let px = mockQuote(t).price;
        const arr = [];
        for (let i = 0; i < need; i++) { px *= 1 + (Math.random() - 0.5) * 0.0018; arr.push(Math.round(px * 100) / 100); }
        series[t] = arr; anchors[t] = { price: arr[0], prevClose: arr[0], currency: TICKERS[t].currency };
        continue;
      }
      let result;
      try { result = await yahooChart(TICKERS[t].yahoo, '1d', '1m'); }
      catch (e) { result = await yahooChart(TICKERS[t].yahoo, '5d', '5m'); }
      const q = (result.indicators && result.indicators.quote && result.indicators.quote[0]) || {};
      const closes = (q.close || []).filter(c => c && c > 0);
      if (closes.length < 30) throw new Error('pas assez de barres');
      let use = closes.slice(-need);
      if (use.length < need) use = use.concat(use.slice(-(need - use.length)));  // complète par le passé
      series[t] = use;
      anchors[t] = { price: use[0], prevClose: use[0], currency: (result.meta && result.meta.currency) || TICKERS[t].currency };
    } catch (e) {
      errors[t] = String(e.message || e);
    }
  }
  const ok = Object.keys(series).length > 0;
  json(res, ok ? 200 : 502, { ok, source: MOCK ? 'mock' : 'yahoo', at: Date.now(), need, series, anchors, errors });
}

function serveStatic(url, res) {
  let rel = decodeURIComponent(url.pathname);
  if (rel === '/' || rel === '') rel = '/index.html';
  const file = path.join(ROOT, path.normalize(rel).replace(/^(\.\.[/\\])+/, ''));
  if (!file.startsWith(ROOT)) { res.writeHead(403); return res.end('forbidden'); }
  fs.readFile(file, (err, data) => {
    if (err) {
      res.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' });
      return res.end('404');
    }
    res.writeHead(200, {
      'content-type': MIME[path.extname(file)] || 'application/octet-stream',
      'cache-control': 'no-cache'
    });
    res.end(data);
  });
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, 'http://localhost');
  if (req.method === 'OPTIONS') {
    res.writeHead(204, { 'access-control-allow-origin': '*', 'access-control-allow-headers': '*' });
    return res.end();
  }
  if (url.pathname === '/api/health') {
    return json(res, 200, { ok: true, mock: MOCK, at: Date.now(), tickers: Object.keys(TICKERS) });
  }
  if (url.pathname === '/api/quotes') return handleQuotes(url, res).catch(e => json(res, 500, { error: String(e) }));
  if (url.pathname === '/api/bars') return handleBars(url, res).catch(e => json(res, 500, { error: String(e) }));
  if (url.pathname === '/api/replay') return handleReplay(url, res).catch(e => json(res, 500, { error: String(e) }));
  serveStatic(url, res);
});

server.listen(PORT, '0.0.0.0', () => {
  console.log('AmplifyME trainer — données ' + (MOCK ? 'MOCK' : 'Yahoo Finance'));
  console.log('→ http://localhost:' + PORT);
});
