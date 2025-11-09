---
categories: LLM  
subCategories:
  - automation
  - cli
  - gemini
topics:
  - Gemini CLI
  - Product Management
  - Workflow Automation
subTopics:
dateCreated: 2025-09-02  
dateRevised: 2025-09-02
aliases: [Gemini CLI Guide, Gemini PM Automation]
tags: [automation, cli, gemini, workflows]
---

# Gemini CLI Implementation Guide for Product Managers

## Executive Summary

This guide provides comprehensive instructions for implementing and using the Gemini CLI for Product Manager automation. It covers installation, configuration, command structure, and practical workflows optimized for Gemini's capabilities.

## Installation and Setup

### Prerequisites

```bash
# System requirements
- Python 3.9+
- Node.js 16+
- Google Cloud SDK
- 8GB RAM minimum
- 10GB disk space

# Required permissions
- Google Cloud Project access
- Gemini API enabled
- Google Workspace API access (optional)
```

### Installation Steps

```bash
# Step 1: Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init

# Step 2: Install Gemini CLI
pip install gemini-cli-pm
# or
npm install -g @google/gemini-pm-cli

# Step 3: Authenticate
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID

# Step 4: Install PM-specific extensions
gemini-cli install-extension pm-toolkit
gemini-cli install-extension workspace-integration
gemini-cli install-extension analytics-suite
```

### Configuration

```bash
# Create configuration directory
mkdir -p ~/.gemini-pm
cd ~/.gemini-pm

# Generate default configuration
gemini-cli init --profile pm

# Edit configuration
cat > config.yaml << EOF
version: 1.0
profiles:
  default:
    model: gemini-2.0-pro
    temperature: 0.7
    max_tokens: 8192
    
  pm:
    models:
      prd: gemini-2.0-pro
      status: gemini-2.0-flash
      analysis: gemini-2.0-pro
      visual: gemini-2.0-pro-vision
    
    integrations:
      google_workspace: true
      jira: true
      github: true
      slack: true
    
    cache:
      enabled: true
      ttl: 3600
      max_size: 1GB
    
    output:
      format: markdown
      save_to_drive: true
      auto_share: false
EOF

# Set environment variables
export GEMINI_API_KEY="your-api-key"
export GEMINI_PROFILE="pm"
export GEMINI_WORKSPACE="/path/to/pm/workspace"
```

## CLI Command Structure

### Core Commands

```bash
# Basic syntax
gemini [global-options] <command> [command-options] [arguments]

# Global options
--profile, -p     : Use specific profile (default: pm)
--model, -m       : Override default model
--verbose, -v     : Verbose output
--output, -o      : Output format (json|markdown|html)
--save, -s        : Save output to file

# Main commands
gemini help          : Show help
gemini init          : Initialize workspace
gemini config        : Manage configuration
gemini generate      : Generate PM artifacts
gemini analyze       : Analyze data/metrics
gemini integrate     : Manage integrations
gemini workflow      : Run automated workflows
```

### PM-Specific Commands

```bash
# PRD Generation
gemini generate prd [options]
  --input, -i       : Input requirements file
  --template, -t    : PRD template (standard|lean|technical)
  --context, -c     : Additional context file
  --sections        : Specific sections to include
  --output-format   : Format (md|docx|pdf)

# Example
gemini generate prd \
  --input requirements.md \
  --template standard \
  --context user-research.json \
  --sections "problem,stories,metrics,timeline" \
  --output-format md > auth-feature-prd.md

# Status Updates
gemini generate status [options]
  --period, -p      : Period (daily|weekly|monthly)
  --sources         : Data sources to include
  --audience        : Target audience (exec|team|stakeholder)
  --format          : Output format

# Example
gemini generate status \
  --period weekly \
  --sources "jira,github,analytics" \
  --audience exec \
  --format bullet-points

# Metrics Analysis
gemini analyze metrics [options]
  --data, -d        : Data file or source
  --type            : Analysis type (trends|cohort|funnel)
  --period          : Time period
  --visualize       : Generate charts

# Example
gemini analyze metrics \
  --data analytics-export.csv \
  --type trends \
  --period last-30-days \
  --visualize true
```

