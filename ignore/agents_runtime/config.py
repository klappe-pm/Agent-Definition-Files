import os
from pathlib import Path
from typing import Any, Dict

import yaml
from dotenv import load_dotenv

CONFIG_DIR = Path(__file__).resolve().parents[2] / "config"

DEFAULT_FILES = [
    CONFIG_DIR / "llm.providers.yaml",
    CONFIG_DIR / "model.routing.yaml",
    CONFIG_DIR / "agent.runtime.yaml",
    CONFIG_DIR / "memory.yaml",
    CONFIG_DIR / "tools.yaml",
    CONFIG_DIR / "safety.yaml",
    CONFIG_DIR / "logging.yaml",
    CONFIG_DIR / "reliability.yaml",
]


def _read_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_config(env: str | None = None) -> Dict[str, Any]:
    """Load minimal configuration with sensible defaults.

    - Loads .env if present
    - Loads YAML config files if present; otherwise returns empty sections
    - Merges into a single config dict
    """
    load_dotenv()  # optional, only if .env exists

    cfg: Dict[str, Any] = {}
    for path in DEFAULT_FILES:
        section = _read_yaml(path)
        # shallow merge; later files can override earlier ones
        cfg.update(section)

    # Environment overrides
    if env is None:
        env = os.getenv("ENVIRONMENT", "development")
    cfg["environment"] = env

    # Default provider/model from env if provided
    default_model = os.getenv("DEFAULT_MODEL")
    if default_model:
        cfg.setdefault("routing", {})["default"] = default_model

    return cfg

