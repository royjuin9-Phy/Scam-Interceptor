# models.py
from pydantic import BaseModel
from typing import List, Optional

class ScanRequest(BaseModel):
    content: str
    language: Optional[str] = "en"

class ScanResponse(BaseModel):
    risk_score: int
    risk_level: str
    detected_flags: List[str]
    advice_summary: str