# Morgan Stanley Sales & Trading Assessment — Candidate Quick Reference

> **Independent preparation notes — not an official Morgan Stanley or Aon document.** This is a compact refresher on general numerical reasoning, inductive reasoning and workplace judgement. It is not an answer key and does not reproduce proprietary questions. Follow the assessment invitation and on-screen instructions for the actual test.

## What is known — and what is not

The candidate invitation identifies **Numerical Reasoning, Inductive Reasoning and Situational Judgement**. Public Aon material describes general practice formats, but it does **not** establish the exact modules, question count, timing, language options or item style selected by Morgan Stanley for this application. In particular, do not assume that a generic Aon format or a SKEMA/Nomura assessment is identical to the Morgan Stanley assessment. Use the live invitation as the source of truth.

If the assessment rules prohibit external help, close this guide before starting. Complete the live assessment independently; use only tools explicitly permitted by the instructions.

---

## 1. Numerical reasoning

### A reliable process for each item

1. **Read the exact question first.** Identify the requested metric, entity and time period.
2. **Find the relevant cells only.** Check the table title, row/column labels, units, currency and whether values are actual, forecast, indexed or cumulative.
3. **Write the relationship before calculating.** For example, percentage change uses the old value as its denominator.
4. **Keep units and periods aligned.** Do not compare annual with quarterly values, or totals with per-unit figures.
5. **Estimate the answer.** A quick magnitude check catches misplaced decimals and reversed denominators.
6. **Answer only what the data supports.** Do not add assumptions that are not stated.

### Percentages and percentage points

- **A is what percentage of B?** `A / B × 100%`
- **p% of X:** `X × p / 100`
- **Percentage change from old to new:** `(new − old) / old × 100%`
- **Value after an increase of p%:** `old × (1 + p)` where `p` is written as a decimal.
- **Value after a decrease of p%:** `old × (1 − p)`.
- **Recover the starting value after an increase:** `final / (1 + p)`.
- **Recover the starting value after a decrease:** `final / (1 − p)`.
- **Sequential changes compound:** `final = initial × (1 + p₁) × (1 + p₂)`. Do not simply add the percentages unless the question explicitly defines a common base.
- **Percentage-point change:** `new rate − old rate`. A move from 12% to 15% is **+3 percentage points**, and a **25% relative increase** in the rate.
- **Basis points:** `1 bp = 0.01 percentage point = 0.0001` as a decimal; `100 bps = 1 percentage point`.

**Example:** Revenue rises from 80 to 100. The change is 20; percentage growth is `20 / 80 = 25%`, not 20%.

### Fractions, ratios and proportions

- Convert a fraction to a percentage with `numerator / denominator × 100%`.
- Compare positive fractions `a/b` and `c/d` by cross-multiplying: compare `a × d` with `c × b` (denominators must be positive).
- For a ratio `a:b`, total parts are `a+b`; the first share of total `T` is `T × a/(a+b)`.
- If `A:B = 2:3` and `A = 40`, one ratio unit is `40/2 = 20`, so `B = 3 × 20 = 60`.
- “A is twice B” means `A = 2B`; “A is 200% of B” also means `2B`. “A increased **by** 200%” means the final value is `3B`.
- If quantities are proportional, calculate the value per unit before scaling.

### Weighted averages, margins and market shares

- **Weighted average:** `Σ(weight × value) / Σ(weights)`. If weights are already percentages summing to 100%, divide by 100 as appropriate.
- **Profit margin:** `profit / revenue × 100%`.
- **Market share:** `company sales / total market sales × 100%`.
- **Average price:** `total spend / total units`, not the simple average of prices when quantities differ.
- **Contribution to total growth:** calculate each component’s change, then compare it with the stated total; do not confuse a component’s growth rate with its contribution to aggregate growth.

### Growth over several periods

- **Compound annual growth rate (CAGR):** `((ending value / beginning value)^(1/n) − 1) × 100%`, where `n` is the number of periods.
- If a value grows at a constant rate `r` for `n` periods: `ending = beginning × (1+r)^n`.
- For a simple average growth rate, use the arithmetic average only when the question asks for it. CAGR is usually the relevant compounded rate between two endpoints.

### Present value and discounting

