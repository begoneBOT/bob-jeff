# bob+jeff

Private scratch repository for FA26 study guides (Arshia Nasr, America/Phoenix).

## Start here

- **Weekly study order (Thu Sep 24 → Thu Oct 8):** [Markdown](<study-guides/weekly/2026-09-24-weekly-study-order.md>) · [PDF](<study-guides/weekly/2026-09-24-weekly-study-order.pdf>)
- **Latest review notes:** [OPUS-REVIEW-NOTES.md](OPUS-REVIEW-NOTES.md)

## Assessment guides

Each guide opens with a **Start Here** block: the next assessment with confirmed / provisional / NV labels, topic order with reasons, a day-by-day plan that avoids class blocks, and a final self-check.

| Guide | Markdown | PDF |
|-------|----------|-----|
| CSC 252 — Test 2 | [md](<study-guides/csc252/assessments/CSC 252 — Test 2 Study Guide.md>) | [pdf](<study-guides/csc252/assessments/CSC 252 — Test 2 Study Guide.pdf>) |
| CSC 252 — Test 3 | [md](<study-guides/csc252/assessments/CSC 252 — Test 3 Study Guide.md>) | [pdf](<study-guides/csc252/assessments/CSC 252 — Test 3 Study Guide.pdf>) |
| CSC 335 — Midterm | [md](<study-guides/csc335/assessments/CSC 335 — Midterm Study Guide.md>) | [pdf](<study-guides/csc335/assessments/CSC 335 — Midterm Study Guide.pdf>) |
| CSC 337 — Midterm 1 | [md](<study-guides/csc337/assessments/CSC 337 — Midterm 1 Study Guide.md>) | [pdf](<study-guides/csc337/assessments/CSC 337 — Midterm 1 Study Guide.pdf>) |
| CSC 345 — Exam 1 | [md](<study-guides/csc345/assessments/CSC 345 — Exam 1 Study Guide.md>) | [pdf](<study-guides/csc345/assessments/CSC 345 — Exam 1 Study Guide.pdf>) |
| CSC 380 — Quiz 04 Practice | [md](<study-guides/csc380/assessments/CSC 380 — Quiz 04 Practice Guide.md>) | [pdf](<study-guides/csc380/assessments/CSC 380 — Quiz 04 Practice Guide.pdf>) |
| CSC 380 — Midterm | [md](<study-guides/csc380/assessments/CSC 380 — Midterm Study Guide.md>) | [pdf](<study-guides/csc380/assessments/CSC 380 — Midterm Study Guide.pdf>) |

Courses included: CSC 252, CSC 335, CSC 337, CSC 345, and CSC 380.

## Rebuilding PDFs

```bash
pip install markdown
python3 tools/md_to_pdf_chrome.py            # all study-guides/**/*.md
python3 tools/md_to_pdf_chrome.py path/to.md # one file
```

Requires `google-chrome` or `chromium` on PATH.

Live copies also live on the Munch box at `/home/box/shared/munch/study-guides/`. The slide-excerpt PNGs referenced by the guides exist only there (`<course>/assessments/excerpts/`).
