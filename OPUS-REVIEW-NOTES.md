# Opus review notes — FA26 Start Here study guides

**Reviewer model:** Claude Opus 5.5. The Cursor cloud-agent run metadata reports the model id as **`claude-opus-5-5-high`**, and the agent's system configuration says "powered by Claude Opus 5.5". Both agree. No other model reviewed or edited these files in this pass.  
**Run:** https://cursor.com/agents/bc-1deff9cf-a4d1-53f6-a2ef-1ea845d6d051  
**Date:** Thu Sep 24, 2026, about 3:00–3:25 PM America/Phoenix  
**For:** Arshia Nasr  
**Repo:** private `begoneBOT/bob-jeff` only (visibility checked: `PRIVATE`). No other repo was touched.

## Inputs reviewed

- `uploads/starthere-pack.tgz`: 7 assessment guides + `weekly/2026-09-24-weekly-study-order.md`, extracted into `study-guides/`
- `uploads/start-here-assessment-facts.md`: verified dates (confirmed / provisional / NV)
- `uploads/start-here-rewrite-report.md`: what the previous rewrite changed

## How I checked

- **Answer keys:** I recomputed every numeric answer. The binary/hex/2's-complement/overflow/carry items and all probability items (with exact fractions) were checked by script. I compiled and ran the CSC 335 Java traces (T1–T4, W2 in both forms, W3) with `javac`/`java`, and ran the CSC 337 JavaScript traces (T1–T5, `sort`, `Number`/`parseInt`, the ZIP regex) in Node. The BFS/DFS/Dijkstra/Kruskal/topological-sort traces, the Master Theorem cases, and the proofs were checked by hand.
- **Dates:** a script checked every "weekday + month + day" string against the 2026 calendar.
- **Class blocks:** I checked every Tue/Thu plan row against 252 9:30–10:45, 335 12:30–1:45, 345 2:00–3:15, 337 3:30–4:45, and 380 5:00–6:15.
- **Prep time:** I summed the planned minutes per assessment and per day, then compared them with the deadline stack.

## Issues found

### Wrong answers

**None.** Every answer key in all 7 guides is correct. The fixes below are about clarity, precision, and completeness.

### Precision problems (answers were not wrong, but could mislead)

| Guide | Issue |
|-------|-------|
| 337 Midterm 1 | **ICA-M4 was underspecified.** Its key depended on which ids had which class, and the question never said. |
| 337 Midterm 1 | Excerpt caption said border-box makes "the content shrink". With width 70px and 104px of padding + border, the content collapses to 0 and the box renders 104px. |
| 337 Midterm 1 | GS-337-E1 justification used 2^6 < 100 <= 2^7. The tight bound is 2^k - 1 numbers with k guesses. |
| 335 Midterm | Type erasure was given as the reason `List<int>` is illegal. The real reason is that type arguments can't be primitives. The ConcurrentModificationException claim was stated as guaranteed; it is not. |
| 345 Exam 1 | "Dijkstra fails with negative weights" is now "can return wrong distances". The circular-list append had no empty-list case. |
| 380 Quiz 04 | Garbled notation note: "often written not-A or not-A". |

### Weekday errors (dates kept; weekday corrected)

- Weekly order title and horizon: **"Wed Oct 8"** → Thu Oct 8.
- 335 Start Here: **"Mon Sep 28 – Wed Oct 1"** → Thu Oct 1.
- 252 Test 3 Start Here: **"Thu Sep 24 – Wed Oct 1"** → Wed Sep 30.
- Facts sheet (input, not edited): **"Mon Sep 29"** for 252 HW2 and 380 HW03. Sep 29, 2026 is a **Tuesday**. The guides already used Tue.

### Class-block conflicts and impossible windows

