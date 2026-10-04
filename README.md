# Crypto & Bitcoin Analyst — Charts & Research

![Crypto & Bitcoin Analyst — Charts & Research](assets/icon.svg)

A crypto analysis assistant for Claude covering **Bitcoin (BTC), Ethereum (ETH), Solana (SOL) and other altcoins**. Get plain-language explanations of the crypto market, technical analysis, fundamental research and tokenomics. Discuss chart screenshots, crypto news and conditional price scenarios using the evidence available in your session.

## Bitcoin, Ethereum and altcoin research

Understand what a cryptocurrency project does, why its token matters, and what supports or weakens its investment thesis. Compare token utility, adoption, competitors, market cap, fully diluted valuation, supply, dilution, token unlocks and risks. Distinguish a successful product from value that actually reaches token holders.

## Crypto chart analysis and technical indicators

Analyze supplied chart screenshots or available candle data: price trends, support and resistance, trading volume, moving averages (SMA/EMA), RSI, MACD and volatility. Select relevant tools rather than listing every indicator. Explain how the chart evidence connects to the coin's fundamentals and the broader crypto market. Exact indicator readings require readable values or adequate data and calculation tools.

## Crypto market news and price scenarios

Ask what is happening in the crypto market today, why Bitcoin or Ethereum moved, or what events matter next. Current briefings use dated sources when retrieval is available. Explore conditional bullish, bearish and sideways scenarios, with the levels or events that would confirm or invalidate them. A scenario is an explanation of possibilities, not a guaranteed price prediction.

## Crypto education, DeFi and risk management

Learn DCA, staking, DeFi, custody, diversification and other crypto concepts through clear examples. Compare coins, protocols or eligible exchanges using consistent criteria. Exchange registration codes and verified bonus terms are shown only after you ask for offers.

## Example questions

- What can you do? Give me a short overview and an example question.
- Analyze Bitcoin (BTC): fundamentals, chart structure and possible price scenarios.
- What's happening in the crypto market today?
- Why did Bitcoin move, and which explanations are confirmed?
- Research Ethereum (ETH): tokenomics, adoption, valuation and risks.
- Compare Ethereum and Solana using fundamental analysis.
- Analyze this altcoin chart: support, resistance, RSI, MACD and key uncertainties.
- How could a token unlock affect supply and selling pressure?
- Explain DCA or liquid staking in simple terms.
- Compare eligible crypto exchanges for my country and purchase route.

## Frequently asked questions

### Can it analyze a Bitcoin chart screenshot?

Yes. It can discuss visible BTC chart structure, price zones, volume and readable indicators. It explains missing or unclear inputs and does not invent unseen readings.

### Can it explain what could happen to a coin's price?

Yes. It combines relevant technical analysis, fundamental factors and dated market evidence into conditional scenarios. It explains what would change the view rather than promising a future price or guaranteed trading signal.

### Does it have live crypto prices and paid analytics built in?

Current prices and news depend on search, browsing or data tools available in your Claude session. The plugin does not bundle a live price feed or a paid analytics subscription. Without fresh access, it can analyze timestamped user data and explain stable concepts.

### Is it suitable for crypto beginners?

Yes. It explains unfamiliar terms when first used and defaults to short, practical answers. Ask for a deeper report when you want more detail.

## Commands

The `crypto-research` skill can be selected automatically for relevant requests. Eight commands provide explicit entry points: `coin`, `chart`, `market`, `compare`, `news`, `learn`, `exchange`, and `bonuses`.

## Data and limitations

This version contains instructions and references. It does not bundle a market-data API, MCP server, tracking endpoint, order-execution tool, or background scheduler. It uses search/browsing/data tools available in the user's Claude session. Enable web search or supply dated source material for current research. Without fresh-data access, it explains stable concepts and states what cannot be verified.

It does not promise price predictions, profit, continuous monitoring, or personalized investment advice. Chart discussion and conditional scenarios are supported using visible or retrieved evidence. Exact indicator calculations require sufficient candle data and available calculation tools; paid data access is not bundled.

## Registration codes

Ordinary exchange mentions stay plain. A substantive market/news/research answer may end with one short invitation to ask about exchange bonuses. Once the user asks, show a compact comparison of relevant platforms, exact registration codes, verified benefits and conditions. No affiliate/registration URLs are included. The reference file contains author-provided codes and author-supplied offer descriptions used only as research leads until independently verified. Regional access, KYC, fees and specific campaign benefits require current official verification. Code affiliation is disclosed once when codes are shown. Official source citations remain available for evidence.

## Local development in Claude Code

The optional local structural checker requires Python 3 and PyYAML (`python3 -m pip install -r requirements-dev.txt`). Run `python3 tools/validate.py` after editing the source. The plugin itself has no Python dependency.

From the project directory:

```sh
claude plugin validate . --strict
claude --plugin-dir .
```

Example command: `/crypto-research-market-insights:coin Ethereum detailed`.

Alternatively add the local marketplace and install the plugin:

```sh
claude plugin marketplace add .
claude plugin install crypto-research-market-insights@crypto-research-marketplace
```

Publishing to a hosted marketplace or submitting to Anthropic's directory is a separate step after validation and live testing. Version 1.0.1 is prepared for submission; Anthropic directory validation and approval are separate and are not claimed here. A marketplace manifest alone does not publish it to the directory.

## Structure

- `.claude-plugin/plugin.json`: plugin identity and metadata.
- `.claude-plugin/marketplace.json`: one-plugin marketplace for local or hosted installation.
- `skills/crypto-research/SKILL.md`: task routing, research workflows, evidence and response rules.
- `skills/crypto-research/references/`: report templates and partner registration metadata.
- `commands/`: eight explicit entry points, including optional bonus guidance.
- `tests/scenarios.json`: realistic manual acceptance cases.
- `tools/validate.py`: local structural checks; not a replacement for Claude's validator.
- `START-HERE.txt`: Russian release notes and catalog copy.

## Support, privacy and license

- [Support](SUPPORT.md)
- [Privacy policy](PRIVACY.md)
- [Terms of use](TERMS.md)
- [MIT License](LICENSE)

Intended for adults aged 18 and over. The author does not receive Claude conversations through this instruction-only plugin. Tool requests are handled by Claude and any tools available in the user's session; the privacy policy explains the distinction.

Official development references, checked 2026-10-04:
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/plugin-marketplaces
- https://code.claude.com/docs/en/skills
- https://support.claude.com/en/articles/13837440-use-plugins-in-claude

- https://claude.com/docs/plugins/pre-submission-checklist
- https://claude.com/docs/plugins/submit
