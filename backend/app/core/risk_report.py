from __future__ import annotations

from typing import Any, Dict, List


class RiskReporter:
    """Formats security findings into a readable report."""

    def build_report(self, findings: List[Dict[str, Any]]) -> Dict[str, Any]:
        severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        for item in findings:
            severity = item.get("severity", "low")
            severity_counts[severity] = severity_counts.get(severity, 0) + 1

        return {
            "total_findings": len(findings),
            "by_severity": severity_counts,
            "items": findings,
        }
