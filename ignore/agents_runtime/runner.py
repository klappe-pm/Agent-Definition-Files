"""
Simple runner for executing agents - minimal configuration required
"""

import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

from .agent import Agent
from .config import load_config


def setup_logging(config: Dict[str, Any]) -> None:
    """Setup basic logging based on config"""
    log_config = config.get("logging", {})
    level = getattr(logging, log_config.get("level", "INFO"))
    
    format_style = log_config.get("format", "simple")
    if format_style == "simple":
        format_str = "%(levelname)s: %(message)s"
    elif format_style == "detailed":
        format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    else:  # json
        format_str = '{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
    
    logging.basicConfig(level=level, format=format_str)


def load_agent_definition(agent_name: str) -> Dict[str, Any]:
    """Load agent definition from JSON/YAML files"""
    agents_dir = Path(__file__).parent.parent.parent / "agents"
    
    # Search for agent definition
    for agent_type_dir in agents_dir.iterdir():
        if not agent_type_dir.is_dir():
            continue
            
        # Check JSON files
        json_dir = agent_type_dir / "json"
        if json_dir.exists():
            for json_file in json_dir.glob("*-definition.json"):
                if agent_name in json_file.stem:
                    with open(json_file) as f:
                        return json.load(f)
    
    # Return minimal default if not found
    return {
        "name": agent_name,
        "role": agent_name.replace("-", " ").title(),
        "description": f"Agent: {agent_name}"
    }


def run_agent(
    agent_name: str,
    task: str,
    context: Optional[str] = None,
    config_override: Optional[Dict[str, Any]] = None
) -> str:
    """
    Run an agent with a task - minimal configuration required
    
    Args:
        agent_name: Name or type of agent
        task: Task to execute
        context: Optional context
        config_override: Optional config overrides
    
    Returns:
        Agent's response
    """
    # Load configuration
    config = load_config()
    if config_override:
        config.update(config_override)
    
    # Setup logging
    setup_logging(config)
    logger = logging.getLogger(__name__)
    
    # Load agent definition
    agent_def = load_agent_definition(agent_name)
    
    # Create agent
    agent = Agent(
        name=agent_def.get("name", agent_name),
        role=agent_def.get("role", "Assistant"),
        description=agent_def.get("description", ""),
        model=agent_def.get("model") or config.get("routing", {}).get("default"),
        params=agent_def.get("parameters", {})
    )
    
    logger.info(f"Running agent: {agent.name}")
    logger.debug(f"Task: {task}")
    
    # Execute task
    result = agent.act(task, context)
    
    logger.info("Task completed")
    return result


def run(agent_name: str = None, task: str = None) -> None:
    """CLI entry point for agent-run command"""
    import sys
    
    if not agent_name:
        agent_name = sys.argv[1] if len(sys.argv) > 1 else None
    if not task:
        task = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not agent_name or not task:
        print("Usage: agent-run <agent_name> <task>")
        sys.exit(1)
    
    result = run_agent(agent_name, task)
    print(result)
