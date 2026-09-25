"""Render study-calendar-2026-09-24-to-10-08.png: cross-course PDF switch order by day.

Cells list which class / guide PDF to open next (switch order), not topics inside a course.
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

# (number, name, when) for the banner, soonest first.
PDF_ORDER = [
    (1, "345 Exam1", "after HW2 (late \u2264 Sat 9/26 2p)"),
    (2, "337 Midterm1", "after A4 (A4 Tue 9/29 3:30p)"),
    (3, "252 Test2", "Thu 10/1"),
    (4, "380 Quiz04", "due NV \u00b7 in gaps"),
    (5, "335 Midterm", "Thu 10/8 (then 345 Exam1)"),
    (6, "252 Test3", "Thu 10/15 \u00b7 LIGHT"),
    (7, "380 Mid", "~Tue 10/20 NV \u00b7 LIGHT"),
    (8, "Weekly overview", "last"),
]

# Per day: switch order of class/PDF short names. Prefix "*" = exam that day, "~" = light.
# A (time, name) tuple is a Study Sessions calendar block (Arizona time).
PLAN = {
    date(2026, 9, 24): [("7\u20139p", "252 Test2")],
    date(2026, 9, 25): [("8:30", "345 Exam1"), ("10:00", "252 Test2"), ("12:00", "337 Mid1/A4"),
                        ("2:00", "252 Test2"), ("4:30", "335 Mid"), ("6:00", "345 Exam1"),
                        ("7:00", "380 Quiz04"), ("8:30", "252 Test2")],
    date(2026, 9, 26): [("8:00", "345 HW2/Exam1"), ("10:00", "252"), ("1:00", "337 A4"),
                        ("3:00", "252 Test2"), ("4:30", "335"), ("7:00", "380")],
    date(2026, 9, 27): ["337 A4", "252 HW2", "380 HW03"],
    date(2026, 9, 28): ["252 Test2", "337 A4", "252 HW2"],
    date(2026, 9, 29): ["380 HW03", "~252 Test2"],
    date(2026, 9, 30): ["252 Test2", "337 Mid1", "380 Quiz04"],
    date(2026, 10, 1): ["*252 Test2", "337 Mid1"],
    date(2026, 10, 2): ["337 Mid1", "335 Mid", "345 Exam1"],
    date(2026, 10, 3): ["337 Mid1", "335 Mid", "345 Exam1"],
    date(2026, 10, 4): ["337 Mid1", "335 Mid", "345 Exam1"],
    date(2026, 10, 5): ["337 Mid1", "335 Mid", "345 Exam1"],
    date(2026, 10, 6): ["*337 Mid1", "~335 Mid", "~345 Exam1"],
    date(2026, 10, 7): ["~335 Mid", "~345 Exam1"],
    date(2026, 10, 8): ["*335 Mid", "*345 Exam1"],
}

DUE = {
    date(2026, 9, 26): ["345 HW2 late 2p"],
    date(2026, 9, 28): ["submit A4 + 252 HW2"],
    date(2026, 9, 29): ["337 A4 3:30p", "252 HW2 7p", "380 HW03 11:59p"],
    date(2026, 9, 30): ["252 Asm2 5p"],
    date(2026, 10, 7): ["252 Sim3 7p"],
}

AFTER = {
    date(2026, 10, 9): ["~380 Mid"],
    date(2026, 10, 10): ["~252 Test3"],
}

W, H = 2240, 2200
COLS = 7
MARGIN = 36
BANNER_Y = 180
BANNER_H = 330
DOW_H = 50
FOOTER_H = 190
CELL_W = (W - 2 * MARGIN) // COLS
ROWS = 3
TOP = BANNER_Y + BANNER_H + DOW_H
CELL_H = (H - TOP - FOOTER_H) // ROWS


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


def color_of(name):
    return COURSE.get(name[:3], MUTED)


def draw_step(d, x, y, w, n, raw, h=56):
    if isinstance(raw, tuple):
        return draw_timed(d, x, y, w, *raw)
    exam = raw.startswith("*")
    light = raw.startswith("~")
    name = raw.lstrip("*~")
    col = color_of(name)
    d.ellipse([x, y + h / 2 - 17, x + 34, y + h / 2 + 17], fill=WHITE)
    d.text((x + 17, y + h / 2), str(n), font=font(22, True), fill="#000000", anchor="mm")
    cx = x + 44
    cw = w - 44
    if exam:
        d.rounded_rectangle([cx, y, cx + cw, y + h], radius=10, fill=EXAM)
        text, fg = "\u2605 " + name, WHITE
    elif light:
        d.rounded_rectangle([cx, y, cx + cw, y + h], radius=10, outline=col, width=3)
        text, fg = name, col
    else:
        d.rounded_rectangle([cx, y, cx + cw, y + h], radius=10, fill=col)
        text, fg = name, "#000000"
    d.text((cx + 12, y + h / 2), text, font=fit_font(d, text, cw - 22, 32, min_size=20), fill=fg, anchor="lm")
    return h


def draw_timed(d, x, y, w, when, name, h=42):
    tf = fit_font(d, when, 62, 21, min_size=15)
    d.text((x + 64, y + h / 2), when, font=tf, fill=WHITE, anchor="rm")
    cx = x + 72
    cw = w - 72
    d.rounded_rectangle([cx, y, cx + cw, y + h], radius=9, fill=color_of(name))
    d.text((cx + 10, y + h / 2), name, font=fit_font(d, name, cw - 18, 26, min_size=18),
           fill="#000000", anchor="lm")
    return h


def draw_banner(d):
    d.rounded_rectangle([MARGIN, BANNER_Y, W - MARGIN, BANNER_Y + BANNER_H - 16], radius=16,
                        fill="#161a23", outline=WHITE, width=3)
    d.text((MARGIN + 24, BANNER_Y + 18), "PDF switch order (open these guides in this order)",
           font=font(36, True), fill=WHITE)
    col_w = (W - 2 * MARGIN - 48) // 4
    box_h = 112
    for i, (n, name, when) in enumerate(PDF_ORDER):
        r, c = divmod(i, 4)
        x = MARGIN + 24 + c * col_w
        y = BANNER_Y + 76 + r * (box_h + 12)
        col = color_of(name)
        d.rounded_rectangle([x, y, x + col_w - 14, y + box_h], radius=12, fill=CELL, outline=col, width=4)
        d.ellipse([x + 12, y + 14, x + 52, y + 54], fill=WHITE)
        d.text((x + 32, y + 34), str(n), font=font(26, True), fill="#000000", anchor="mm")
        d.text((x + 64, y + 34), name, font=fit_font(d, name, col_w - 92, 30), fill=col, anchor="lm")
        d.text((x + 16, y + 84), when, font=fit_font(d, when, col_w - 44, 26, bold=False), fill=WHITE, anchor="lm")


def main(out):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.text((MARGIN, 26), "Arshia Nasr \u00b7 FA26 \u00b7 What to open next", font=font(54, True), fill=WHITE)
    d.text((MARGIN, 94), "Thu Sep 24 \u2192 Thu Oct 8, 2026  \u00b7  Arizona time  \u00b7  1\u21922\u21923 = switch order that day",
           font=font(29), fill=MUTED)
    blocks = "Tue/Thu class blocks (no study): 252 9:30\u201310:45 \u00b7 335 12:30\u20131:45 \u00b7 345 2:00\u20133:15 \u00b7 337 3:30\u20134:45 \u00b7 380 5:00\u20136:15"
    d.text((MARGIN, 136), blocks, font=fit_font(d, blocks, W - 2 * MARGIN, 26, bold=False), fill=WHITE)

    draw_banner(d)

    y0 = BANNER_Y + BANNER_H
    for i, name in enumerate(["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]):
        x = MARGIN + i * CELL_W
        d.text((x + CELL_W / 2, y0 + DOW_H / 2), name, font=font(28, True),
               fill=WHITE if name in ("TUE", "THU") else MUTED, anchor="mm")

    grid_start = date(2026, 9, 20)
    for r in range(ROWS):
        for c in range(COLS):
            day = grid_start + timedelta(days=r * 7 + c)
            x = MARGIN + c * CELL_W
            y = TOP + r * CELL_H
            in_window = START <= day <= END
            class_day = in_window and day.weekday() in (1, 3)
            d.rounded_rectangle([x + 4, y + 4, x + CELL_W - 4, y + CELL_H - 4], radius=14,
                                fill=CELL if in_window else CELL_OFF,
                                outline=WHITE if day == START else GRID, width=4 if day == START else 2)

            label = day.strftime("%b %-d") if day.day == 1 or day == grid_start else str(day.day)
            d.text((x + 20, y + 16), label, font=font(34, True), fill=WHITE if in_window else "#4a5163")
            if class_day:
                tag = "CLASS DAY"
                tf = font(18, True)
                tw = d.textlength(tag, font=tf)
                d.rounded_rectangle([x + CELL_W - tw - 38, y + 20, x + CELL_W - 18, y + 50], radius=8, fill=WHITE)
                d.text((x + CELL_W - 28, y + 35), tag, font=tf, fill="#000000", anchor="rm")
                hint = "study <9:30 \u00b7 10:45\u201312:30 \u00b7 6:15+"
                d.text((x + 20, y + 62), hint, font=fit_font(d, hint, CELL_W - 40, 19, bold=False), fill=MUTED)
            if day == START:
                d.text((x + 20, y + 84), "tonight after 6:15", font=font(19, True), fill=WHITE)

            steps = PLAN.get(day) or AFTER.get(day) or []
            cy = y + (114 if day == START else 96 if class_day else 68)
            timed = any(isinstance(s, tuple) for s in steps)
            for n, raw in enumerate(steps, 1):
                cy += draw_step(d, x + 14, cy, CELL_W - 28, n, raw) + (7 if timed else 12)

            dues = DUE.get(day, [])
            dy = y + CELL_H - 20 - 32 * len(dues)
            for t in dues:
                text = t if t.startswith("submit") else "DUE " + t
                d.text((x + 20, dy), text, font=fit_font(d, text, CELL_W - 40, 24, min_size=16), fill=RED)
                dy += 32
            if day in AFTER:
                d.text((x + 20, y + CELL_H - 44), "after window", font=font(18), fill="#6b7386")

    fy = TOP + ROWS * CELL_H + 14
    lx = MARGIN
    legend = [("exam", "\u2605 EXAM day"), ("light", "light review"), ("due", "DUE (red text)")] + \
             [("core", k) for k in COURSE]
    for kind, text in legend:
        f = font(24, True)
        w = d.textlength(text, font=f) + 30
        if kind == "exam":
            d.rounded_rectangle([lx, fy, lx + w, fy + 40], radius=10, fill=EXAM)
            fg = WHITE
        elif kind == "light":
            d.rounded_rectangle([lx, fy, lx + w, fy + 40], radius=10, outline=WHITE, width=3)
            fg = WHITE
        elif kind == "due":
            fg = RED
        else:
            d.rounded_rectangle([lx, fy, lx + w, fy + 40], radius=10, fill=COURSE[text])
            fg = "#000000"
        d.text((lx + 15, fy + 20), text, font=f, fill=fg, anchor="lm")
        lx += w + 14

    notes = [
        "Homework first, then that course's guide PDF.  337 Mid1 PDF only after A4 is in.  Weekly overview goes last.  Later LIGHT: 252 Test3 Thu Oct 15.",
        "Thu\u2013Sat times = Study Sessions calendar blocks.  NV = not verified: exam clocks (252 Test2, 335 Mid, 345 Exam1), 380 Quiz04 due, 380 Mid date (~Tue Oct 20).",
    ]
    ny = fy + 60
    for n in notes:
        d.text((MARGIN, ny), n, font=fit_font(d, n, W - 2 * MARGIN, 25, bold=False), fill=WHITE)
        ny += 42

    img.save(out, optimize=True)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "study-calendar-2026-09-24-to-10-08.png")
