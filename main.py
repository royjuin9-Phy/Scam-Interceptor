# main.py
from fastapi import FastAPI, HTTPException
from models import ScanRequest, ScanResponse
from services import compute_rule_score

app = FastAPI(title="Scam Interceptor API", version="1.0.0")

@app.post("/api/v1/scan", response_model=ScanResponse)
async def scan_message(payload: ScanRequest):
    if not payload.content.strip():
        raise HTTPException(status_code=400, detail="Content cannot be empty.")

    base_score, flags = compute_rule_score(payload.content)
    
    if base_score >= 60:
        level = "HIGH RISK (SCAM)"
        summary = "Contains strong indicators of financial fraud. SEBI-registered entities never guarantee fixed returns."
    elif base_score >= 30:
        level = "CAUTION"
        summary = "Exhibits speculative or pressure tactics. Verify credentials before acting."
    else:
        level = "SAFE / LOW RISK"
        summary = "No immediate scam signatures detected. Always verify sources independently."

    return ScanResponse(
        risk_score=base_score,
        risk_level=level,
        detected_flags=flags,
        advice_summary=summary
    )

# Run this file with: uvicorn main:app --reload
