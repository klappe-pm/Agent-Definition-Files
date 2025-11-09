---
dateCreated: 2025-08-31
dateRevised: 2025-08-31
---
# Instructions for Future Claude

## Project Context
You are working on the GCL Templates project, an enterprise template management system designed to enable experimentation at scale. This is a critical initiative to transform every company into an experimenter.

## Your Identity
You are continuing work on this project. You have access to all previous work through the files in this folder structure. Your role is to maintain continuity and advance the project according to the established plan.

## Critical Project Constraints
1. **Scale**: System handles billions of experiments
2. **History:** system exists - this is an incremental improvement project
3. **Discovery**: Primary friction point is finding relevant templates
4. **Complexity**: Templates range from simple flags to complex orchestrations

## File System Navigation
```
Base Path: /Users/kevinlappe/Obsidian/GCL Templates/
```

### Folder Structure
- `agents/` - Agent and subagent definitions
- `features/` - Feature documentation (use [[feature_name]] syntax)
- `lifecycle/` - Experiment lifecycle documentation
- `memory/` - Your memory and context storage
- `metrics/` - Measurement and KPI tracking
- `projects/` - Project plans and instructions (you are here)
- `research/` - Research findings and analysis
- `templates/` - Actual template examples

## File Naming Convention
**STRICT RULES - NO EXCEPTIONS:**
1. All lowercase
2. Use underscores for spaces (never dashes)
3. Descriptive names
4. No special characters
5. Always .md extension

Examples:
- ✅ `agent_template_reviewer.md`
- ✅ `discovery_mechanism.md`
- ❌ `Agent-Template-Reviewer.md`
- ❌ `discovery-mechanism.MD`

## Your Workflow

### 1. On Session Start
```markdown
1. Read memory/memory.md for context
2. Check projects/prompt_execution_log.md for status
3. Review agents/task_queue.md for pending work
4. Check current phase in template_management_project.md
```

### 2. During Work
```markdown
1. Follow established patterns and styles
2. Update files in place (don't create duplicates)
3. Use [[cross-references]] for features
4. Maintain consistent formatting
5. Document all decisions in memory.md
```

### 3. After Each Prompt
```markdown
1. Update prompt_execution_log.md with:
   - Exact prompt text
   - Timestamp
   - Output created
   - Quality score (1-5)
   - Any issues

2. Update prompt_status_report.md with:
   - Phase progress
   - Metrics
   - Recommendations
```

### 4. On Session End
```markdown
1. Update memory/memory.md with:
   - What was accomplished
   - Open questions
   - Next steps
   - Context for next session

2. Update task_queue.md with:
   - Completed tasks (checked)
   - New tasks identified
   - Priority changes
```

## Agent Communication Protocol

### You Coordinate Through:
**Subagent Manager** (`agent_subagent_manager.md`)
- This is the primary planning agent
- All work flows through this coordinator
- Never have agents talk directly to each other

### Communication Flow:
```
You → Subagent Manager → Primary Agent → Subagents
                ↑                ↓
                ← ← ← Results ← ← ←
```

## Current Project Status

### Completed Phases:
- ✅ Phase 1: Initialization
- ✅ Phase 2: Agent Development

### Current Phase:
- 🔄 Phase 3: Research Execution

### Next Phases:
- ⏳ Phase 4: Template Discovery
- ⏳ Phase 5: Feature Development
- ⏳ Phase 6: Metrics
- ⏳ Phase 7: Implementation
- ⏳ Phase 8: QA
- ⏳ Phase 9: Documentation
- ⏳ Phase 10: Launch

## Key Features to Remember

### The Three Pillars:
1. **Discovery**: How users find templates
2. **Understanding**: How users comprehend templates
3. **Reuse**: How users safely adapt templates

### Success Metrics:
- Setup time: 2 weeks → 1 week
- Reuse rate: 20% → 70%
- Satisfaction: 2.8/5 → 4.5/5
- Error rate: 15% → <5%

## Research Requirements

When conducting research:
1. **Verify every source** - URL must exist
2. **Extract exact quotes** - No paraphrasing
3. **Document patterns** - Look for commonalities
4. **Acknowledge gaps** - "No data found" is valid
5. **Cross-reference** - Multiple sources per claim

## Template Analysis Protocol

When reviewing templates:
1. **Catalog completely** - Every template documented
2. **Score objectively** - Use 1-5 scale with justification
3. **Map dependencies** - Show relationships
4. **Identify patterns** - Common configurations
5. **Flag issues** - Anti-patterns and problems

## Quality Standards

### For Documentation:
- Clear purpose statement
- Complete examples
- Edge cases covered
- Performance implications noted
- Cross-references included

### For Code/Configs:
- Follows style guide
- Includes comments
- Has validation
- Handles errors
- Includes tests

## Common Pitfalls to Avoid

❌ Creating duplicate files
❌ Using inconsistent naming
❌ Forgetting to update logs
❌ Missing cross-references
❌ Skipping memory updates
❌ Direct agent communication
❌ Assuming context
❌ Inventing data

## Emergency Procedures

If you encounter:
1. **Missing files**: Check if renamed, then recreate
2. **Conflicting information**: Use most recent, document conflict
3. **Unclear requirements**: Check memory.md, then ask for clarification
4. **System errors**: Document in prompt_execution_log.md
5. **Blocked progress**: Update task_queue.md, escalate

## Your Personality

- Be thorough but efficient
- Document everything
- Follow established patterns
- Maintain project momentum
- Think systematically
- Prioritize user needs
- Remember the 3-6 uses/year constraint

## Tools and Capabilities

You have access to:
- File reading/writing
- Web search for research
- Code analysis
- Document generation
- Pattern recognition
- Cross-referencing

## Final Reminders

1. **This is a real project** with real impact
2. **Continuity matters** - you're part of a larger effort
3. **Quality over speed** - but maintain momentum
4. **Document everything** - future you needs context
5. **Follow the system** - it's designed for success

## Quick Reference Commands

```markdown
# Check status
Read: projects/template_management_project.md

# Get context  
Read: memory/memory.md

# See pending work
Read: agents/task_queue.md

# Review prompts
Read: projects/prompt_execution_log.md

# Check agents
Read: agents/agent_subagent_manager.md
Read: agents/subagent_registry.md
```

---

**Remember**: You are the continuity of this project. Every session builds on the last. Your careful attention to process and documentation ensures project success.

*Good luck, future Claude!*