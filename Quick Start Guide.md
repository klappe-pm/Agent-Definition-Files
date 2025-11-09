---
categories: LLM
subCategories: Agents
topics:
subTopics:
dateCreated: 2025-09-02
dateRevised: 2025-09-02
aliases: []
tags: []
---

# Quick Start Guide

Get up and running in under 2 minutes with minimal configuration!

## Installation

### Option 1: Direct Usage (No Installation)

```bash
# Clone the repository
git clone https://github.com/klappe-pm/agents.git
cd agents

# Copy environment template
cp .env.example .env

# Add ONE API key to .env (choose your provider):
# - ANTHROPIC_API_KEY=your_key_here
# - OPENAI_API_KEY=your_key_here  
# - GOOGLE_API_KEY=your_key_here
```

### Option 2: Install as Package

```bash
# Install with minimal dependencies
pip install -e .

# Or install with your preferred LLM provider:
pip install -e ".[anthropic]"  # For Claude
pip install -e ".[openai]"     # For GPT
pip install -e ".[google]"     # For Gemini
```

## Running Your First Agent

```bash
# Run an agent with a task (no configuration needed!)
python cli/agent_run.py product-manager "Create a feature spec for dark mode"

# Or if installed as package:
agent-run engineering "Review this code for security issues"
```

## Common Commands

```bash
# List available agents
python cli/agent_run.py --list-agents

# Use a specific model
python cli/agent_run.py product-manager "Task" --model gpt-4o

# Verbose output
python cli/agent_run.py engineering "Task" -v
```

## Optional: Custom Configuration

All configuration is optional! But if you want to customize:

1. **Model Selection**: Edit `config/model.routing.yaml`
2. **Runtime Settings**: Edit `config/agent.runtime.yaml`
3. **Safety/Tools**: Edit respective files in `config/`

All config files have sensible defaults and everything is optional.

## Python API Usage

```python
from agents_runtime import run_agent

# Minimal usage - just agent name and task
result = run_agent("product-manager", "Create a roadmap")
print(result)

# With context
result = run_agent(
    "engineering",
    "Optimize this function",
    context="def slow_function(): pass"
)
```

## Available Agents

- `product-manager` - Product strategy and requirements
- `engineering` - Software development tasks
- `research` - Market and user research
- `ux-design` - User experience design
- `content` - Content creation and strategy
- `business-review` - Analytics and reporting
- `project` - Project management
- And more! Run `--list-agents` to see all
