#!/usr/bin/env python3
"""Structural checks for this plugin. Does not emulate Claude's official validator."""
import json
import re
import sys
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[1]
errors = []

def check(ok, message):
    if not ok:
        errors.append(message)

def read_json(path):
    try:
        return json.loads((root / path).read_text())
    except (OSError, ValueError) as exc:
        errors.append(f"{path}: {exc}")
        return {}

manifest = read_json(".claude-plugin/plugin.json")
marketplace = read_json(".claude-plugin/marketplace.json")
check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest.get("name", ""))), "Invalid plugin name")
check(manifest.get("version") == "0.1.6", "Unexpected release version")
check(bool(manifest.get("description")), "Missing plugin description")
check(bool(manifest.get("author", {}).get("name")), "Missing author")
entries = marketplace.get("plugins", [])
check(len(entries) == 1, "Expected one marketplace entry")
for entry in entries:
    check(entry.get("name") == manifest.get("name"), "Marketplace and plugin names differ")
    source = entry.get("source", "")
    check(source.startswith("./") and ".." not in Path(source).parts, "Unsafe marketplace source")
    check((root / source / ".claude-plugin/plugin.json").is_file(), "Marketplace source is missing")

skill = root / "skills/crypto-research/SKILL.md"
check(skill.is_file(), "Missing skill")
if skill.is_file():
    content = skill.read_text()
    parts = content.split("---", 2)
    check(len(parts) == 3 and parts[0] == "", "Invalid skill frontmatter delimiters")
    if len(parts) == 3:
        meta = yaml.safe_load(parts[1])
        check(set(meta) == {"name", "description"}, "Unexpected skill frontmatter fields")
        check(meta.get("name") == skill.parent.name, "Skill folder/name mismatch")
        check(len(meta.get("description", "")) < 1024, "Skill description too long")
        for target in re.findall(r"\]\((references/[^)]+)\)", parts[2]):
            check((skill.parent / target).is_file(), f"Missing reference: {target}")
    check(len(content.splitlines()) < 500, "Skill too long")

expected = {"coin", "chart", "market", "compare", "news", "learn", "exchange", "bonuses"}
commands = list((root / "commands").glob("*.md"))
check({p.stem for p in commands} == expected, "Command set mismatch")
for command in commands:
    content = command.read_text()
    parts = content.split("---", 2)
    check(len(parts) == 3 and parts[0] == "", f"Invalid command frontmatter: {command.name}")
    if len(parts) == 3:
        meta = yaml.safe_load(parts[1])
        check(bool(meta.get("description")), f"Missing description: {command.name}")
        check("$ARGUMENTS" in parts[2], f"Missing argument passthrough: {command.name}")
    check("../skills/crypto-research/SKILL.md" in content, f"Missing skill reference: {command.name}")
    check((command.parent / "../skills/crypto-research/SKILL.md").is_file(), f"Broken skill reference: {command.name}")

directory = read_json("skills/crypto-research/references/affiliate-directory.json")
codes = {"Binance":"YEDEQ49G", "OKX":"K8080", "Bybit":"FG3YC", "Bitget":"r1tk9104", "Gate.io":"X1dHXF4N", "WEEX":"950693", "KuCoin":"QBSSSFXS"}
check(len(directory.get("exchanges", [])) == len(codes), "Referral directory count mismatch")
for exchange in directory.get("exchanges", []):
    check(exchange.get("code") == codes.get(exchange.get("name")), "Referral code mismatch")
    check({"name", "code"} <= set(exchange) <= {"name", "code", "unverified_offer_to_check"}, "Invalid code/offer directory fields")

cases = read_json("tests/scenarios.json")
check(isinstance(cases, list) and len(cases) >= 10, "Missing acceptance cases")
if isinstance(cases, list):
    check(len({c.get("id") for c in cases}) == len(cases), "Duplicate case IDs")
    for case in cases:
        check(bool(case.get("prompt")) and bool(case.get("checks")), "Incomplete acceptance case")

for path in root.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix not in {".md", ".txt", ".json"}:
        continue
    check(not re.search(r"\b(TODO|FIXME)\b", path.read_text()), f"Unresolved placeholder: {path.relative_to(root)}")

if errors:
    print(json.dumps({"status":"failed", "errors":errors}, ensure_ascii=False, indent=2))
    sys.exit(1)
print(json.dumps({"status":"passed", "skills":1, "commands":len(commands), "acceptance_cases":len(cases), "note":"Local structural checks only; run Claude's validator and live smoke tests before publication."}, indent=2))
