from __future__ import annotations

from typing import Any, Dict


class RiskReporter:
    """Formats vulnerability summaries into a readable structure."""

    def build_report(self, findings: list[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "total_findings": len(findings),
            "severities": {
                "critical": sum(1 for item in findings if item.get("severity") == "critical"),
                "high": sum(1 for item in findings if item.get("severity") == "high"),
                "medium": sum(1 for item in findings if item.get("severity") == "medium"),
            },
            "items": findings,
        }
