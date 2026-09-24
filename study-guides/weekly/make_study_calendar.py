"""Render study-calendar-2026-09-24-to-10-08.png from the weekly study order.

Source of truth: weekly-study-order (Thu Sep 24 -> Thu Oct 8, FA26, America/Phoenix).
Usage: python3 make_study_calendar.py [output.png]
"""

import sys
from datetime import date, timedelta

from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

BG = "#0d0f14"
CELL = "#1b1f29"
CELL_CLASS = "#1b1f29"
CELL_OFF = "#12141a"
GRID = "#3a4152"
WHITE = "#ffffff"
MUTED = "#9aa3b5"
RED = "#ff3b3b"
EXAM = "#ff2d55"

COURSE = {
    "252": "#4ea8ff",
    "335": "#3ddc84",
    "337": "#ff9f43",
    "345": "#c792ea",
    "380": "#ffd43b",
}

START = date(2026, 9, 24)
END = date(2026, 10, 8)

# Per day: list of (kind, label). kind: exam | due | flag | core | opt
# Labels are short names only; see weekly-study-order.md for detail.
PLAN = {
    date(2026, 9, 24): [("flag", "345 HW2 LATE open"), ("core", "345 HW2"), ("opt", "252 binary")],
    date(2026, 9, 25): [("core", "345 HW2"), ("core", "252 2's comp"), ("core", "337 A4")],
    date(2026, 9, 26): [("due", "345 HW2 2p"), ("core", "252 MIPS"), ("core", "345 proofs"), ("core", "337 A4")],
    date(2026, 9, 27): [("core", "252 retake"), ("core", "337 A4"), ("core", "252 HW2 draft"), ("core", "380 HW03 draft")],
    date(2026, 9, 28): [("due", "SUBMIT 337 A4"), ("due", "SUBMIT 252 HW2"), ("core", "252 Test2 mock"), ("core", "380 HW03")],
    date(2026, 9, 29): [("due", "337 A4 3:30p"), ("due", "252 HW2 7p"), ("due", "380 HW03 11:59p"), ("opt", "252 flash")],
    date(2026, 9, 30): [("due", "252 Asm2 5p"), ("core", "252 recall"), ("core", "337 HTTP"), ("opt", "380 Q4 Bayes")],
    date(2026, 10, 1): [("exam", "252 TEST 2"), ("core", "337 HTML/CSS"), ("core", "252 Sim3 start")],
    date(2026, 10, 2): [("core", "337 HTML/CSS"), ("core", "335 OOP/UML"), ("core", "345 BFS/DFS"), ("opt", "252 Sim3")],
    date(2026, 10, 3): [("core", "337 JS/DOM"), ("core", "335 lambdas"), ("core", "345 Dijkstra"), ("opt", "252 Sim3")],
    date(2026, 10, 4): [("core", "337 mock"), ("core", "335 generics"), ("core", "345 proofs"), ("opt", "252 Sim3")],
    date(2026, 10, 5): [("core", "337 misses"), ("core", "335 mock"), ("core", "345 mock")],
    date(2026, 10, 6): [("exam", "337 MIDTERM 1"), ("due", "SUBMIT 252 Sim3"), ("opt", "335/345 flash")],
    date(2026, 10, 7): [("due", "252 Sim3 7p"), ("core", "335 light"), ("core", "345 light")],
    date(2026, 10, 8): [("exam", "335 MIDTERM"), ("exam", "345 EXAM 1"), ("opt", "calm only")],
}

AFTER = {
    date(2026, 10, 9): [("opt", "380 MT light")],
    date(2026, 10, 10): [("opt", "Oct 13 stack")],
}

W, H = 2240, 1720
COLS = 7
MARGIN = 36
HEADER_H = 190
DOW_H = 50
FOOTER_H = 250
CELL_W = (W - 2 * MARGIN) // COLS
ROWS = 3
CELL_H = (H - HEADER_H - DOW_H - FOOTER_H - MARGIN) // ROWS


def font(size, bold=False):
    return ImageFont.truetype(FONT_B if bold else FONT, size)


def fit_font(draw, text, max_w, start, bold=True, min_size=16):
    size = start
    while size > min_size:
        f = font(size, bold)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 1
    return font(min_size, bold)


def chip_style(kind, label):
    course = COURSE.get(label.split()[0]) if label[:3].isdigit() else None
    if kind == "exam":
        return EXAM, WHITE, None
    if kind in ("due", "flag"):
        return RED, WHITE, None
    if kind == "core":
        return course or MUTED, "#000000", None
    return None, course or MUTED, course or MUTED


def draw_chip(draw, x, y, w, kind, label, h=54):
    fill, fg, outline = chip_style(kind, label)
    text = label
    if kind == "exam":
        text = "\u2605 " + label
    elif kind == "due" and not label.startswith("SUBMIT"):
        text = "DUE " + label
    elif kind == "due":
        text = label.replace("SUBMIT", "SUBMIT\u2192", 1)
    if fill:
        draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fill)
    else:
        draw.rounded_rectangle([x, y, x + w, y + h], radius=10, outline=outline, width=3)
    f = fit_font(draw, text, w - 22, 31, bold=True, min_size=20)
    draw.text((x + 12, y + h / 2), text, font=f, fill=fg, anchor="lm")
    return h


