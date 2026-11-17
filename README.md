# CivicConnect AI

A Flask and SQLite prototype based on `spec.md`. It provides a responsive landing page, text and media submission flows, report pages, and a local verification history.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

## Prototype limits

This build does not connect to a fact-checking service, AI API, speech recognition, or forensic media analysis. Reports therefore say **Unable to Verify** and do not present synthetic confidence scores. Text reports provide search links for independent research. Uploaded files are stored under a randomly generated name in the local `uploads/` directory and are not served publicly. Remove local prototype data by deleting `civicconnect.db` and its associated uploads.
