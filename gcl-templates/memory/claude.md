# Claude Next Steps - New Chat Instructions

## 🚀 START HERE - MUST READ ALL FILES

**CRITICAL**: Read ALL project files in the folder structure before proceeding.

**Project**: GCL Templates - Enterprise Template Management System
**Location**: `/Users/kevinlappe/Obsidian/GCL Templates/`
**Current Phase**: 3 - Research Execution (READY TO START)

---

## 📋 STEP 1: Read Every File (IN THIS ORDER)

### Core Project Files
```markdown
1. projects/template_management_project.md
2. projects/claude_instructions.md  
3. projects/prompt_execution_log.md
4. projects/prompt_status_report.md
```

### Memory Files
```markdown
5. memory/memory.md
6. memory/claude.md (this file)
```

### Agent Files
```markdown
7. agents/agent_subagent_manager.md
8. agents/agent_template_reviewer.md
9. agents/agent_template_analyst.md
10. agents/subagent_registry.md
11. agents/task_queue.md
```

### Research Files
```markdown
12. research/research_execution_plan.md
```

### Any Other Files Found
```markdown
13. [List any additional files you find in the folders]
```

---

## 📋 STEP 2: After Reading All Files

### Planning Decisions Already Made
✅ **Run agents in parallel** - All agents and subagents execute simultaneously
✅ **Report at each commit** - Agents report status every time they save work
✅ **GitHub sync needed** - Set up GitHub repository and sync all files
✅ **Add reports to GitHub** - All reports must be committed
❌ **Skip stakeholder updates** - Don't worry about external communications
❌ **Skip quality score obsessing** - Just maintain good quality

---

## 📋 STEP 3: Execute These Tasks

### Priority 1: GitHub Setup
```bash
cd /Users/kevinlappe/Obsidian/GCL Templates/
git init
git add .
git commit -m "Initial GCL Templates project structure"
# Get GitHub repo URL from user
# git remote add origin [URL]
# git push -u origin main
```

### Priority 2: Begin Phase 3 Research
- Start executing prompts 3.1, 3.2, 3.3 from prompt_execution_log.md
- Run all research agents in parallel
- Each agent commits findings immediately

### Priority 3: Update Tracking
After EVERY action:
1. Update prompt_execution_log.md
2. Update prompt_status_report.md  
3. Update memory/memory.md
4. Commit changes to Git

---

## 🔴 CRITICAL REMINDERS

1. **READ ALL FILES FIRST** - Do not skip this step
2. **Follow naming convention** - lowercase, underscores only
3. **Update logs after EVERY prompt** - No exceptions
4. **Agents run in parallel** - Don't wait for sequential completion
5. **Commit frequently** - After each meaningful change
6. **Use Filesystem tools** - Not window.fs for file operations

---

## ❓ What You're Looking For When Reading

- **Project goals**: Every company is an experimenter
- **Key constraint**: Users only use system 3-6 times/year
- **Scale**: Must handle billions of experiments
- **Current status**: Phase 2 complete, Phase 3 ready
- **Communication flow**: Subagents → Agents → Manager
- **Tracking requirements**: Every prompt must be logged

---

## 📝 Your First Message Should Be:

"I've read all [X] files in the GCL Templates project. Here's what I understand:
- [Summary of project status]
- [Current phase and next steps]
- [Any issues or questions found]

Ready to:
1. Set up GitHub sync
2. Begin Phase 3 research execution
3. Run agents in parallel"

---

## 🛠 Tools to Use

- **File Operations**: Use Filesystem tools (read_file, write_file, etc.)
- **Web Search**: Available for research phase
- **Code Analysis**: Available as needed
- **NOT window.fs**: This doesn't work for writing files

---

## 📊 Current File Status

All core files have been created:
- ✅ 8 directories created
- ✅ 13 core files written
- ✅ Project structure established
- ⏳ GitHub sync pending
- ⏳ Research phase pending

---

**DO NOT PROCEED WITHOUT READING ALL FILES FIRST**