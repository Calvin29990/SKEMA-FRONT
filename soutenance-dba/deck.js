/* Soutenance DBA — navigation de diaporama.
   Zéro dépendance. Amélioration progressive : sans JS, les diapositives
   restent empilées et lisibles (impression, lecteurs d'écran, vieux postes). */
(function () {
  "use strict";

  var slides = Array.prototype.slice.call(document.querySelectorAll(".slide"));
  if (!slides.length) return;

  var body = document.body;
  var stage = document.getElementById("stage");
  var counter = document.querySelector("[data-counter]");
  var progress = document.querySelector("[data-progress]");
  var index = 0;
  var KEY = "spm-soutenance-slide";

  /* ---------- mise à l'échelle 16:9 ---------- */
  function fit() {
    if (!body.classList.contains("is-deck")) return;
    var vw = window.innerWidth;
    var vh = window.innerHeight;
    var k = Math.min((vw - 24) / 1280, (vh - 96) / 720);
    k = Math.max(k, 0.28);
    slides.forEach(function (s) { s.style.transform = "scale(" + k + ")"; });
    if (stage) stage.style.height = vh + "px";
  }
  window.addEventListener("resize", fit);
  window.addEventListener("orientationchange", fit);


  /* ---------- garde-fou anti-débordement ----------
     Les diapositives sont à taille fixe. Si un texte dépasse (police
     différente selon la machine), on réduit légèrement la taille de base
     de la diapositive, par pas de 0,25 px, jusqu'à ce que tout tienne.
     Rien n'est jamais rogné : au pire, le texte devient plus petit. */
  function bodyOverflows(slide) {
    var body = slide.querySelector(".body");
    if (!body) return false;
    var top = body.offsetTop;
    var bottom = top + body.offsetHeight;
    var kids = body.querySelectorAll("*");
    for (var i = 0; i < kids.length; i++) {
      var el = kids[i];
      if (!el.offsetHeight) continue;
      var y = el.offsetTop;
      var h = el.offsetHeight;
      if (y + h > bottom + 1 || y < top - 1) return true;
    }
    return slide.scrollHeight > slide.clientHeight + 1;
  }

  function fitText(slide) {
    var root = 16;
    slide.classList.remove("is-overflow");
    slide.style.fontSize = root + "px";
    var guard = 0;
    while (bodyOverflows(slide) && root > 12.5 && guard < 30) {
      root -= 0.25;
      guard++;
      slide.style.fontSize = root + "px";
    }
    /* dernier recours (police très large ou visuel imposant) : défilement
       interne plutôt qu'un texte rogné — rien n'est perdu. */
    if (bodyOverflows(slide)) slide.classList.add("is-overflow");
  }

  function autofitAll() {
    slides.forEach(function (s) {
      s.classList.add("is-measuring");
      fitText(s);
      s.classList.remove("is-measuring");
    });
  }

  /* ---------- navigation ---------- */
  function show(i, push) {
    index = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach(function (s, n) {
      s.classList.toggle("is-active", n === index);
      s.setAttribute("aria-hidden", n === index ? "false" : "true");
    });
    if (counter) counter.textContent = (index + 1) + " / " + slides.length;
    if (progress) progress.style.width = ((index + 1) / slides.length) * 100 + "%";
    if (push !== false) {
      try {
        var h = "#" + (index + 1);
        if (window.location.hash !== h) history.replaceState(null, "", h);
        localStorage.setItem(KEY, String(index));
      } catch (e) { /* mode fichier local : on ignore */ }
    }
    var active = slides[index];
    if (active) active.scrollTop = 0;
    fit();
  }
  function next() { show(index + 1); }
  function prev() { show(index - 1); }

  document.querySelectorAll("[data-next]").forEach(function (b) { b.addEventListener("click", next); });
  document.querySelectorAll("[data-prev]").forEach(function (b) { b.addEventListener("click", prev); });

  /* ---------- sommaire ---------- */
  var toc = document.getElementById("toc");
  var tocList = document.querySelector("[data-toc-list]");
  if (tocList) {
    slides.forEach(function (s, n) {
      var b = document.createElement("button");
      b.type = "button";
      b.innerHTML = "<i>" + (n + 1) + "</i><span>" + (s.getAttribute("data-title") || "Diapositive " + (n + 1)) + "</span>";
      b.addEventListener("click", function () { closeOverlays(); show(n); });
      tocList.appendChild(b);
    });
  }
  function openOverlay(el) {
    if (!el) return;
    el.classList.add("open");
    var first = el.querySelector("button");
    if (first) first.focus();
  }
  function closeOverlays() {
    document.querySelectorAll(".overlay.open").forEach(function (o) { o.classList.remove("open"); });
  }

  /* ---------- notes ---------- */
  var notesBtn = document.querySelector("[data-notes-toggle]");
  function toggleNotes() {
    var on = body.classList.toggle("show-notes");
    if (notesBtn) notesBtn.setAttribute("aria-pressed", on ? "true" : "false");
  }
  if (notesBtn) notesBtn.addEventListener("click", toggleNotes);

  /* ---------- divers ---------- */
  var tocBtn = document.querySelector("[data-toc-toggle]");
  var help = document.getElementById("help");
  var helpBtn = document.querySelector("[data-help-toggle]");
  var printBtn = document.querySelector("[data-print]");
  if (tocBtn) tocBtn.addEventListener("click", function () { openOverlay(toc); });
  if (helpBtn) helpBtn.addEventListener("click", function () { openOverlay(help); });
  if (printBtn) printBtn.addEventListener("click", function () { window.print(); });

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      (document.documentElement.requestFullscreen || function () {}).call(document.documentElement);
    } else if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }

  /* ---------- clavier ---------- */
  document.addEventListener("keydown", function (e) {
    var open = document.querySelector(".overlay.open");
    if (e.key === "Escape") { closeOverlays(); return; }
    if (open) return;
    switch (e.key) {
      case "ArrowRight": case "PageDown": case " ": case "Enter":
        e.preventDefault(); next(); break;
      case "ArrowLeft": case "PageUp":
        e.preventDefault(); prev(); break;
      case "Home": e.preventDefault(); show(0); break;
      case "End": e.preventDefault(); show(slides.length - 1); break;
      case "s": case "S": openOverlay(toc); break;
      case "n": case "N": toggleNotes(); break;
      case "f": case "F": toggleFullscreen(); break;
      case "p": case "P": window.print(); break;
      default: break;
    }
  });

  /* ---------- tactile ---------- */
  var x0 = null, y0 = null;
  stage && stage.addEventListener("touchstart", function (e) {
    if (e.touches.length !== 1) return;
    x0 = e.touches[0].clientX; y0 = e.touches[0].clientY;
  }, { passive: true });
  stage && stage.addEventListener("touchend", function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    var dy = e.changedTouches[0].clientY - y0;
    if (Math.abs(dx) > 55 && Math.abs(dx) > Math.abs(dy)) { dx < 0 ? next() : prev(); }
    x0 = y0 = null;
  }, { passive: true });

  /* ---------- démarrage ---------- */
  function start() {
    body.classList.add("is-deck");
    try { autofitAll(); } catch (e) { /* mesure impossible : on garde la taille de base */ }
    var fromHash = parseInt((window.location.hash || "").replace("#", ""), 10);
    var saved = parseInt(localStorage.getItem(KEY) || "1", 10);
    var i = !isNaN(fromHash) && fromHash >= 1 ? fromHash - 1 : (!isNaN(saved) ? saved : 0);
    show(i, false);
    window.addEventListener("hashchange", function () {
      var n = parseInt((window.location.hash || "").replace("#", ""), 10);
      if (!isNaN(n) && n - 1 !== index) show(n - 1, false);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
