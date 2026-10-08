from __future__ import annotations

import re
from typing import Any, Dict, List


class SecurityScanner:
    """Static, heuristic scanner for common application security issues."""

    patterns = {
        "sql_injection": [
            r"execute\s*\(\s*f?['\"]\s*SELECT",
            r"SELECT\s+.*\s+FROM\s+.*\s+WHERE\s+.*\+",
            r"cursor\.execute\s*\(\s*query",
        ],
        "hardcoded_secret": [
            r"(api[_-]?key|secret[_-]?key|token|password|private[_-]?key)\s*[:=]\s*['\"][^'\"]+['\"]",
            r"aws_access_key_id|aws_secret_access_key",
        ],
        "command_injection": [
            r"os\.system\s*\(",
            r"subprocess\.(call|run|Popen)\s*\(.*shell\s*=\s*True",
            r"shell=True",
        ],
        "unsafe_eval": [
            r"eval\s*\(",
            r"exec\s*\(",
        ],
        "insecure_deserialization": [
            r"pickle\.loads\s*\(",
            r"yaml\.load\s*\(",
        ],
        "xss": [
            r"innerHTML\s*=|document\.write\s*\(",
            r"<script>|javascript:",
        ],
    }

    severity_map = {
        "sql_injection": "high",
        "hardcoded_secret": "high",
        "command_injection": "high",
        "unsafe_eval": "critical",
        "insecure_deserialization": "high",
        "xss": "medium",
    }

    messages = {
        "sql_injection": "Possible SQL injection risk detected.",
        "hardcoded_secret": "A secret or credential appears to be hardcoded.",
        "command_injection": "Command execution may be vulnerable to user-controlled input.",
        "unsafe_eval": "Dynamic code execution may permit arbitrary code execution.",
        "insecure_deserialization": "Untrusted deserialization may lead to code execution.",
        "xss": "Potential cross-site scripting issue found.",
    }

    def scan(self, code: str, filename: str = "") -> Dict[str, Any]:
        findings: List[Dict[str, Any]] = []
        lines = code.splitlines()

        for category, patterns in self.patterns.items():
            for pattern in patterns:
                for idx, line in enumerate(lines, start=1):
                    if re.search(pattern, line, re.IGNORECASE):
                        findings.append({
                            "category": category,
                            "severity": self.severity_map.get(category, "medium"),
                            "pattern": pattern,
                            "message": self.messages.get(category, "Potential issue detected."),
                            "line": idx,
                            "file": filename,
                        })
                        break

        risk_score = min(100, len(findings) * 18)
        if risk_score >= 80:
            risk_level = "critical"
        elif risk_score >= 50:
            risk_level = "high"
        elif risk_score >= 20:
            risk_level = "medium"
        else:
            risk_level = "low"

        return {
            "summary": {
                "total_findings": len(findings),
                "risk_score": risk_score,
                "risk_level": risk_level,
                "status": "warning" if findings else "ok",
            },
            "findings": findings,
        }
