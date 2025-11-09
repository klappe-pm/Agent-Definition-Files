#!/usr/bin/env python3
"""
Minimal CLI runner for agents - Quick start with zero configuration required
Usage: python agent_run.py [agent_name] [task]
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from agents_runtime import Agent, load_config


def main():
    parser = argparse.ArgumentParser(
        description="Run an agent with minimal configuration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python agent_run.py product-manager "Create a feature spec"
  python agent_run.py engineering "Review this code"
  python agent_run.py --list-agents
        """
    )
    
    parser.add_argument("agent", nargs="?", help="Agent name or type")
    parser.add_argument("task", nargs="?", help="Task to execute")
    parser.add_argument("--list-agents", action="store_true", help="List available agents")
    parser.add_argument("--config", help="Override config file")
    parser.add_argument("--model", help="Override default model")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    # Load config (all optional)
    config = load_config()
    
    if args.list_agents:
        print("Available agents:")
        agents_dir = Path(__file__).parent.parent / "agents"
        for agent_type_dir in agents_dir.iterdir():
            if agent_type_dir.is_dir() and not agent_type_dir.name.startswith("."):
                print(f"  - {agent_type_dir.name}")
        return
    
    if not args.agent:
        parser.print_help()
        return
    
    if not args.task:
        print(f"Error: Please provide a task for {args.agent}")
        return
    
    # Create and run agent with minimal config
    agent = Agent(
        name=args.agent,
        role=args.agent.replace("-", " ").title(),
        model=args.model or config.get("routing", {}).get("default"),
    )
    
    if args.verbose:
        print(f"Running {agent.name} with task: {args.task}")
        print(f"Config: {json.dumps(config, indent=2)}")
    
    result = agent.act(args.task)
    print(result)


if __name__ == "__main__":
    main()