## Workflow Automation

### 1. Daily PM Workflow

```bash
#!/bin/bash
# daily-pm-workflow.sh

echo "Starting Daily PM Workflow..."

# 1. Fetch updates from all sources
gemini integrate fetch \
  --sources "jira,github,slack,calendar" \
  --since yesterday \
  --save-to daily-updates.json

# 2. Generate morning status
gemini generate status \
  --period daily \
  --input daily-updates.json \
  --audience team \
  --output morning-status.md

# 3. Analyze overnight metrics
gemini analyze metrics \
  --data analytics-api \
  --type anomaly-detection \
  --period last-24-hours \
  --alert-threshold 2-sigma

# 4. Update task priorities
gemini workflow prioritize \
  --backlog jira-backlog.json \
  --method rice \
  --constraints "sprint-capacity:40" \
  --output prioritized-backlog.md

# 5. Prepare for standup
gemini generate standup \
  --format three-questions \
  --include-blockers true \
  --time-box 2-minutes

# 6. Share updates
gemini integrate share \
  --content morning-status.md \
  --channels "slack:#product,email:stakeholders" \
  --schedule "9:00 AM"

echo "Daily workflow completed!"
```

### 2. Sprint Planning Automation

```bash
#!/bin/bash
# sprint-planning.sh

# Configuration
SPRINT_NUMBER=$1
TEAM_VELOCITY=40

echo "Preparing Sprint $SPRINT_NUMBER Planning..."

# 1. Analyze previous sprint
gemini analyze sprint \
  --sprint-id "SPRINT-$((SPRINT_NUMBER-1))" \
  --metrics "velocity,completion,quality" \
  --output previous-sprint-analysis.md

# 2. Generate capacity planning
gemini calculate capacity \
  --team-size 5 \
  --sprint-days 10 \
  --holidays "check-calendar" \
  --buffer 20% \
  --output capacity.json

# 3. Prioritize backlog items
gemini workflow prioritize-sprint \
  --backlog product-backlog.json \
  --capacity capacity.json \
  --dependencies true \
  --technical-debt 20% \
  --output sprint-candidates.json

# 4. Generate sprint goals
gemini generate sprint-goals \
  --candidates sprint-candidates.json \
  --okrs company-okrs.json \
  --format smart-goals \
  --max-goals 3

# 5. Create sprint documentation
gemini generate sprint-plan \
  --sprint $SPRINT_NUMBER \
  --items sprint-candidates.json \
  --goals sprint-goals.md \
  --risks identify \
  --output "sprint-$SPRINT_NUMBER-plan.md"

# 6. Prepare presentation
gemini generate presentation \
  --input "sprint-$SPRINT_NUMBER-plan.md" \
  --template sprint-planning \
  --slides 10 \
  --output "sprint-$SPRINT_NUMBER.pptx"

echo "Sprint planning completed!"
```

### 3. PRD Generation Pipeline