Use these only if the question calls for discounting. Match the discount rate to the cash-flow period (annual rate with annual periods, quarterly rate with quarterly periods).

- **Present value of one future amount:** `PV = FV / (1+r)^n`.
- **Future value:** `FV = PV × (1+r)^n`.
- **Present value of multiple cash flows:** `PV = Σ[CFₜ / (1+r)^t]`.
- **Net present value:** `NPV = −initial investment + Σ[CFₜ / (1+r)^t]`.
- **Ordinary annuity, payments at each period-end:** `PV = C × [1 − (1+r)^(−n)] / r`.
- **Level perpetuity:** `PV = C/r`.
- **Growing perpetuity:** `PV = C₁/(r−g)`, only when `r > g` and the first payment is one period from now.

Here `r` is the rate **per period**, `n` is the number of periods, `C` is the regular payment and `CFₜ` is cash flow at time `t`. If a test does not provide or require a discount rate, do not invent one.

### Reading tables and interpreting claims

- Check whether figures are in units, thousands, millions, percentages, basis points or index values.
- Distinguish **level** (“revenue was 120”) from **change** (“revenue rose by 20”) and from **growth rate** (“revenue grew 20%”).
- An index of 100 is a base, not necessarily a currency amount.
- Check whether a figure is annual, quarterly, year-to-date, trailing-twelve-month or cumulative.
- “Average” may mean a simple or weighted average; use the definition supplied.
- “At least” includes the boundary; “more than” does not. “Up to” usually includes a maximum, subject to the wording.

Some public Aon numerical practice material uses **True / False / Cannot Say** statements based on data:

- **True:** the statement follows from the provided information.
- **False:** the information contradicts it.
- **Cannot Say:** the information is insufficient to decide either way.

This is a **general Aon practice format**, not confirmation that Morgan Stanley uses these exact response options. In any test, use the choices actually shown and do not bring in outside knowledge.

---

## 2. Inductive reasoning

Treat each shape or symbol as data. Scan systematically rather than guessing from the overall appearance.

### A useful scan order

Check one property at a time:

1. **Count:** number of objects, marks, sides, dots or elements.
2. **Type:** shape, symbol or category.
3. **Position:** location, order, inside/outside, left/right, top/bottom.
4. **Orientation:** rotation, direction, reflection or sequence.
5. **Appearance:** fill, shading, colour, size, line style or border.
6. **Relationship:** overlap, containment, alternation, addition/subtraction or movement.

Then compare rows, columns or adjacent items. State the rule in plain words and verify it against every relevant item. If the question asks for an odd one out, look for a property shared by the majority and identify the one that violates it. Prefer a simple rule that explains all items over a complicated rule that fits only some.

Aon’s public **Scales ix** practice material shows a generic task with nine objects and one that does not follow the rule. This is useful for general practice, but does not prove that Morgan Stanley uses Scales ix or the same layout, timing or number of questions.

### Avoid common traps

- Do not lock onto colour or rotation before checking count and position.
- Do not infer a pattern from only two items if the full sequence can disprove it.
- Watch for two alternating sequences (odd positions and even positions may follow different rules).
- Verify whether a change is clockwise or counter-clockwise and whether it advances by a fixed or changing step.
- If stuck, test a different property rather than repeatedly re-reading the same guess.

---

## 3. Situational judgement

There is no public answer key for Morgan Stanley’s specific scenarios. Use sound professional judgement rather than trying to game a presumed scoring formula. A useful priority order is:

1. **Law, regulation, firm policy and market integrity.** These are boundaries, not trade-offs against convenience or revenue.
2. **Client interests, suitability and confidentiality.** Help the client within those boundaries; do not mislead, overpromise or disclose another client’s information.
3. **Prevent or reduce immediate harm.** Identify urgency, impact and who has authority to act.
4. **Communicate accurately and respectfully.** Clarify facts, state what is known, and avoid blame or speculation.
5. **Take ownership and involve the right people.** Act within your authority; escalate material compliance, conduct, client or market risks promptly to the appropriate manager or control function.
6. **Follow through.** Keep an appropriate record and make sure the issue reaches resolution, following firm procedure.

### Practical principles

