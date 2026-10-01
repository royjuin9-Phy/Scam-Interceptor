# config.py

SUSPICIOUS_DOMAINS = [
    "free-stock-tips.in", 
    "guaranteed-crypto-profit.com",
    "sebi-approved-vip.net", 
    "wealth-double-fast.xyz"
]

HIGH_RISK_TERMS = [
    r"guaranteed\s+(return|profit)",
    r"100%\s+daily",
    r"double\s+your\s+money",
    r"zero\s+risk",
    r"vip\s+(group|calls|signals)",
    r"inside\s+leak"
]