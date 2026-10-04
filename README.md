# Crypto Research & Market Insights

A professional crypto financial-consulting assistant for Claude. Get concise, plain-language answers grounded in financial fundamentals and current evidence: understand today's market, evaluate projects and tokenomics, compare options, and assess risks. It explains its conclusions and the conditions that could change them.

## Capabilities

- Research the product, token utility, dilution, adoption, valuation, catalysts, and risks of a project.
- Compare assets or protocols using consistent criteria.
- Explain crypto market movements and news without claiming unsupported causation.
- Teach crypto, DeFi, staking, custody, and strategies with clear examples.
- Compare exchanges when requested; show registration codes and verified bonus terms only after the user asks for offers.

The included `crypto-research` skill can be selected automatically for relevant requests. Seven commands provide explicit entry points: `coin`, `market`, `compare`, `news`, `learn`, `exchange`, and `bonuses`.

## Examples

- Research Ethereum: utility, tokenomics, competitors, and key risks.
- Compare Ethereum and Solana for a long-term research thesis.
- Explain the main crypto market events from the last 24 hours, with sources.
- What does an upcoming token unlock actually change?
- Explain liquid staking to a beginner.
- Compare eligible spot exchanges for my country and purchase route.

## Data and limitations

This version contains instructions and references. It does not bundle a market-data API, MCP server, tracking endpoint, order-execution tool, or background scheduler. It uses search/browsing/data tools available in the user's Claude session. Enable web search or supply dated source material for current research. Without fresh-data access, it explains stable concepts and states what cannot be verified.

It does not promise price predictions, profit, continuous monitoring, or personalized investment advice. Chart-specific trade entries and position management are outside its main scope.

## Registration codes

Ordinary exchange mentions stay plain. A substantive market/news/research answer may end with one short invitation to ask about exchange bonuses. Once the user asks, show a compact comparison of relevant platforms, exact registration codes, verified benefits and conditions. No affiliate/registration URLs are included. The reference file contains author-provided codes and author-supplied offer descriptions used only as research leads until independently verified. Regional access, KYC, fees and specific campaign benefits require current official verification. Code affiliation is disclosed once when codes are shown. Official source citations remain available for evidence.

## Local development in Claude Code

The optional local structural checker requires Python 3 and PyYAML (`python3 -m pip install -r requirements-dev.txt`). Run `python3 tools/validate.py` after editing the source. The plugin itself has no Python dependency.

From the project directory:

```sh
claude plugin validate .claude-plugin/plugin.json --strict
claude plugin validate .claude-plugin/marketplace.json --strict
claude --plugin-dir .
```

Example command: `/crypto-research-market-insights:coin Ethereum detailed`.

Alternatively add the local marketplace and install the plugin:

```sh
claude plugin marketplace add .
claude plugin install crypto-research-market-insights@crypto-research-marketplace
```

Publishing to a hosted marketplace or submitting to Anthropic's directory is a separate step after validation and live testing. This package has not been submitted or approved. A marketplace manifest alone does not publish it to the directory.

## Structure

- `.claude-plugin/plugin.json`: plugin identity and metadata.
- `.claude-plugin/marketplace.json`: one-plugin marketplace for local or hosted installation.
- `skills/crypto-research/SKILL.md`: task routing, research workflows, evidence and response rules.
- `skills/crypto-research/references/`: report templates and partner registration metadata.
- `commands/`: seven explicit entry points, including optional bonus guidance.
- `tests/scenarios.json`: realistic manual acceptance cases.
- `tools/validate.py`: local structural checks; not a replacement for Claude's validator.
- `START-HERE.txt`: Russian release notes and catalog copy.

Official development references, checked 2026-10-03:
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/plugin-marketplaces
- https://code.claude.com/docs/en/skills
- https://support.claude.com/en/articles/13837440-use-plugins-in-claude