```python
#!/usr/bin/env python3
# prd_pipeline.py

import subprocess
import json
import sys
from pathlib import Path

class GeminiPRDPipeline:
    """Automated PRD generation pipeline using Gemini CLI"""
    
    def __init__(self, feature_name: str):
        self.feature_name = feature_name
        self.workspace = Path.home() / "pm-workspace" / feature_name
        self.workspace.mkdir(parents=True, exist_ok=True)
        
    def run_pipeline(self):
        """Execute complete PRD generation pipeline"""
        
        print(f"Starting PRD pipeline for {self.feature_name}")
        
        # Step 1: Gather requirements
        self.gather_requirements()
        
        # Step 2: Research and analysis
        self.conduct_research()
        
        # Step 3: Generate PRD sections
        self.generate_prd_sections()
        
        # Step 4: Consolidate and review
        self.consolidate_prd()
        
        # Step 5: Generate supporting artifacts
        self.generate_artifacts()
        
        # Step 6: Distribute
        self.distribute_prd()
        
        print(f"PRD pipeline completed for {self.feature_name}")
    
    def gather_requirements(self):
        """Gather requirements from multiple sources"""
        
        print("Gathering requirements...")
        
        # Fetch from various sources
        sources = [
            ("jira", f"project = PM AND component = '{self.feature_name}'"),
            ("slack", f"channel:product-feedback {self.feature_name}"),
            ("docs", f"folder:requirements {self.feature_name}"),
            ("survey", f"form:user-feedback {self.feature_name}")
        ]
        
        for source, query in sources:
            cmd = f"gemini integrate fetch --source {source} --query '{query}' --output {self.workspace}/{source}-requirements.json"
            subprocess.run(cmd, shell=True)
        
        # Consolidate requirements
        cmd = f"gemini consolidate requirements --input {self.workspace}/*-requirements.json --output {self.workspace}/consolidated-requirements.md"
        subprocess.run(cmd, shell=True)
    
    def conduct_research(self):
        """Conduct market and user research"""
        
        print("Conducting research...")
        
        # Competitive analysis
        cmd = f"""gemini research competitive \
            --feature '{self.feature_name}' \
            --competitors auto-detect \
            --aspects 'features,pricing,ux' \
            --output {self.workspace}/competitive-analysis.md"""
        subprocess.run(cmd, shell=True)
        
        # User research synthesis
        cmd = f"""gemini research users \
            --data user-interviews.json \
            --filter "feature:{self.feature_name}" \
            --insights personas,jobs-to-be-done,pain-points \
            --output {self.workspace}/user-research.md"""
        subprocess.run(cmd, shell=True)
        
        # Technical feasibility
        cmd = f"""gemini research technical \
            --requirements {self.workspace}/consolidated-requirements.md \
            --architecture current-architecture.json \
            --estimate effort,risk,dependencies \
            --output {self.workspace}/technical-assessment.md"""
        subprocess.run(cmd, shell=True)
    
    def generate_prd_sections(self):
        """Generate individual PRD sections"""
        
        print("Generating PRD sections...")
        
        sections = [
            ("executive-summary", "gemini-2.0-flash"),
            ("problem-statement", "gemini-2.0-pro"),
            ("user-stories", "gemini-2.0-pro"),
            ("functional-requirements", "gemini-2.0-pro"),
            ("technical-requirements", "gemini-2.0-pro-code"),
            ("success-metrics", "gemini-2.0-pro"),
            ("timeline", "gemini-2.0-flash")
        ]
        
        for section, model in sections:
            cmd = f"""gemini generate prd-section \
                --section {section} \
                --model {model} \
                --context {self.workspace}/*.md \
                --output {self.workspace}/{section}.md"""
            subprocess.run(cmd, shell=True)
    
    def consolidate_prd(self):
        """Consolidate all sections into final PRD"""
        
        print("Consolidating PRD...")
        
        cmd = f"""gemini generate prd \
            --sections {self.workspace}/*.md \
            --template comprehensive \
            --toc true \
            --references true \
            --output {self.workspace}/PRD-{self.feature_name}.md"""
        subprocess.run(cmd, shell=True)
        
        # Generate review checklist
        cmd = f"""gemini review prd \
            --input {self.workspace}/PRD-{self.feature_name}.md \
            --checklist completeness,clarity,feasibility \
            --output {self.workspace}/prd-review.md"""
        subprocess.run(cmd, shell=True)
    
    def generate_artifacts(self):
        """Generate supporting artifacts"""
        
        print("Generating supporting artifacts...")
        
        # User flow diagram
        cmd = f"""gemini generate diagram \
            --type user-flow \
            --input {self.workspace}/user-stories.md \
            --format mermaid \
            --output {self.workspace}/user-flow.mmd"""
        subprocess.run(cmd, shell=True)
        
        # Mockups analysis (if available)
        if Path(f"{self.workspace}/mockups").exists():
            cmd = f"""gemini analyze mockups \
                --input {self.workspace}/mockups/*.png \
                --model gemini-2.0-pro-vision \
                --aspects 'ux,accessibility,consistency' \
                --output {self.workspace}/mockup-analysis.md"""
            subprocess.run(cmd, shell=True)
        
        # Test scenarios
        cmd = f"""gemini generate test-scenarios \
            --requirements {self.workspace}/functional-requirements.md \
            --coverage edge-cases,happy-path,error-handling \
            --output {self.workspace}/test-scenarios.md"""
        subprocess.run(cmd, shell=True)
    
    def distribute_prd(self):
        """Distribute PRD to stakeholders"""
        
        print("Distributing PRD...")
        
        # Upload to Google Drive
        cmd = f"""gemini integrate upload \
            --file {self.workspace}/PRD-{self.feature_name}.md \
            --destination google-drive:/PRDs/ \
            --share-with product-team@company.com \
            --permission edit"""
        subprocess.run(cmd, shell=True)
        
        # Create Jira epic
        cmd = f"""gemini integrate create-epic \
            --title '{self.feature_name} Implementation' \
            --description {self.workspace}/PRD-{self.feature_name}.md \
            --attachments {self.workspace}/*.md \
            --assignee product-owner"""
        subprocess.run(cmd, shell=True)
        
        # Send notification
        cmd = f"""gemini integrate notify \
            --channels 'slack:#product,email:stakeholders' \
            --message 'PRD for {self.feature_name} is ready for review' \
            --link auto-generate"""
        subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prd_pipeline.py <feature_name>")
        sys.exit(1)
    
    pipeline = GeminiPRDPipeline(sys.argv[1])
    pipeline.run_pipeline()
```

