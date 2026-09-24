# CSC 380 — Midterm Study Guide (PROVISIONAL · LIGHT · date NV)

## Start Here

**Guide updated:** 2026-09-24 afternoon (America/Phoenix) -- Start Here rewrite. **LIGHT / date NV.** Reviewed 2026-09-24 evening by Claude Opus 5.5 (see §8c).

> **If you only read one thing:** do nothing midterm-specific until after Oct 8, except Quiz 04 practice. Re-verify the **tentative** Oct 20 date during Oct 13-19. If it is confirmed, use the contingent plan below. If not, keep it light.

### Next scheduled assessment

| Field | Value | Label |
|-------|-------|-------|
| Assessment | CSC 380 Midterm | item exists |
| Date/time | Syllabus says **tentatively** Tue Oct 20, 2026, 5:00-6:15 PM in regular lecture | **date-NV** -- do not treat as fixed |
| Format | **Not published.** Gradescope delivery unconfirmed | NV |
| Coverage | Syllabus weeks 1-8: pandas, viz, probability, RVs, special distributions, covariance/correlation, review | **PROVISIONAL -- schedule-based** |
| Not yet lectured | Special distributions (wk 6), covariance/correlation (wk 7), midterm review (wk 8) | study only as lectured |

Do **not** schedule study during class blocks (Tue/Thu through Dec 9, Arizona time):
CSC 252 9:30-10:45 AM; CSC 335 12:30-1:45 PM; CSC 345 2:00-3:15 PM; CSC 337 3:30-4:45 PM; CSC 380 5:00-6:15 PM.
All times below are **Arizona (MST, UTC-7)**. Combined daily order: `weekly/2026-09-24-weekly-study-order.md`.

**Do not densify** until the instructor confirms the date (re-check D2L / xinchenyu calendar during Oct 13-19). Nearer work: Quiz 04 practice (scope confirmed, due NV), HW03 Sep 29 11:59 PM, HW4 Oct 13 11:59 PM (when released). Finals horizon (not this 14-day window): Wed Dec 16 6:00-8:00 PM.

### Topics to study first (order + WHY)

1. **Quiz 04 published subset (`380-Q04-*`)** -- WHY: Bayes / LOTP / independence is the only **confirmed** midterm-overlapping slice; use the Quiz 04 guide.
2. **`380-L-prob1` + `380-L-comb` -- conditional probability + combinations** -- WHY: weeks 2-3 already lectured; combinations was missing from older drafts.
3. **`380-L-pandas` + `380-L-viz`** -- WHY: week 1; short recall, not a marathon.
4. **`380-L-rv` then `380-L-special` / `380-L-corr`** -- WHY: weeks 4-7; add only after lecture.
5. **Do not start** modeling / regression / classification (post-midterm).

**Confirmed vs schedule-based:** Nothing about the midterm date or blueprint is confirmed. Weeks 1-8 are a syllabus timeline, not a published scope.

### Day-by-day tasks (LIGHT; no class-block study)

| When | Window | Task | Guide / slides / problems | Min |
|------|--------|------|---------------------------|-----|
| Now - Oct 1 | After HW03 / 252 Test 2 only | Quiz 04 practice. **Not** a midterm marathon. | Quiz 04 guide | see Quiz 04 |
| Fri Oct 9 | No class; after the Oct 8 exam cluster | One light pass over the `380-L-*` map + L1-L10. (Moved from Sat Oct 3, which is the heaviest 337/335/345 prep day.) | Sec 2-4 | 35 |
| Mon Oct 12 | Anytime | Aim to finish HW4 written + Code tonight, if released. Tue Oct 13 is a class day that also carries CSC 345 PP2 (2:00 PM) and 252 HW3 (7:00 PM, rule-derived). | HW4 | HW4 |
| Tue Oct 13 | HW4 due 11:59 PM (written + Code). Free gaps: before 9:30, 10:45-12:30, after 6:15 | Submit HW4. Then **re-verify** midterm date/scope. | D2L / https://xinchenyu.github.io/csc380/calendar/ | 10 |
| Oct 13-19 | Outside class blocks | Re-verify date. Densify **only if confirmed**. | -- | -- |
| If Oct 20 is confirmed | Sit 5:00-6:15 PM. Night before: calm review only | L1-L11 + Quiz 04 fluency | 30 light |

**Contingent plan -- use ONLY if the Oct 20 date is confirmed by about Tue Oct 13.** This adds no new date; it only says how to use the week if the tentative date holds. Thu Oct 15 is CSC 252 Test 3, so the deep days are after it:

