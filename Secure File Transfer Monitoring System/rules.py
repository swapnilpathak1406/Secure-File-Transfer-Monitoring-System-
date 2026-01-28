import re

ATTACK_RULES = {
    "SQL Injection": r"(\bUNION\b|\bSELECT\b|\bDROP\b|\bINSERT\b|--|')",
    "XSS": r"(<script>|</script>|onerror=|onload=)",
    "Command Injection": r"(;|\|\||&&|\bcat\b|\bwget\b|\bcurl\b)",
    "Directory Traversal": r"(\.\./|\.\.\\)",
    "LFI": r"(/etc/passwd|boot.ini)"
}

def detect_attack(payload):
    for attack, pattern in ATTACK_RULES.items():
        if re.search(pattern, payload, re.IGNORECASE):
            return attack
    return None