- **Tue Sep 29:** 337 A4 (3:30 PM) was planned "submit before class", and 252 HW2 (7:00 PM) "before 7:00 PM". Tuesday's classes run 9:30–10:45 and 12:30–6:15, so the only real windows are 10:45–12:30 and 6:15–7:00 (45 minutes). **Fixed:** both now target **Mon Sep 28 night**, with 10:45–12:30 as the only backup.
- **Thu Oct 8 buffers:** 335 said "before 12:30 PM" and 345 said "before 2:00 PM (and after 335 midterm)". Both overlap 252 (9:30–10:45), and 345's also overlaps the 335 midterm. **Fixed:** before 9:30 or 10:45–12:30 only.
- **Tue Oct 6:** "after 4:45 PM" in 335, 345, and the weekly order. 380 meets 5:00–6:15. **Fixed:** after 6:15 PM.
- **Tue Oct 6 (337):** "before 3:30 PM: calm buffer" spans three class blocks. **Fixed:** named the real windows.
- **380 Quiz 04, Tue Sep 29:** said only "no study 5:00–6:15". **Fixed:** the whole 9:30–6:15 stack is excluded.

### Study-order and prep-time problems

- **252 Sim 3 (due Wed Oct 7 7:00 PM, confirmed) had no work time.** The Test 3 guide said Oct 2–7 "belongs to Sim 3", but the weekly order gave it no sessions, in the busiest stretch. **Fixed:** sessions run Thu Oct 1 evening through Sun Oct 4, with a Tue Oct 6 night submit target.
- **Overloaded Sep 25–27.** Adding up the per-guide tables, Fri Sep 25 and Sat Sep 26 each carried about 4 hours of study on top of 345 HW2, 337 A4, 252 HW2, and 380 HW03. **Fixed:** the weekly order now has a **Daily load** table splitting "core" from "bank-ahead" minutes. The 335 and 345 guides label their pre-Oct 2 rows the same way. 345's Sat Sep 26 proofs session stays core, because HW1 feedback pointed at proofs.
- **380 light midterm pass sat on Sat Oct 3**, the heaviest 337/335/345 day, for an exam that is Oct 20 at the earliest and tentative. **Moved** to Fri Oct 9.
- **335 logic bug:** Sun Sep 27 lambdas were gated on "252 mock done", but that mock is Monday. The gate is now the Sunday retake.
- **Tue Oct 13 deadline stack wasn't flagged:** 345 PP2 at 2:00 PM (confirmed), 252 HW3 at 7:00 PM (rule-derived), 380 HW4 at 11:59 PM (when released), and 337 A5 at ~3:30 PM (NV), all on a class day. **Added** warnings and Mon Oct 12 targets.
- **Dec 16 has three finals back-to-back** (1:00–8:00 PM). Added as a horizon note.

### Is the prep time enough? (after fixes)

| Assessment | Planned study | Verdict |
|------------|---------------|---------|
| 252 Test 2 (Oct 1, ~25 min likely) | ~6.5 h + HW2 (same skills) | Enough, if the Fri/Sat deep blocks happen. Never drop the Mon mock. |
| 337 Midterm 1 (Oct 6, 75 min per inventory) | ~6.75 h (Sep 30–Oct 5) | Adequate. JS/DOM is thinnest; re-weight Monday after the mock. |
| 335 Midterm (Oct 8) | ~5 h core + 2.5–3 h bank-ahead | Adequate **only if** syllabus-only topics get lecture notes by Sun Oct 4. |
| 345 Exam 1 (Oct 8) | ~5.3 h core + ~2 h bank-ahead | Adequate. Protect Sat Sep 26 proofs and the Mon mock. |
| 380 Quiz 04 (due NV) | Rolling 10–20 min mocks | Fine. Added a "posted with under 24 h notice" fallback. |
| 252 Test 3 (Oct 15) | ~3.5 h light | Right while scope is unpublished. Added a two-deep-day upgrade if Decks 05–07 are named. |
| 380 Midterm (tentative Oct 20) | ~1.5 h light | Right while the date is NV. Added a **contingent** ~4.5 h plan, used only if the date is confirmed. |

The main remaining risk is **Oct 2–5**: 3–4 hours of study a day plus Sim 3, whose size is unknown.

### Labeling problems

- 252 Test 2/3 length was labeled "confirmed" in the headers. The verified facts sheet only confirms the date; ~25 min is the Test 1 pattern. **Now "likely".**
- 335 closed-book: the Start Here said "closed-book per D2L lessons note", while the header said "not in inventory, verify". **Harmonized** to "stated once (facts sheet), re-verify". Coverage "weeks 1–6" vs "weeks 3–6" is now stated consistently.
- 337 75-minute length: **now "per inventory"**. The facts sheet only states the 3:30–4:45 class period.
- Four guides said the copy "lives in a public repository". It is now private `bob-jeff`. Wording fixed; the words-only score policy was kept.
- The weekly order said "leave repo named `begoneBOT/test`, no GitHub push". That was stale and has been replaced.