| When (contingent) | Task | Min |
|-------------------|------|-----|
| Fri Oct 16 | pandas + viz recall (L8, L9); random variables (L3, L4) | 60 |
| Sat Oct 17 | Weeks 4-7 **as lectured**: distributions, covariance/correlation (L5); redo Quiz 04 Mock C and D | 90 |
| Sun Oct 18 | 60-minute paper mock: L1-L11 plus two Quiz 04 mocks; then redo misses | 80 |
| Mon Oct 19 | Light review of misses only | 30 |
| Tue Oct 20 | Calm buffer before 9:30 or 10:45-12:30 only; exam 5:00-6:15 if confirmed | 10 |

**Is this enough time?** The light plan (~1.5 hours before Oct 13) is right while the date is NV. If the date is confirmed, the contingent plan adds about 4.5 hours, which is adequate if it is a lecture-period (5:00-6:15) midterm as tentatively listed.

### Final self-check (light)

- [ ] Weeks 1-8 concept map reviewed
- [ ] Quiz 04 topics solid
- [ ] L1-L11 correct
- [ ] Date and scope re-verified during Oct 13-19 **before** densifying
- [ ] No regression/NN early study
- [ ] No invented Tuesday quiz dates

### Slide excerpts

Reuse the Quiz 04 excerpts (Probability 2 short p.19 LOTP and p.47 Bayes) under `csc380/assessments/excerpts/`. For pandas/viz, review `csc380-26f380_data1.pdf` on the harvest path -- no extra excerpt pulled (keep this guide light).

---


**Banner — date NEEDS VERIFICATION; scope PROVISIONAL; LIGHT guide.**
- **Date:** the syllabus says **"tentatively"** Tue Oct 20, 2026, 5:00–6:15 PM Arizona time, in the regular lecture. The calendar also lists Oct 20. The date stays **Needs verification** until the instructor confirms it.
- **Scope:** coverage is **not published**. It is provisional, from syllabus weeks 1–8: pandas, visualization, probability, random variables and distributions, covariance and correlation, and midterm review.
- **Light only:** this is a concept map plus a small practice set. Do not do dense prep that assumes a confirmed date.

Canonical maps: `csc380-topic-map.md` · `announced-assessments-inventory-2026-09-24.md` · `site-audit-2026-09-24.md`

## 1. Header

| Field | Value | Status |
|-------|-------|--------|
| Course | CSC 380 Principles of Data Science (FA26), TuTh 5:00–6:15 PM, M Pacheco ILC 130 | Confirmed |
| Assessment | Midterm (light provisional guide) | Item exists |
| Date/time | Tentatively Tue Oct 20, 2026, 5:00–6:15 PM Arizona | **Needs verification** |
| Format | **Not published.** Gradescope delivery is not confirmed. | NV |
| Coverage | Syllabus weeks 1–8 | **PROVISIONAL** |
| Not yet lectured | Special Distributions (week 6), Covariance/Correlation (week 7), and Midterm Review (week 8) are still ahead | Expected |
| Guide updated | 2026-09-24 (America/Phoenix) — Opus + Content-fold (light) | |

All times are **Arizona time (MST)**.


### Sources (Content-pass 2026-09-24)

| Source | Role |
|--------|------|
| Content `Resources/quiz01_03.pdf` | Early quiz-style practice grain (descriptive stats; sample space; LOTP+Bayes). Overlaps Quiz 04 published subset. |
| Content `Homework/homework01.zip`, `homework02.pdf`, `homework03.pdf` | HW practice context (pandas/viz; probability; Bayes/independence). Not midterm solutions. |
| Syllabus weeks 1-8 | **PROVISIONAL** midterm coverage map |


---

## 2. Topic checklist (light concept map)

| Order | Section ID | Topic (syllabus week — **provisional**) |
|------:|------------|-----------------------------------------|
| 1 | `380-L-intro` | Course overview (wk 1) |
| 2 | `380-L-pandas` | Basic data manipulation with pandas (wk 1) |
| 3 | `380-L-viz` | Basic visualization (wk 1) |
| 4 | `380-L-prob1` | Probability intro; conditional probability (wk 2) |
| 5 | `380-L-comb` | Combinations (wk 3) — *new in this review* |
| 6 | `380-Q04-indep` | Independence (wk 3; also Quiz 04) |
| 7 | `380-Q04-bayes` / `380-Q04-lotp` | Bayes and LOTP (Quiz 04 **published** subset) |
| 8 | `380-L-rv` | Random variables; distributions; discrete vs continuous (wk 4–5) |
| 9 | `380-L-special` | Special distributions (wk 6 — as lectured) |
| 10 | `380-L-corr` | Covariance and correlation (wk 7 — as lectured) |
| 11 | `380-L-review` | Midterm review (wk 8) |

