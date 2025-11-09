from dataclasses import dataclass, field
from typing import Any, Dict, Optional

@dataclass
class Agent:
    name: str
    role: str
    description: str = ""
    model: Optional[str] = None
    params: Dict[str, Any] = field(default_factory=dict)

    def act(self, task: str, context: Optional[str] = None) -> str:
        # Minimal stub: just echoes intent. Hook up to LLM client later.
        return f"[{self.name} ({self.role})] Task: {task}\nContext: {context or 'N/A'}\nModel: {self.model or 'default'}"

