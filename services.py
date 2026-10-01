# services.py
import re
from typing import List, Tuple
from config import SUSPICIOUS_DOMAINS, HIGH_RISK_TERMS

def compute_rule_score(text: str) -> Tuple[int, List[str]]:
    flags = []
    score = 0
    text_lower = text.lower()

    # Rule 1: High-risk deceptive phrases
    for pattern in HIGH_RISK_TERMS:
        if re.search(pattern, text_lower):
            flags.append(f"Unrealistic Promise Detected: '{pattern}'")
            score += 35

    # Rule 2: Suspicious Links
    urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text_lower)
    for url in urls:
        for bad_domain in SUSPICIOUS_DOMAINS:
            if bad_domain in url:
                flags.append(f"Known Malicious URL: {bad_domain}")
                score += 45

    # Rule 3: Unsolicited Payment Request (UPI Handles)
    upi_pattern = r'[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}'
    if re.search(upi_pattern, text):
        flags.append("Direct payment/deposit request found")
        score += 20

    return min(score, 90), flags