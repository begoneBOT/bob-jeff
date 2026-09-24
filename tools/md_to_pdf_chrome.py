"""Render study-guide Markdown to PDF via python-markdown + headless Chrome.

Usage: python3 tools/md_to_pdf_chrome.py [files...]   (default: every study-guides/**/*.md)
Needs: pip install markdown; google-chrome (or chromium) on PATH.
"""
import glob
import html
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time

import markdown

CSS = """
@page { size: Letter; margin: 0.7in 0.7in; }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 10.5pt; line-height: 1.4; color: #111; }
h1 { font-size: 18pt; border-bottom: 2px solid #333; padding-bottom: 4px; }
h2 { font-size: 14pt; margin-top: 18px; border-bottom: 1px solid #aaa; }
h3 { font-size: 12pt; margin-top: 14px; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9.5pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #999; padding: 3px 5px; vertical-align: top; text-align: left; }
th { background: #eee; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 9pt; background: #f3f3f3; padding: 0 2px; }
pre { background: #f6f6f6; border: 1px solid #ddd; padding: 6px 8px; font-size: 8.8pt; white-space: pre-wrap; page-break-inside: avoid; }
pre code { background: none; padding: 0; }
blockquote { border-left: 4px solid #4a78c2; margin: 8px 0; padding: 4px 10px; background: #f2f6fc; }
.pagebreak { page-break-after: always; }
"""


def chrome():
    for name in ("google-chrome", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    sys.exit("no Chrome/Chromium found")


def render(md_path, browser):
    text = open(md_path, encoding="utf-8").read()
    text = text.replace("<!-- PAGEBREAK -->", '<div class="pagebreak"></div>')
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    title = html.escape(os.path.splitext(os.path.basename(md_path))[0])
    page = f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>"
    pdf_path = os.path.splitext(md_path)[0] + ".pdf"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp.write(page)
    # Some headless Chrome builds write the PDF and then never exit, so wait for a stable file
    # and then stop only the process group started here.
    profile = tempfile.mkdtemp(prefix="md2pdf-profile-")
    if os.path.exists(pdf_path):
        os.unlink(pdf_path)
    proc = subprocess.Popen(
        [browser, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
         f"--user-data-dir={profile}", f"--print-to-pdf={os.path.abspath(pdf_path)}",
         f"file://{tmp.name}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True,
    )
    try:
        last, stable, deadline = -1, 0, time.time() + 90
        while time.time() < deadline and proc.poll() is None:
            size = os.path.getsize(pdf_path) if os.path.exists(pdf_path) else -1
            stable = stable + 1 if size > 0 and size == last else 0
            if stable >= 3:
                break
            last = size
            time.sleep(0.5)
        if not os.path.exists(pdf_path) or os.path.getsize(pdf_path) == 0:
            raise RuntimeError(f"no PDF produced for {md_path}")
    finally:
        if proc.poll() is None:
            os.killpg(proc.pid, signal.SIGTERM)
            proc.wait(timeout=10)
        os.unlink(tmp.name)
        shutil.rmtree(profile, ignore_errors=True)
    return pdf_path


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob("study-guides/**/*.md", recursive=True))
    browser = chrome()
    for f in files:
        print(render(f, browser))
