from __future__ import annotations

from typing import Any, Dict


class HealthService:
    def get_status(self) -> Dict[str, Any]:
        return {
            "service": "AI Security Suite",
            "status": "online",
            "modules": ["ai_agent", "security_scanner", "health"],
        }
