from __future__ import annotations

from typing import Any, Dict, List


class SecurityScanner:
    """Basic static security scanner for source-like text."""

    risky_patterns = {
        "sql_injection": ["SELECT * FROM users WHERE name = '", "sql =", "query = f\"SELECT"],
        "hardcoded_secret": ["api_key", "secret_key", "token", "password", "private_key"],
        "command_injection": ["os.system(", "subprocess.call(", "shell=True"],
        "unsafe_eval": ["eval(", "exec("],
        "insecure_deserialization": ["pickle.loads", "yaml.load("]
    }

    def scan(self, code: str) -> Dict[str, Any]:
        findings: List[Dict[str, Any]] = []
        lowered = code.lower()

        for category, patterns in self.risky_patterns.items():
            for pattern in patterns:
                if pattern.lower() in lowered:
                    findings.append({
                        "category": category,
                        "severity": self._severity_for(category),
                        "pattern": pattern,
                        "message": self._message_for(category),
                    })

        return {
            "summary": {
                "total_findings": len(findings),
                "status": "ok" if not findings else "warning",
            },
            "findings": findings,
        }

    def _severity_for(self, category: str) -> str:
        mapping = {
            "sql_injection": "high",
            "hardcoded_secret": "high",
            "command_injection": "high",
            "unsafe_eval": "critical",
            "insecure_deserialization": "high",
        }
        return mapping.get(category, "medium")

    def _message_for(self, category: str) -> str:
        messages = {
            "sql_injection": "Possible SQL injection vector found.",
            "hardcoded_secret": "Sensitive secret or credential may be embedded in source code.",
            "command_injection": "Command execution may be vulnerable to injection.",
            "unsafe_eval": "Dynamic code execution may be unsafe.",
            "insecure_deserialization": "Untrusted deserialization may allow exploitation.",
        }
        return messages.get(category, "Potential security issue detected.")
