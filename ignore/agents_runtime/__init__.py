"""
Agents Runtime - Minimal framework for LLM agents
Quick start: Just set your API key and run!
"""

__version__ = "0.1.0"

from .agent import Agent
from .config import load_config
from .runner import run_agent

__all__ = ["Agent", "load_config", "run_agent"]
