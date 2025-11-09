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

# LLM Agents Framework

**🚀 Zero-Config LLM Agents Ready in 2 Minutes**

A comprehensive framework with 100+ pre-configured LLM agents for product development teams. Works out-of-the-box with any LLM provider (Claude, GPT, Gemini) - just add your API key and run!

## ✨ Key Features

- **🎯 100+ Pre-Built Agents**: Product, Engineering, Research, UX, Content, and more
- **⚡ Zero Configuration**: Sensible defaults for everything
- **🔧 Extensible**: All advanced features optional
- **🏢 Enterprise Ready**: Includes corporate & Google-specific deployment guides
- **📦 Multiple Formats**: JSON, YAML, TOML, XML, Markdown definitions

## 🚀 Quick Start (< 2 Minutes)

```bash
# 1. Clone repository
git clone https://github.com/klappe-pm/agents.git
cd agents

# 2. Set up environment
cp .env.example .env
# Add ONE API key to .env (Anthropic, OpenAI, or Google)

# 3. Run your first agent!
python cli/agent_run.py product-manager "Create a feature spec for dark mode"
```

That's it! No configuration needed. See [QUICKSTART.md](Quick%20Start%20Guide.md) for more examples.

## 📚 Documentation

### Getting Started

- **[QUICKSTART.md](Quick%20Start%20Guide.md)** - 2-minute setup guide
- **[.env.example](./.env.example)** - Environment variables template

### Enterprise Deployment

- **[CORPORATE_ONBOARDING.md](Onboarding%20Guide%20-%20Product%20Manager%20MCP.md)** - Corporate environment setup
- **[GOOGLE_INTERNAL_ONBOARDING.md](Google%20Internal%20Onboarding%20Guide%20-%20LLM%20Agents%20Framework.md)** - Google-specific implementation guide

## 🎯 Available Agents (100+)

### Primary Agents & Sub-Agents

| Agent Category | Primary Agent | Sub-Agents | Use Cases |
|----------------|---------------|------------|------------|
| **Product** | Product Manager | 14 specialized roles | PRDs, metrics, strategy, dashboards |
| **Engineering** | Engineering Agent | 11 specialized roles | Code review, architecture, DevOps |
| **Research** | Research Agent | 10 specialized roles | User research, data analysis, insights |
| **UX Design** | UX Design Agent | 9 specialized roles | Wireframes, prototypes, usability |
| **Content** | Content Strategist | 11 specialized roles | Writing, SEO, editorial, social |
| **Business** | Business Review | 11 specialized roles | Analytics, OKRs, financial analysis |
| **Cloud** | AWS/Azure/GCP | 30+ cloud roles | Infrastructure, deployment, costs |
| **Project** | Project Manager | 5 specialized roles | Planning, tracking, reporting |
| **Context** | Context Agent | 12 specialized roles | Memory, knowledge synthesis |
| **Apps Script** | Google Apps Script | 11 specialized roles | Automation, integration, testing |
| **PR** | Public Relations | 2 specialized roles | Press releases, communications |

## 🛠️ Configuration (All Optional!)

### Minimal Setup

```yaml
# Just add your API key - everything else has defaults!
ANTHROPIC_API_KEY=sk-...
# or
OPENAI_API_KEY=sk-...
# or
GOOGLE_API_KEY=...
```

### Available Configurations

All configuration files in `/config/` are **optional** with sensible defaults:

| Config File | Purpose | Required? |
|-------------|---------|----------|
| `llm.providers.yaml` | LLM endpoints and models | No (defaults included) |
| `model.routing.yaml` | Task routing and budgets | No (uses default model) |
| `agent.runtime.yaml` | Execution settings | No (10 iterations, 5min timeout) |
| `memory.yaml` | Storage and RAG | No (in-memory default) |
| `tools.yaml` | Tool permissions | No (all tools enabled) |
| `safety.yaml` | Content filtering | No (standard safety) |
| `logging.yaml` | Monitoring | No (console logging) |
| `reliability.yaml` | Retries and limits | No (2 retries default) |

## 📁 Repository Structure

```javascript
agents/
├── config/                 # Optional configuration files
│   ├── *.yaml             # Config files (all optional)
│   └── schemas/           # JSON schemas for validation
├── agents/                # 100+ agent definitions
│   ├── [agent-type]/      # Organized by function
│   │   ├── json/          # JSON format
│   │   ├── yaml/          # YAML format
│   │   ├── toml/          # TOML format
│   │   ├── xml/           # XML format
│   │   └── md/            # Markdown docs
├── product-manager-mcp/   # Product Manager MCP resources
├── ignore/                # Development/experimental files
└── *.md                   # Documentation

```

## 📚 How to Use This Framework

### 1. Choose Your Agent

```bash
# List all available agents
python cli/agent_run.py --list-agents
```

### 2. Run Agent Tasks

```python
# Python API
from agents_runtime import run_agent
result = run_agent("product-manager", "Write a PRD for mobile app")

# CLI
python cli/agent_run.py engineering "Review code for security issues"
```

### 3. Customize (Optional)

- Edit agent definitions in `/agents/[type]/`
- Modify configurations in `/config/`
- Add new tools or integrations

## 🏭️ Architecture Overview

### 4-Layer Hierarchy

1. **Orchestration Layer**: Coordinates multiple agents
2. **Primary Agent Layer**: 11 domain-specific agents
3. **Sub-Agent Layer**: 90+ specialized task agents
4. **Foundation Layer**: Configuration, memory, tools

### Key Design Principles

- **Zero Required Config**: Works immediately with defaults
- **Progressive Enhancement**: Add features as needed
- **Format Flexibility**: JSON, YAML, TOML, XML, Markdown
- **Provider Agnostic**: Works with any LLM provider

## 🔗 Integrations

### Supported LLM Providers

- ✅ Anthropic Claude (All models)
- ✅ OpenAI GPT (GPT-4, GPT-4o, etc.)
- ✅ Google Gemini (1.5 Pro, Flash)
- ✅ Local models (Ollama)

### Tool Integrations (Configurable)

- Issue Tracking (Jira, GitHub Issues, Linear)
- Documentation (Confluence, Notion, Google Docs)
- Communication (Slack, Teams, Discord)
- Analytics (Mixpanel, Amplitude, BigQuery)
- Version Control (GitHub, GitLab, Bitbucket)

## 🔒 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/klappe-pm/agents/issues)
- **Discussions**: [GitHub Discussions](https://github.com/klappe-pm/agents/discussions)
- **Email**: kevin@averageintelligence.ai

## 🙏 Acknowledgments

- Anthropic Claude for LLM capabilities
- OpenAI for GPT models
- Google for Gemini models
- Open source community for feedback and contributions

---

**🔄 Status**: Actively Maintained
**📅 Last Updated**: 2025-09-03
**🎯 Version**: 1.0.0
