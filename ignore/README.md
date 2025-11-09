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

# GitIgnore Files Collection

## Overview

This directory contains all `.gitignore` files collected from various projects and consolidated into a single location for reference and reuse.

**Collection Date**: 2025-09-02
**Total Files Collected**: 21 `.gitignore` files
**Master File**: `master.gitignore` - Contains all unique patterns consolidated

## Files Origin Mapping

### Desktop Projects

- `apps-script-samples-main.gitignore` ← `/Desktop/To Process/apps-script-samples-main/`
- `wasm-hello-world.gitignore` ← `/Desktop/To Process/apps-script-samples-main/wasm/hello-world/`
- `wasm-image-add-on.gitignore` ← `/Desktop/To Process/apps-script-samples-main/wasm/image-add-on/`
- `wasm-python.gitignore` ← `/Desktop/To Process/apps-script-samples-main/wasm/python/`

### Obsidian Root Projects

- `Agents.gitignore` ← `/Obsidian/Agents/`
- `Real-Estate-MCP.gitignore` ← `/Obsidian/Real Estate MCP/`
- `Spreadsheets.gitignore` ← `/Obsidian/Spreadsheets/`
- `TypeNotes.gitignore` ← `/Obsidian/TypeNotes/`
- `Workspace-Automation.gitignore` ← `/Obsidian/Workspace Automation/`

### Public Projects

- `Vibe-Coding-Gold.gitignore` ← `/Obsidian/Public Projects/Vibe Coding Gold/`
- `quartz.gitignore` ← `/Obsidian/Public Projects/Vibe Coding Gold/quartz/`
- `Public-Workspace-Automation.gitignore` ← `/Obsidian/Public Projects/Workspace Automation/`

### Nested Projects

- `dotfiles.gitignore` ← `/Obsidian/TypeNotes/dotfiles/`
- `dotfiles-docs.gitignore` ← `/Obsidian/TypeNotes/dotfiles/docs/`
- `zen-mcp-server.gitignore` ← `/Obsidian/TypeNotes/zen-mcp-server/`
- `zen-venv.gitignore` ← `/Obsidian/TypeNotes/zen-mcp-server/.zen_venv/`
- `Another-Google-Automation-Repo.gitignore` ← `/Obsidian/Workspace Automation/Another-Google-Automation-Repo/`

### Application-Specific

- `gmail-app.gitignore` ← `/Obsidian/Public Projects/Workspace Automation/apps/gmail/`
- `test-environment.gitignore` ← `/Obsidian/Public Projects/Workspace Automation/test-environment/`

## Duplicate Files Removed

Two duplicate files were found and consolidated:

- Gmail app configuration (identical in two locations)
- Test environment configuration (identical in two locations)

## Pattern Categories Found

### 1. Operating System Files

- macOS: `.DS_Store`, `.Spotlight-V100`, `.Trashes`, etc.
- Windows: `Thumbs.db`, `Desktop.ini`, etc.

### 2. IDE & Editor Files

- VS Code: `.vscode/`
- JetBrains: `.idea/`
- Vim: `*.swp`, `*.swo`
- Eclipse: `.project`, `.classpath`

### 3. Programming Languages

- **Node.js/JavaScript**: `node_modules/`, `*.log`, `dist/`, `build/`
- **Python**: `__pycache__/`, `*.py[cod]`, `venv/`, `.venv`
- **TypeScript**: `*.tsbuildinfo`, `*.d.ts.map`
- **Java/Gradle**: `.gradle/`, `target/`
- **WASM**: `/src/pkg`, `.wireit`

### 4. Build & Distribution

- Common: `dist/`, `build/`, `out/`, `target/`
- Archives: `*.zip`, `*.tar.gz`, `*.rar`

### 5. Testing & Coverage

- Coverage tools: `coverage/`, `.coverage`, `htmlcov/`
- Test frameworks: `.pytest_cache/`, `.tox/`, `.nyc_output/`

### 6. Environment & Configuration

- Environment files: `.env`, `.env.*`
- Credentials: `credentials.json`, `service-account.json`
- Config files: `config.json`, `settings.json`

### 7. Google Apps Script & Clasp

- `.clasp.json`, `.clasprc.json`
- Exception for apps directory: `!apps/**/.clasp.json`

### 8. Obsidian-Specific

- `.obsidian/` (with exceptions for appearance settings)
- `.trash/`, `Untitled*.md`

### 9. Project-Specific Patterns

- Quartz: `public/`, `.quartz-cache/`
- MCP: `.mcp-cache/`
- Google Drive: `~$*` (temp files)

## Usage

### Using the Master File

The `master.gitignore` file contains all unique patterns from all projects. You can:

1. Copy it entirely for new projects
2. Extract specific sections as needed
3. Use it as a reference for creating custom `.gitignore` files

### Using Individual Files

Each original `.gitignore` file is preserved with a descriptive name indicating its origin project. Use these when you need project-specific patterns.

## Maintenance Notes

- All files have been moved (not copied) from their original locations
- Dependencies have been preserved - projects may need new `.gitignore` files created from these templates
- The master file is organized by category with clear section headers
- Duplicate patterns have been removed in the master file
- Special "keep" patterns (starting with `!`) are preserved at the end

## Statistics

- **Total unique patterns**: ~200+
- **Most common patterns**: `node_modules/`, `.DS_Store`, `*.log`, `.env`
- **Language coverage**: JavaScript, TypeScript, Python, Java, Ruby, WASM
- **Tool coverage**: npm, yarn, pip, gradle, clasp, docker
- **IDE coverage**: VS Code, JetBrains, Vim, Eclipse, Emacs

## Recommendations

1. For new Node.js projects: Use sections 1-3, 5, 6
2. For Python projects: Use sections 1-2, Python subsection, 5, 6
3. For Google Apps Script: Use the Google Apps Script section + basic patterns
4. For Obsidian plugins: Use the Obsidian section + relevant language patterns
5. For full-stack projects: Consider using the entire master file

---

*This collection ensures consistent ignore patterns across all projects and serves as a comprehensive reference for future development.*
