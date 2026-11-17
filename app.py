"""CivicConnect AI: evidence-first verification prototype."""
from datetime import datetime, timezone
import json
import os
import re
import secrets
import sqlite3
import uuid
from pathlib import Path

from flask import Flask, abort, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
DB_PATH = BASE_DIR / "civicconnect.db"
ALLOWED = {"image": {"png", "jpg", "jpeg", "webp", "gif"},
           "video": {"mp4", "webm", "mov", "m4v"},
           "audio": {"mp3", "wav", "ogg", "m4a", "webm"}}
MAX_BYTES = 25 * 1024 * 1024

app = Flask(__name__)
app.secret_key = os.environ.get("CIVICCONNECT_SECRET") or secrets.token_hex(32)
app.config["MAX_CONTENT_LENGTH"] = MAX_BYTES
UPLOAD_DIR.mkdir(exist_ok=True)


def db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    with db() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS verifications (
            id TEXT PRIMARY KEY, kind TEXT NOT NULL, title TEXT NOT NULL,
            status TEXT NOT NULL, confidence TEXT NOT NULL, explanation TEXT NOT NULL,
            evidence TEXT NOT NULL, created_at TEXT NOT NULL, original_name TEXT
        )""")


def save_report(kind, title, status, confidence, explanation, evidence, original_name=None):
    report_id = uuid.uuid4().hex[:12]
    created = datetime.now(timezone.utc).isoformat()
    with db() as con:
        con.execute("INSERT INTO verifications VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (report_id, kind, title[:160], status, confidence, explanation,
                     json.dumps(evidence), created, original_name))
    return report_id


def search_links(query):
    from urllib.parse import quote_plus
    q = quote_plus(query[:300])
    return [{"label": "Search the claim on Google News", "url": f"https://news.google.com/search?q={q}"},
            {"label": "Search official government sources", "url": f"https://www.google.com/search?q={q}+site%3Agov"}]


def get_report(report_id):
    with db() as con:
        row = con.execute("SELECT * FROM verifications WHERE id=?", (report_id,)).fetchone()
    if not row:
        abort(404)
    item = dict(row)
    item["evidence"] = json.loads(item["evidence"])
    item["created_display"] = datetime.fromisoformat(item["created_at"]).astimezone().strftime("%b %d, %Y · %I:%M %p")
    return item


@app.route("/")
def home():
    with db() as con:
        total = con.execute("SELECT COUNT(*) FROM verifications").fetchone()[0]
    return render_template("home.html", total=total)


@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "GET":
        return render_template("verify.html", active="verify")
    kind = request.form.get("kind", "text")
    if kind == "text":
        content = request.form.get("content", "").strip()
        if len(content) < 12:
            flash("Add a little more context so the claim can be reviewed.", "error")
            return redirect(url_for("verify"))
        if len(content) > 5000:
            flash("Text submissions must be 5,000 characters or fewer.", "error")
            return redirect(url_for("verify"))
        title = re.sub(r"\s+", " ", content)[:110]
        explanation = ("This prototype does not have a connected fact-checking or AI analysis service. "
                       "It has not verified the claim. Review the linked searches and compare dates, "
                       "original documents, and independent reporting before drawing a conclusion.")
        evidence = [{"type": "User submission", "detail": content[:1200]},
                    {"type": "Source search", "detail": "Search links are provided for research; results have not been fetched or evaluated."}]
        report_id = save_report(kind, title, "Unable to Verify", "Not assessed", explanation,
                                evidence + search_links(content))
    elif kind in ALLOWED:
        upload = request.files.get("file")
        if not upload or not upload.filename:
            flash("Choose a file to analyze.", "error")
            return redirect(url_for("verify"))
        original = secure_filename(upload.filename)
        suffix = Path(original).suffix.lower().lstrip(".")
        if suffix not in ALLOWED[kind]:
            flash(f"That file type is not supported for {kind}.", "error")
            return redirect(url_for("verify"))
        data = upload.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            flash("Files must be 25 MB or smaller.", "error")
            return redirect(url_for("verify"))
        if not data:
            flash("The selected file is empty. Choose another file.", "error")
            return redirect(url_for("verify"))
        # Keep only a randomly named private copy; never expose uploads as public URLs.
        stored = f"{uuid.uuid4().hex}.{suffix}"
        (UPLOAD_DIR / stored).write_bytes(data)
        title = original
        explanation = (f"The {kind} was received, but no forensic or AI detection service is connected. "
                       "No authenticity conclusion has been made. Metadata and visual/audio cues alone "
                       "cannot prove who created or altered a file.")
        evidence = [{"type": "File received", "detail": f"{original} · {len(data) / (1024 * 1024):.2f} MB"},
                    {"type": "Analysis status", "detail": "Automated media analysis is not configured in this prototype."}]
        report_id = save_report(kind, title, "Unable to Verify", "Not assessed", explanation, evidence, original)
    else:
        abort(400)
    return redirect(url_for("report", report_id=report_id))


@app.route("/report/<report_id>")
def report(report_id):
    return render_template("report.html", report=get_report(report_id))


@app.route("/history")
def history():
    with db() as con:
        rows = con.execute("SELECT id,kind,title,status,created_at FROM verifications ORDER BY created_at DESC LIMIT 100").fetchall()
    records = [dict(r) for r in rows]
    for item in records:
        item["created_display"] = datetime.fromisoformat(item["created_at"]).astimezone().strftime("%b %d, %Y · %I:%M %p")
    return render_template("history.html", records=records, active="history")


@app.route("/about")
def about():
    return render_template("about.html", active="about")


@app.errorhandler(413)
def too_large(_error):
    flash("Files must be 25 MB or smaller.", "error")
    return redirect(url_for("verify"))


init_db()

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
