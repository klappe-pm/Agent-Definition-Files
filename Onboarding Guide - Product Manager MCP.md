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

# Onboarding Guide - Product Manager MCP

## Environment Assumptions

- **Models**: Only Gemini models available (gemini-1.5-pro, gemini-1.5-flash)
- **Access**: Models accessed through corporate SSO authentication
- **Network**: Models hosted on internal corporate infrastructure

## Configuration Decisions Required for Translation

### 1. Model Selection Mapping

**Current Framework Configuration:**

```yaml
# config/llm.providers.yaml
providers:
  google:
    models:
      - name: gemini-1.5-pro-002
      - name: gemini-1.5-flash-002
```

**Corporate Translation Required:**
- Map to your internal Gemini endpoint URL
- Replace with corporate model names/versions
- Adjust context windows to corporate limits

### 2. Authentication Method

**Current Framework:**

```bash
GOOGLE_API_KEY=your_api_key
```

**Corporate Translation Required:**
- Replace with SSO token retrieval method
- Configure session management for token refresh
- Set corporate authentication endpoint

### 3. Product Manager Agent Configuration

**Current Framework Decisions in `/agents/product-agents/`:**

#### Core Agent Responsibilities

The framework defines these PM responsibilities that need corporate context:

- **Strategy Development** → Link to corporate strategy tools
- **Metrics Definition** → Map to corporate KPI systems
- **Requirements Writing** → Align with corporate templates
- **Dashboard Creation** → Connect to corporate BI tools
- **Stakeholder Communication** → Use corporate communication channels

#### Sub-Agent Task Allocation

Framework assumes these sub-agents - determine which apply:

- `product-manager-agent-strategist` → Corporate strategy processes?
- `product-manager-agent-metrics-analyst` → Corporate analytics tools?
- `product-manager-agent-dashboard-designer` → Corporate BI platform?
- `product-manager-agent-business-analyst` → Corporate BA standards?
- `product-manager-agent-requirements-writer` → Corporate PRD templates?

### 4. Tool Permissions

**Current Framework (`config/tools.yaml`):**

```yaml
tools:
  enable_all: true  # Open permissions
```

**Corporate Translation Required:**
- Define allowed internal tools only
- Set read/write permissions per tool
- Configure data access boundaries
- Set approved API endpoints

### 5. Memory and Context Storage

**Current Framework (`config/memory.yaml`):**

```yaml
memory:
  type: "memory"  # Ephemeral
```

**Corporate Translation Required:**
- Define approved storage location
- Set data retention policies
- Configure encryption requirements
- Define PII handling rules

### 6. Routing and Budget Controls

**Current Framework (`config/model.routing.yaml`):**

```yaml
routing:
  default: claude-3-5-sonnet  # Not available
```

**Corporate Translation Required:**

```yaml
routing:
  default: gemini-1.5-flash  # Cost-optimized
  tasks:
    strategy: gemini-1.5-pro  # Higher capability
    simple_queries: gemini-1.5-flash
```

### 7. Safety and Compliance

**Current Framework (`config/safety.yaml`):**

```yaml
safety:
  level: "standard"
```

**Corporate Requirements to Define:**
- Acceptable use policies
- Data classification levels
- Output review requirements
- Restricted topics/domains

### 8. Integration Points

**Framework Assumes These PM Tools (Not Configured):**
- Jira/Linear → Your issue tracker?
- Confluence/Notion → Your documentation?
- Slack/Teams → Your communication?
- Mixpanel/Amplitude → Your analytics?
- Figma/Miro → Your design tools?

**Corporate Decisions Required:**
- List approved PM tools
- Define integration methods (API/webhook/manual)
- Set data sync frequencies
- Configure access credentials

### 9. Workflow Orchestration

**Framework PM Workflows Needing Translation:**

1. **Feature Specification Flow**
   - Current: Agent generates spec → Output
   - Corporate: Agent → Review → Approval → System entry?

2. **Metrics Definition Flow**
   - Current: Agent defines metrics → Output
   - Corporate: Agent → Validation → BI tool entry?

3. **Requirements Gathering Flow**
   - Current: Agent writes requirements → Output
   - Corporate: Agent → Stakeholder review → JIRA creation?

### 10. Output Formatting

**Framework Outputs (Unstructured):**
- Markdown documents
- JSON definitions
- YAML configurations

**Corporate Requirements:**
- PRD template format?
- Metrics dashboard format?
- User story format?
- Acceptance criteria format?

## Required Corporate Configurations

### Step 1: Define Model Access

```yaml
# Corporate config needed
gemini:
  endpoint: "https://internal-gemini.company.com"
  auth_method: "oauth2"
  token_endpoint: "https://sso.company.com/token"
  scopes: ["gemini.generate", "gemini.embed"]
```

### Step 2: Map PM Processes

Create mapping document:

```yaml
pm_processes:
  feature_definition:
    template: "corporate_prd_template_v2"
    approval_chain: ["pm_lead", "eng_lead", "product_head"]
  metrics:
    system: "tableau"
    update_frequency: "daily"
  requirements:
    format: "jira_story"
    fields: ["acceptance_criteria", "business_value", "dependencies"]
```

### Step 3: Configure Data Boundaries

```yaml
data_access:
  allowed_sources:
    - "internal_wiki"
    - "product_database"
    - "metrics_warehouse"
  restricted:
    - "hr_systems"
    - "financial_systems"
  pii_handling: "redact"
```

## Onboarding Checklist

- [ ] Obtain Gemini model endpoint URL
- [ ] Configure SSO authentication for model access
- [ ] Map PM agent tasks to corporate processes
- [ ] Define approved data sources
- [ ] Set output format requirements
- [ ] Configure tool integrations
- [ ] Define approval workflows
- [ ] Set data retention policies
- [ ] Configure monitoring/logging destination
- [ ] Test in sandbox environment
