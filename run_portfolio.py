"""
Injects GROQ_API_KEY from .env into portfolio_assistant.html and opens it in the browser.
Run with: python run_portfolio.py
"""
import os, webbrowser, tempfile
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GROQ_API_KEY", "")
if not key:
    print("ERROR: GROQ_API_KEY not found in .env")
    raise SystemExit(1)

html = Path("portfolio_assistant.html").read_text(encoding="utf-8")
html = html.replace("__GROQ_KEY__", key)

tmp = Path(tempfile.mktemp(suffix=".html"))
tmp.write_text(html, encoding="utf-8")
webbrowser.open(tmp.as_uri())
print(f"Portfolio assistant opened. Temp file: {tmp}")