def main(out):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.text((MARGIN, 30), "Arshia Nasr \u00b7 FA26 Study Calendar", font=font(56, True), fill=WHITE)
    d.text((MARGIN, 100), "Thu Sep 24 \u2192 Thu Oct 8, 2026  \u00b7  Arizona time (America/Phoenix)",
           font=font(30), fill=MUTED)
    blocks = "Tue/Thu class blocks (no study): 252 9:30\u201310:45 \u00b7 335 12:30\u20131:45 \u00b7 345 2:00\u20133:15 \u00b7 337 3:30\u20134:45 \u00b7 380 5:00\u20136:15"
    d.text((MARGIN, 145), blocks, font=fit_font(d, blocks, W - 2 * MARGIN, 26, bold=False), fill=WHITE)

    y0 = HEADER_H
    for i, name in enumerate(["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]):
        x = MARGIN + i * CELL_W
        d.text((x + CELL_W / 2, y0 + DOW_H / 2), name, font=font(28, True),
               fill=WHITE if name in ("TUE", "THU") else MUTED, anchor="mm")

    grid_start = date(2026, 9, 20)
    top = y0 + DOW_H
    for r in range(ROWS):
        for c in range(COLS):
            day = grid_start + timedelta(days=r * 7 + c)
            x = MARGIN + c * CELL_W
            y = top + r * CELL_H
            in_window = START <= day <= END
            class_day = day.weekday() in (1, 3)
            box = [x + 4, y + 4, x + CELL_W - 4, y + CELL_H - 4]
            d.rounded_rectangle(box, radius=14, fill=CELL if in_window else CELL_OFF,
                                outline=WHITE if day == START else GRID, width=4 if day == START else 2)

            label = day.strftime("%b %-d") if day.day == 1 or day == grid_start else str(day.day)
            d.text((x + 20, y + 16), label, font=font(34, True), fill=WHITE if in_window else "#4a5163")
            if in_window and class_day:
                tag = "CLASS DAY"
                tf = font(18, True)
                tw = d.textlength(tag, font=tf)
                d.rounded_rectangle([x + CELL_W - tw - 38, y + 20, x + CELL_W - 18, y + 50],
                                    radius=8, fill=WHITE)
                d.text((x + CELL_W - 28, y + 35), tag, font=tf, fill="#000000", anchor="rm")
                hint = "study <9:30 \u00b7 10:45\u201312:30 \u00b7 6:15+"
                d.text((x + 20, y + 62), hint, font=fit_font(d, hint, CELL_W - 40, 19, bold=False), fill=MUTED)

            items = PLAN.get(day) or AFTER.get(day) or []
            cy = y + (96 if in_window and class_day else 68)
            for kind, text in items:
                cy += draw_chip(d, x + 16, cy, CELL_W - 32, kind, text) + 10

            if not in_window and not items:
                pass
            elif day in AFTER:
                d.text((x + 20, y + CELL_H - 36), "after window", font=font(18), fill="#6b7386")

    fy = top + ROWS * CELL_H + 16
    lx = MARGIN
    legend = [("exam", "EXAM"), ("due", "DUE / SUBMIT"), ("core", "252"), ("core", "335"),
              ("core", "337"), ("core", "345"), ("core", "380"), ("opt", "optional")]
    for kind, text in legend:
        f = font(24, True)
        shown = {"exam": "\u2605 EXAM", "due": "DUE / SUBMIT"}.get(kind, text)
        w = d.textlength(shown, font=f) + 30
        fill, fg, outline = chip_style(kind, text if kind != "opt" else "x")
        if fill:
            d.rounded_rectangle([lx, fy, lx + w, fy + 40], radius=10, fill=fill)
        else:
            d.rounded_rectangle([lx, fy, lx + w, fy + 40], radius=10, outline=WHITE, width=3)
            fg = WHITE
        d.text((lx + 15, fy + 20), shown, font=f, fill=fg, anchor="lm")
        lx += w + 14

    notes = [
        "NV = not verified.  Exam clocks NV (252 Test 2, 335 MT, 345 Exam 1).  380 Quiz 04: scope = Bayes/LOTP/independence, due NV.",
        "Later (light only now):  Fri Oct 9 380 MT light pass  \u00b7  Tue Oct 13 deadline stack  \u00b7  Thu Oct 15 252 Test 3  \u00b7  ~Tue Oct 20 380 Midterm (date NV)",
        "Tue/Thu afternoon deadlines = finish the night before.  Oct 2\u20135 heaviest: keep all three mocks.",
    ]
    ny = fy + 62
    for n in notes:
        d.text((MARGIN, ny), n, font=fit_font(d, n, W - 2 * MARGIN, 25, bold=False), fill=WHITE)
        ny += 42

    img.save(out, optimize=True)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "study-calendar-2026-09-24-to-10-08.png")