### Other

- All 8 slide-excerpt `![...](excerpts/*.png)` embeds pointed to files **not in the pack**, so they would render as broken images. They are now text pointers to the box path. The own-words captions are kept.
- Stale PDFs in the repo predated the Start Here rewrite. All 7 were rebuilt and the weekly PDF was added. The text layer shows 0 missing-glyph boxes, and every PDF contains its Start Here block.

## Changes made (files)

- `study-guides/*/assessments/*.md` (7 guides): the fixes above, plus a one-paragraph "If you only read one thing" at the top of each Start Here, an "Is this enough time?" check, stronger self-checks, and a §8c "Opus 5.5 review" changelog in each guide.
- New worked examples: 252 carry-out = 1 subtraction (`0x30 - 0x12`); 335 ASCII UML composition with multiplicities; 345 small Dijkstra with per-step relaxation. New self-check items in every exam guide.
- `study-guides/weekly/2026-09-24-weekly-study-order.md`: rebuilt around a Daily load table (core vs bank-ahead), realistic Tue Sep 29 deadlines, Sim 3 sessions, Oct 13 and Dec 16 horizon warnings, and a PT-vs-Arizona warning.
- All `*.pdf` rebuilt from the reviewed Markdown with `tools/md_to_pdf_chrome.py`, a new, small, reusable script.
- `README.md`: links to the weekly order, these notes, all MD/PDF pairs, and PDF rebuild steps.

## Could NOT verify without sources

I had no access to the Munch box, D2L, Gradescope, course sites, or slides from this environment. So I could **not** verify:

- Any date beyond what the facts sheet says. I trusted its confirmed labels and changed none.
- **Slide contents** behind the excerpt captions (252 Deck 01 p.41, Deck 03 p.35; 335 Classes 1 p.2; 337 Layout p.3; 345 Topic 2 p.68, Topic 3 p.40; 380 Prob 2 p.19, p.47). The captions are internally consistent, but I couldn't compare them with the slides. The 337 p.3 numbers (70px / 50px / 2px / 10px) are taken on trust.
- Whether **Test 2 is 25 minutes**, whether the **337 midterm is 75 minutes**, and whether **335 is closed-book**.
- **Test 1, HW1, and quiz score signals** (the "largest loss" and "weakest quiz" claims) and the Gradescope format notes.
- **Sim 3 size**, and whether it is posted yet. This affects how realistic Oct 2–5 is.
- Whether the **finals times** are Arizona time as the weekly labels them. The facts sheet uses "PT" elsewhere, and after Nov 1 PT is an hour behind Arizona. UA publishes in Arizona time, so they are probably right. Re-check in November.
- The **Asm 2** 5:00 vs 7:00 PM conflict, and the **380 Final Project** Dec 11 vs Thursday conflict. Both are left as recorded.
- Whether the week-6/7 lectures (337 DOM/client-server, 335 JavaFX/Observer/Composite, 345 MCST/topo) will happen before the exams. The guides keep them "as lectured".

## Rejected as unsafe to invent

- **CSC 380 Quiz 04 due date.** It is still **NV**. I did not infer one from the "quizzes every Tuesday" cadence; I only added a check-for-posting habit and a short-notice fallback.
- **CSC 380 Midterm date.** It is still **date-NV** (tentative Oct 20). The new plan is explicitly **contingent** on confirmation and adds no date.
- **Exam clock times** for 252 Test 2/3, 335, and 345. They are still NV; I only named the class periods.
- **Published scope** for any provisional exam. I did not promote Deck 05–07 (252) or week 6–8 topics (337/380) to confirmed scope.
- **252 HW3** stays "rule-derived", and **337 A5** stays NV. **335 P3** stays NV, with no study time planned around it.
- **Sim 3 time estimates.** I gave sessions and a submit target, but no hours, because the project size is unknown. I added no Sim 3 content or hints (the course prohibits AI help).
- **A4 / HW / PP2 solutions.** None added.