## Advanced CLI Features

### 1. Interactive Mode

```bash
# Start interactive session
gemini interactive --profile pm

Gemini PM CLI v1.0.0
Type 'help' for commands, 'exit' to quit

gemini> load context product-roadmap.md
✓ Context loaded: 1,234 tokens

gemini> generate user-stories --epic "Mobile App Redesign"
Generating user stories...
✓ Generated 12 user stories

gemini> refine --add-acceptance-criteria
Adding acceptance criteria...
✓ Updated 12 user stories with acceptance criteria

gemini> save user-stories-mobile.md
✓ Saved to user-stories-mobile.md

gemini> analyze complexity
Analyzing story complexity...
┌─────────────────────────┬──────────┬────────────┐
│ Story                   │ Points   │ Risk       │
├─────────────────────────┼──────────┼────────────┤
│ User Authentication     │ 8        │ Medium     │
│ Home Screen Redesign    │ 5        │ Low        │
│ Navigation Update       │ 3        │ Low        │
│ ...                     │          │            │
└─────────────────────────┴──────────┴────────────┘
Total: 47 story points

gemini> exit
```

### 2. Batch Processing

```yaml
# batch-jobs.yaml
jobs:
  - name: "Weekly PRD Updates"
    schedule: "0 9 * * MON"
    tasks:
      - command: "generate prd"
        input: "requirements/*.md"
        output: "prds/week-{{week_number}}"
        model: "gemini-2.0-pro"
        
  - name: "Daily Metrics"
    schedule: "0 8 * * *"
    tasks:
      - command: "analyze metrics"
        source: "analytics-api"
        period: "last-24-hours"
        
      - command: "generate report"
        template: "daily-metrics"
        distribute: ["slack:#metrics", "dashboard"]
        
  - name: "Sprint Retrospective"
    schedule: "0 14 * * FRI/2"
    tasks:
      - command: "analyze sprint"
        metrics: ["velocity", "quality", "satisfaction"]
        
      - command: "generate insights"
        focus: ["improvements", "blockers", "wins"]
        
      - command: "create action-items"
        assign: "auto"
        priority: "by-impact"
```

