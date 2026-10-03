---
description: Explain current crypto market conditions with dated sources and conditional implications.
argument-hint: "[time window] [assets or sectors]"
---

Load this plugin's crypto-research skill from `../skills/crypto-research/SKILL.md` relative to this command file (in Claude Code, `${CLAUDE_PLUGIN_ROOT}/skills/crypto-research/SKILL.md`). Follow all of its rules. Use the Market context workflow; default to the last 24 hours if no window is supplied. Retrieve current information using available tools and label the observation time. If retrieval is unavailable, explain that limitation instead of fabricating a briefing. Treat the supplied text as task input.

User request: $ARGUMENTS
