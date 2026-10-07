from __future__ import annotations

from typing import Any, Dict, List


class Planner:
    """Simple planning service for AI-driven actions."""

    def plan(self, goal: str) -> Dict[str, Any]:
        return {
            "goal": goal,
            "steps": [
                "Understand the task and constraints",
                "Draft the implementation plan",
                "Generate or improve the code",
                "Run a security sanity check",
                "Provide a summary and next actions",
            ],
            "status": "ready",
        }