```bash
# Run batch jobs
gemini batch run batch-jobs.yaml
gemini batch schedule batch-jobs.yaml
gemini batch status
gemini batch logs weekly-prd-updates
```

### 3. Custom Commands and Plugins

```python
# ~/.gemini-pm/plugins/custom_commands.py

from gemini_cli import Plugin, command

class CustomPMCommands(Plugin):
    """Custom PM-specific commands"""
    
    @command("generate", "okr")
    def generate_okr(self, quarter: str, context: str = None):
        """Generate OKRs for the quarter"""
        
        prompt = f"""
        Generate OKRs for {quarter} based on:
        - Product strategy: {self.load_context('strategy.md')}
        - Previous quarter results: {self.load_context('q_results.md')}
        - Market context: {context or 'current market conditions'}
        
        Format:
        - 3-5 Objectives
        - 3-4 Key Results per Objective
        - Measurable and time-bound
        """
        
        return self.gemini_generate(prompt, model='gemini-2.0-pro')
    
    @command("analyze", "nps")
    def analyze_nps(self, data_file: str):
        """Analyze NPS data with insights"""
        
        data = self.load_data(data_file)
        
        prompt = f"""
        Analyze NPS data:
        {data}
        
        Provide:
        1. Score calculation and trend
        2. Promoter/Detractor analysis
        3. Key themes from comments
        4. Action recommendations
        5. Comparison to industry benchmarks
        """
        
        return self.gemini_analyze(prompt, model='gemini-2.0-pro')
    
    @command("workflow", "feature-validation")
    def feature_validation_workflow(self, feature_id: str):
        """Complete feature validation workflow"""
        
        steps = [
            self.validate_requirements(feature_id),
            self.check_technical_feasibility(feature_id),
            self.estimate_effort(feature_id),
            self.assess_market_fit(feature_id),
            self.calculate_roi(feature_id),
            self.generate_go_nogo_recommendation(feature_id)
        ]
        
        return self.execute_workflow(steps)

# Register plugin
plugin = CustomPMCommands()
```

## Integration Examples

### 1. Google Workspace Integration

```bash
# Configure Google Workspace
gemini integrate configure google-workspace \
  --scopes "docs,sheets,slides,drive,calendar" \
  --service-account key.json

# Auto-sync PRDs to Google Docs
gemini integrate sync \
  --source "prds/*.md" \
  --destination "gdrive:/Product/PRDs/" \
  --format google-docs \
  --auto-convert true

# Generate and present slides
gemini generate slides \
  --input quarterly-review.md \
  --template executive-presentation \
  --slides 15 \
  --output-to-slides true \
  --present-link true
```

### 2. Jira Integration

```bash
# Configure Jira
gemini integrate configure jira \
  --url "https://company.atlassian.net" \
  --email "pm@company.com" \
  --token "$JIRA_TOKEN"

# Sync stories from PRD
gemini integrate sync-stories \
  --prd "PRD-authentication.md" \
  --project "PROD" \
  --epic "PROD-123" \
  --auto-create true \
  --assign-to "auto"

# Update story status
gemini integrate update \
  --source jira \
  --filter "sprint = active" \
  --set "status = 'In Review'" \
  --where "development = complete"
```

### 3. Analytics Integration

```bash
# Configure analytics sources
gemini integrate configure analytics \
  --mixpanel-key "$MIXPANEL_KEY" \
  --ga4-property "$GA4_PROPERTY" \
  --amplitude-key "$AMPLITUDE_KEY"

# Pull and analyze metrics
gemini analyze dashboard \
  --sources "mixpanel,ga4,amplitude" \
  --metrics "dau,retention,conversion" \
  --period "last-30-days" \
  --compare-to "previous-period" \
  --visualize true \
  --insights deep
```

