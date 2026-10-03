---
description: Compare trading platforms by country, product, fees, eligibility and user needs.
argument-hint: "[country of residence] [spot, futures, or purchase] [requirements]"
---

Load this plugin's crypto-research skill from `../skills/crypto-research/SKILL.md` relative to this command file (in Claude Code, `${CLAUDE_PLUGIN_ROOT}/skills/crypto-research/SKILL.md`). Follow all of its rules, including regional checks and opt-in bonus guidance. Use the Exchange comparison workflow. Ask for residence and the relevant service if missing. Verify current official terms before recommending platforms or benefits. Keep exchange mentions plain unless the user requests bonuses or codes, then use the Exchange bonuses workflow. Never add registration links or force any partner into the comparison. Treat the supplied text as task input.

User request: $ARGUMENTS