Do **not** start the post-midterm material (modeling, regression, classification).

---

## 3. Mini explanations

- **pandas.** These are standard pandas; match your class notebooks.
  - Filter rows: `df[df["age"] > 30]`
  - Select columns: `df[["a", "b"]]`
  - Group means: `df.groupby("team")["score"].mean()`
  - Missing values: `df.isna().sum()` and `df.dropna()`
- **Chart choice.**

| What you want to show | Chart |
|-----------------------|-------|
| Distribution of one numeric variable | Histogram or box plot |
| Two numeric variables | Scatter plot |
| Comparison across categories | Bar chart |
| Change over time | Line chart |

- **Combinations.** C(n, k) = n! / (k!(n-k)!) counts **unordered** selections. Permutations P(n, k) = n! / (n-k)! count **ordered** ones.
- **Random variables.** For a discrete X, E[X] = sum  x·P(x). Var(X) = E[X^2] - (E[X])^2.
- **Special distributions** (as lectured).
  - Bernoulli(p): mean p, variance p(1-p).
  - Binomial(n, p): mean np, variance np(1-p).
  - Uniform, Poisson, Normal, and Exponential follow if covered.
- **Covariance and correlation.** Cov(X, Y) = E[(X - muX)(Y - muY)]. Corr = Cov / (sigmaX·sigmaY), which always lies in [-1, 1]. Correlation measures **linear** association only. Check which denominator the course uses for sample covariance (n or n - 1).
- **Bayes, LOTP, independence.** These are the published Quiz 04 topics; see the Quiz 04 Practice Guide.

---

## 4. Light practice (self-contained)

**L1 (recall).** Define independence, and write correlation in terms of covariance.

**L2 (combinations).** How many 3-person committees can be chosen from 7 people? What is the probability of exactly 2 heads in 4 fair coin flips?

**L3 (random variable).** For a fair six-sided die X, find E[X] and Var(X).

**L4 (binomial).** X ~ Binomial(10, 0.3). Find E[X] and Var(X).

**L5 (covariance/correlation).** For X = [1, 2, 3] and Y = [2, 4, 6], find the sample covariance (denominator n - 1) and the correlation.

**L6 (Bayes).** P(H) = 0.2, P(E | H) = 0.9, P(E | not-H) = 0.3. Find P(H | E).

**L7 (independence).** P(A) = 0.25, P(B) = 0.4, P(A and B) = 0.1. Are A and B independent?

**L8 (visualization).** Pick a chart for (a) the distribution of house prices, (b) price vs. square footage, (c) average price by neighborhood.

**L9 (pandas).** Write one line that gives the mean `score` for each `team` in DataFrame `df`.

**L10 (planning).** Why must the tentative Oct 20 date be re-verified before making a dense plan?


**L11 (Content grain — Practice recommendation).** Two labs: Lab A has 90 students (30% prefer Python); Lab B has 60 students (70% prefer Python). (a) P(prefer Python). (b) Given prefer-Python, P(Lab B). (Cite Content quiz01_03 Quiz-03 style; numbers changed.)

## 4b. Format reminder — **Practice recommendation**

The Gradescope format notes show that quizzes are about 1.5 points on a single page, and each homework has **two** items (written and Code). The **midterm format is not published**. For practice, write L2–L7 by hand, one per half-page, with every step shown. This is a generic habit, not a claimed midterm format.

<!-- PAGEBREAK -->

## 5. ANSWER KEY

**L1.** Independence means P(A and B) = P(A)·P(B). Corr(X, Y) = Cov(X, Y) / (sigmaX·sigmaY).

**L2.** C(7, 3) = 35. P(exactly 2 heads in 4 flips) = C(4, 2)/2^4 = 6/16 = **0.375**.

**L3.** E[X] = 3.5. E[X^2] = 91/6. Var(X) = 91/6 - 12.25 = **35/12 ~= 2.917**.

**L4.** E[X] = 10·0.3 = **3**. Var(X) = 10·0.3·0.7 = **2.1**.

**L5.** The means are 2 and 4. The deviations are (-1, 0, 1) for X and (-2, 0, 2) for Y, so the sum of products is 2 + 0 + 2 = 4. Sample covariance = 4 / (3 - 1) = **2**. The sample standard deviations are 1 and 2, so correlation = 2 / (1·2) = **1**, a perfect positive linear relationship. With the population denominator, the covariance is 4/3, and the correlation is still 1.