## Performance Optimization

### 1. Caching Configuration

```bash
# Enable intelligent caching
gemini config cache \
  --enable true \
  --strategy "semantic" \
  --ttl-flash 1h \
  --ttl-pro 24h \
  --ttl-vision 12h \
  --max-size 2GB

# Clear cache
gemini cache clear --older-than 7d
gemini cache stats
```

### 2. Batch Optimization

```bash
# Process multiple files efficiently
gemini batch process \
  --input "requirements/*.md" \
  --operation "generate prd" \
  --parallel 5 \
  --model-routing "auto" \
  --output-dir "prds/"

# Optimize for cost
gemini batch process \
  --optimize "cost" \
  --fallback-model "gemini-2.0-flash" \
  --quality-threshold 0.8
```

### 3. Model Selection Optimization

```bash
# Configure automatic model selection
gemini config routing \
  --auto-select true \
  --rules routing-rules.yaml

# routing-rules.yaml
rules:
  - pattern: "status|update|summary"
    model: "gemini-2.0-flash"
    
  - pattern: "prd|requirements|analysis"
    model: "gemini-2.0-pro"
    
  - pattern: "mockup|diagram|visual"
    model: "gemini-2.0-pro-vision"
    
  - pattern: "api|code|technical"
    model: "gemini-2.0-pro-code"
    
  cost_threshold: 10.00  # Switch to cheaper model if cost exceeds
  quality_min: 0.85      # Minimum quality score required
```

## Troubleshooting

### Common Issues and Solutions

```bash
# Issue: API rate limiting
gemini config rate-limit \
  --max-requests-per-minute 60 \
  --retry-strategy "exponential-backoff" \
  --max-retries 3

# Issue: Large file processing
gemini config chunking \
  --enable true \
  --chunk-size 30000 \
  --overlap 500 \
  --strategy "semantic"

# Issue: Model timeout
gemini config timeout \
  --flash 30s \
  --pro 120s \
  --vision 180s \
  --code 120s

# Debug mode
gemini --debug generate prd --input test.md

# Check system status
gemini status --verbose
gemini diagnose --full
```

## Best Practices

### 1. Project Structure

```javascript
pm-workspace/
├── .gemini/
│   ├── config.yaml
│   ├── profiles/
│   └── cache/
├── requirements/
│   ├── features/
│   └── templates/
├── prds/
│   ├── in-progress/
│   ├── approved/
│   └── archive/
├── analytics/
│   ├── reports/
│   └── dashboards/
├── workflows/
│   ├── daily.sh
│   ├── weekly.sh
│   └── sprint.sh
└── outputs/
    ├── status/
    └── presentations/
```

### 2. Command Aliases

```bash
# ~/.bashrc or ~/.zshrc
alias gprd="gemini generate prd"
alias gstatus="gemini generate status"
alias ganalyze="gemini analyze"
alias gsync="gemini integrate sync"

# Complex aliases
alias morning_routine="gemini workflow run morning-routine.yaml"
alias sprint_plan="gemini workflow run sprint-planning.yaml"
alias weekly_report="gemini generate report --template weekly --distribute all"
```

### 3. Version Control

```bash
# .gitignore for PM workspace
.gemini/cache/
*.tmp
outputs/tmp/
.env
credentials.json

# Track important files
git add workflows/
git add templates/
git add config.yaml
git commit -m "feat: Add sprint planning workflow"
```

## Conclusion

The Gemini CLI provides a powerful, flexible platform for automating PM workflows. By leveraging Gemini's model family and native integrations, PMs can achieve significant productivity gains while maintaining high-quality outputs. The CLI's extensibility and customization options ensure it can adapt to any team's specific needs and workflows.
