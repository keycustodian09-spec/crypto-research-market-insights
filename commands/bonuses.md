---
description: Show exchange registration codes and verify current bonus or fee-discount terms on request.
argument-hint: "[country] [new or existing account] [requirements]"
---

Load this plugin's crypto-research skill from `../skills/crypto-research/SKILL.md` relative to this command file (in Claude Code, `${CLAUDE_PLUGIN_ROOT}/skills/crypto-research/SKILL.md`). Follow all of its rules. Use the Exchange bonuses workflow: select relevant exchanges, show exact registration codes and verify benefits for the current code/campaign, including conditions. Ask for residency/account status only when needed for eligibility. If verification is unavailable, mark benefits unverified and do not quote the directory's old headline claims as current offers. Include no registration links. Treat the supplied text as task input.

User request: $ARGUMENTS
