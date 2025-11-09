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

# Google Internal Onboarding Guide - LLM Agents Framework

*Disclaimer: This guide represents one approach to implementing this open-source framework within Google's infrastructure. These are suggestions and guidance based on common patterns, not mandated requirements. Teams should adapt based on their specific needs and org requirements.*

## Project Overview

### What This Is

The LLM Agents Framework is an open-source collection of 100+ agent definitions designed for product development teams. It provides pre-configured agent personalities, task allocations, and workflow patterns that can be powered by Gemini models.

### What This Is Not

- Not a production-ready service
- Not a Google-maintained project
- Not integrated with Google's internal tools by default
- Not compliance-certified for sensitive data

## Project Hierarchy

```javascript
┌─────────────────────────────────────┐
│     Orchestration Layer             │
│  (Product Team Orchestrator Agent)  │
└─────────────┬───────────────────────┘
              │
┌─────────────┴───────────────────────┐
│       Primary Agent Layer           │
│   (11 Domain-Specific Agents)       │
├─────────────────────────────────────┤
│ • Product Manager Agent             │
│ • Engineering Agent                 │
│ • Research Agent                    │
│ • UX Design Agent                   │
│ • Content Strategy Agent            │
│ • Business Review Agent             │
│ • Cloud Platform Agents (GCP focus) │
│ • Project Management Agent          │
│ • Context Management Agent          │
│ • Google Apps Script Agent          │
│ • Public Relations Agent            │
└─────────────┬───────────────────────┘
              │
┌─────────────┴───────────────────────┐
│        Sub-Agent Layer              │
│     (90+ Specialized Agents)        │
├─────────────────────────────────────┤
│ Each primary agent has 5-15         │
│ specialized sub-agents for          │
│ specific tasks                      │
└─────────────────────────────────────┘
              │
┌─────────────┴───────────────────────┐
│      Foundation Layer               │
│   (Configuration & Runtime)         │
├─────────────────────────────────────┤
│ • Gemini Model Integration          │
│ • Memory/Context Management         │
│ • Tool Permissions                  │
│ • Safety Controls                   │
└─────────────────────────────────────┘
```

## Core Capabilities

### 1. Product Development Automation

- **Requirements Generation**: PRDs, user stories, acceptance criteria
- **Metrics Definition**: KPIs, success metrics, dashboard specs
- **Strategy Documentation**: Roadmaps, vision docs, competitive analysis
- **Stakeholder Communication**: Updates, reports, presentations

### 2. Engineering Support

- **Code Review Assistance**: Best practices, security checks, performance
- **Documentation**: Technical specs, API docs, runbooks
- **Architecture Planning**: System design, data flow, integration patterns
- **DevOps Automation**: CI/CD configs, monitoring setup, deployment scripts

### 3. Research & Analytics

- **User Research**: Interview guides, survey design, persona development
- **Data Analysis**: Metrics interpretation, trend analysis, reporting
- **Competitive Intelligence**: Feature comparisons, market analysis
- **A/B Test Design**: Hypothesis formation, success criteria, analysis plans

### 4. Design & Content

- **UX Workflows**: Wireframes, user flows, interaction patterns
- **Content Strategy**: Editorial calendars, SEO optimization, style guides
- **Documentation**: Help docs, FAQs, training materials

## Onboarding Categories

### Category A: Infrastructure Setup

**For: SREs, Platform Engineers**

#### Required Adaptations

- [ ] Map Gemini endpoints to internal URLs
- [ ] Configure Vertex AI authentication
- [ ] Set up Cloud IAM permissions
- [ ] Enable required GCP APIs
- [ ] Configure VPC/network access

#### Google-Specific Configs

```yaml
# config/llm.providers.yaml
providers:
  google_internal:
    endpoint: "https://gemini-api.googleprod.com/v1"  # Example
    auth_method: "application_default_credentials"
    project_id: "${GCP_PROJECT_ID}"
    location: "us-central1"
    models:
      - name: "gemini-1.5-pro"
        endpoint_suffix: "/models/gemini-pro:generateContent"
      - name: "gemini-1.5-flash" 
        endpoint_suffix: "/models/gemini-flash:generateContent"
```

