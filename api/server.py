# api/server.py — FastAPI web server for CodeSense

from fastapi import FastAPI
from pydantic import BaseModel
from cli.scanner import scan_file
from storage.database import init_db, save_run, get_history

app = FastAPI(title="CodeSense API", version="0.1.0")
init_db()

class AnalyzeRequest(BaseModel):
    file_path: str

@app.get("/")
def root():
    return {"message": "CodeSense API is running"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    reports = scan_file(request.file_path)
    warnings = sum(1 for r in reports if r.health_label() != "good")
    save_run(request.file_path, len(reports), warnings)
    return {
        "file": request.file_path,
        "total": len(reports),
        "results": [
            {"name": r.name, "score": r.complexity, "health": r.health_label()}
            for r in reports
        ]
    }

@app.get("/history")
def history():
    runs = get_history()
    return [
        {"id": r.id, "file": r.file_path,
         "date": str(r.run_date), "total": r.total, "warnings": r.warnings}
        for r in runs
    ]