- **Compliance before convenience:** never bypass controls to meet a deadline or satisfy a client request. Explain the constraint and offer a compliant alternative where possible.
- **Client first, responsibly:** understand the client’s need, give clear and timely service, and protect the client’s legitimate interests without sacrificing suitability, fairness, accuracy or confidentiality.
- **Protect information:** share sensitive information only with authorised people on approved channels and only when they need it. Verify recipients. Never send client or restricted information to personal accounts, public tools or unauthorised parties. If information may have been exposed, report it promptly through the prescribed channel; do not conceal or independently investigate beyond your role.
- **Respect colleagues; do not cover up risk:** for a minor misunderstanding, clarify directly and privately when appropriate. For serious, repeated or urgent misconduct, client harm, a control breach or potential market abuse, escalate promptly even if a senior colleague is involved.
- **Be diplomatic, not evasive:** describe observable facts, explain the impact, ask a clear question and propose a next step. Do not gossip, retaliate or make accusations without evidence.
- **Be honest about uncertainty:** check before committing. If you do not know, say so, find the right expert and give a realistic time for an update.
- **Use proportionate escalation:** do not escalate every routine disagreement as a crisis; do not sit on a significant risk to avoid an awkward conversation.

### A quick decision check: C.L.E.A.R.

- **C — Compliance:** Is the action lawful, authorised and consistent with controls?
- **L — Listen:** What does the client or colleague actually need? What facts are missing?
- **E — Evaluate:** What is the urgency, impact, confidentiality risk and ownership?
- **A — Act:** Take the most constructive action within your authority; protect people and information.
- **R — Report and review:** Escalate when needed, record appropriately and follow through.

This is a personal reasoning aid, not an official scoring rubric. In a forced-choice item, select the response that best addresses the issue promptly, responsibly and within policy; avoid options that delay, conceal, speculate, disclose too widely or promise what you cannot deliver.

---

## 4. English wording to read precisely

- **by 10%** = change of 10% from the starting base; **to 10%** = final level is 10%.
- **respectively** pairs values and categories in the same order.
- **whereas / while** signals a contrast.
- **unless** introduces an exception or condition.
- **at least / no less than** includes the stated boundary; **more than / greater than** excludes equality.
- **no more than / at most** gives an upper limit.
- **year-on-year (YoY)** compares with the same period a year earlier; **quarter-on-quarter (QoQ)** compares with the previous quarter.
- **approximately / roughly** permits a reasonable estimate; do not waste time chasing unnecessary decimal places.
- **does not necessarily mean** warns that one fact alone does not prove a conclusion.
- **confidential / restricted / inside information** should be handled only under the applicable rules and authorised process.

---

## 5. Before starting the live assessment

- Re-read the invitation and the first on-screen instructions. Confirm the actual language options, time limits, permitted calculator/scratch paper and whether you can navigate back.
- Reserve enough uninterrupted time for the duration stated by the employer, plus a buffer. Do not infer Morgan Stanley’s timing from a different Aon or SKEMA test.
- Use a stable connection and powered device; silence notifications and close unrelated tabs.
- Do not start until ready if the test must be completed in one sitting. Follow the employer’s instructions if they say otherwise.
- During the assessment, work independently and use only explicitly permitted tools. Do not share live questions, screenshots or answers.

## Public references

These sources describe **general Aon preparation formats**, not the exact Morgan Stanley assessment:

- [Aon — Prepare for your Online Assessment](https://www.aon.com/en/capabilities/talent-and-rewards/prepare-for-your-online-assessment)
- [Aon — Numerical Reasoning Practice Tasks (PDF)](https://www.aon.com/getmedia/3cc4d7fa-531f-4c0d-b4b3-e88afb130b74/practice-tasks-numerical-reasoning.pdf)
- [Aon — Inductive Reasoning Scales ix Practice Tasks (PDF)](https://www.aon.com/getmedia/54a05144-c659-4bcb-bb18-8613d9081845/practice-tasks-inductive-reasoning-ix.pdf)
- [Aon candidate information (French; includes chatAssess overview)](https://assessment.aon.com/fr-fr/espace-candidat?shortcut=)

**Bottom line:** be precise with data, systematic with patterns, and calm, client-focused, discreet and compliant in workplace scenarios. The invitation—not this guide—defines the actual assessment.