### Category B: Security & Compliance

**For: Security, Legal, Privacy Teams**

#### Required Adaptations

- [ ] Implement data classification tags
- [ ] Configure Cloud DLP for PII detection
- [ ] Set up audit logging to Cloud Logging
- [ ] Enable VPC Service Controls
- [ ] Configure Access Transparency

#### Google-Specific Controls

```yaml
# config/safety.yaml
safety:
  dlp_inspection:
    enabled: true
    info_types: ["PERSON_NAME", "EMAIL_ADDRESS", "GCP_CREDENTIALS"]
  data_residency: "us"
  encryption:
    cmek_key: "projects/${PROJECT}/locations/${LOCATION}/keyRings/${KEYRING}/cryptoKeys/${KEY}"
```

### Category C: Tool Integration

**For: Product Managers, Engineers**

#### Required Adaptations

- [ ] Connect to Buganizer for issue tracking
- [ ] Integrate with g3doc for documentation
- [ ] Link to OKR system
- [ ] Connect to go/launches for launch tracking
- [ ] Integrate with Critique for code review

#### Google Tool Mappings

```yaml
# config/tools.yaml
integrations:
  issue_tracking:
    system: "buganizer"
    endpoint: "buganizer.corp.google.com/api"
  documentation:
    system: "g3doc"
    path: "//depot/google3/docs/"
  code_review:
    system: "critique"
    endpoint: "critique-api.googleprod.com"
  analytics:
    system: "plx"
    dashboards: "go/team-dashboards"
  communication:
    system: "chat"
    spaces: ["product-team", "eng-team"]
```

### Category D: Workflow Adaptation

**For: Product Teams, TPMs**

#### Required Adaptations

- [ ] Map to Google's PRD template (go/prd-template)
- [ ] Align with RAPID decision framework
- [ ] Configure for Google's launch process
- [ ] Set up dogfood/trusted tester workflows
- [ ] Implement privacy review triggers

#### Workflow Configurations

```yaml
# config/workflows.yaml
google_processes:
  product_development:
    phases: ["ideation", "prr", "design", "eng_review", "launch_review"]
    templates:
      prd: "go/prd-template"
      design_doc: "go/design-doc-template"
    reviews:
      privacy: "go/privacy-review"
      security: "go/security-review"
      legal: "go/legal-review"
  launch:
    tracks: ["dogfood", "trusted_tester", "beta", "ga"]
    approvals: ["product_lead", "eng_lead", "privacy", "legal"]
```

### Category E: Data & Analytics

**For: Data Scientists, Analysts**

#### Required Adaptations

- [ ] Connect to BigQuery datasets
- [ ] Configure Dataflow pipelines
- [ ] Set up PLX dashboards
- [ ] Link to experiment platform (Mendel/Cider)
- [ ] Configure data retention per policy

#### Data Configurations

```yaml
# config/data.yaml
data_sources:
  bigquery:
    project: "${BQ_PROJECT}"
    datasets:
      - "product_metrics"
      - "user_behavior"
      - "experiment_results"
  pubsub:
    topics:
      - "agent-requests"
      - "agent-responses"
  storage:
    bucket: "gs://${PROJECT}-agent-storage"
    retention_days: 90
```

## Recommended Team Structure

### Core Team

- **Tech Lead**: Architecture, technical decisions
- **Product Manager**: Use case definition, prioritization
- **2-3 Engineers**: Implementation, integration
- **UX Designer**: Interface design (if UI needed)
- **TPM**: Cross-functional coordination

### Extended Team

- **Security Champion**: Security reviews
- **Privacy Champion**: Privacy compliance
- **SRE**: Production readiness
- **Data Analyst**: Usage analytics

---

## Important Note

**This guide is an opinion piece and represents one possible approach to implementing this framework at Google. It is not official Google documentation, policy, or mandate. Teams should:**

1. Consult with their own Tech Leads and Managers
2. Follow their org's specific guidelines
3. Adhere to actual Google policies (not this guide)
4. Adapt based on their specific use cases
5. Conduct proper reviews (privacy, security, legal)

**This framework is open-source and not Google-maintained. Use at your own discretion and risk. Always follow official Google policies and procedures for production systems.**