**L6.** P(E) = 0.9·0.2 + 0.3·0.8 = 0.42. P(H | E) = 0.18 / 0.42 = **3/7 ~= 0.429**.

**L7.** 0.25 x 0.4 = 0.1 = P(A and B). **Yes, independent.**

**L8.** (a) Histogram (or box plot). (b) Scatter plot. (c) Bar chart.

**L9.** `df.groupby("team")["score"].mean()`

**L10.** The syllabus marks the date as "tentative". The context rule is never to treat an unconfirmed date as fixed, so re-check on D2L, the course site, or in class during Oct 13–19 before planning around it.


**L11.** (a) 0.3*(90/150) + 0.7*(60/150) = 0.3*0.6 + 0.7*0.4 = 0.18 + 0.28 = **0.46**. (b) 0.28/0.46 = **14/23 ~= 0.609**.


---

## 6. Common mistakes + readiness (light)

- Studying regression or neural networks early.
- Treating the tentative Oct 20 date as fixed.
- Skipping Quiz 04 fluency, since Bayes, LOTP, and independence are the only **published** subset.
- Mixing up combinations (unordered) with permutations (ordered).
- Reading a correlation near 0 as "no relationship", when it only means no **linear** relationship.
- Inventing quiz dates from the Tuesday cadence.

**Ready (light):**
- [ ] Weeks 1–8 concept map reviewed
- [ ] Quiz 04 topics solid
- [ ] L1-L11 correct
- [ ] Date and scope re-verified during Oct 13–19 **before** densifying

---


> **Start Here (top of this guide) is the canonical day-by-day.** The later prep table is kept as a short copy.
## 7. Prep plan (light — no day-before cram that assumes a confirmed date)

| Window | Action |
|--------|--------|
| Now – early Oct | Quiz 04 practice and HW3/HW4 probability. **Not** a midterm marathon. |
| Fri Oct 9 | One light pass over the `380-L-*` concept map and L1–L10 (after the Oct 8 exam cluster) |
| Tue Oct 13 | HW4 due 11:59 PM (written plus Code); aim to finish Mon Oct 12 night |
| Oct 13–19 | **Re-verify** the date and scope on D2L, the site, or the tracker. Densify only after that. |
| If Oct 20 is confirmed | Use the contingent plan in Start Here (Fri Oct 16 - Mon Oct 19). Sit the midterm at 5:00–6:15 PM. The night before, calm review only. |

Do deeper work Mon/Wed/Fri and weekends; keep Tuesdays and Thursdays light.

---

## 8. Changes in this review (2026-09-24)

- Kept the **date NV** and **LIGHT** banners unchanged in meaning. Changed "PT" to Arizona time.
- **Made the answer key self-contained.** The old key said "see the Quiz 04 guide" for Bayes; all L-items now have worked answers.
- Added the week-3 **Combinations** topic, which was merged into independence and had no practice. Added practice on random variables, the binomial distribution, covariance/correlation, visualization, and pandas (L2–L5, L8–L9).
- Noted that the weeks 6–8 lectures have not happened yet.
- Kept the new practice to ten short items so the guide stays light.


## 8b. Content-fold (2026-09-24, America/Phoenix)

- Light only: cited Content quiz01_03 + HW01-03; added L11 similar-style LOTP+Bayes drill. Date/scope banners unchanged (NV / PROVISIONAL / LIGHT). No dense invent.

## 8c. Opus 5.5 review (2026-09-24 evening, America/Phoenix)

- Recomputed L1-L11 (combinations, die mean/variance = 35/12, binomial, sample covariance/correlation, Bayes, independence, the L11 LOTP). **No wrong answers found.**
- **Order fix:** the one light 380 pass moved from Sat Oct 3, the heaviest 337/335/345 prep day, to Fri Oct 9, after the exam cluster. The midterm is Oct 20 at the earliest, and that date is tentative.
- Added a Mon Oct 12 HW4 target, because Tue Oct 13 is a class day that also carries 345 PP2 and 252 HW3.
- Added a clearly labeled **contingent** plan (Fri Oct 16 - Tue Oct 20) to use **only if** the tentative Oct 20 date is confirmed. **No date was invented or promoted**; the midterm is still **date-NV**.
- Converted the remaining non-ASCII math symbols to ASCII, to match the Quiz 04 guide's PDF-safe convention.

## 9. Disclaimer

Study aid only — not for submitted work. Follow CSC 380 and UA policies. The title marks provisional/NV status on purpose.
