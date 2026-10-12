"""Generate requirements.csv from PRD-v*.md (importable via platform delivery: work items > import > requirement).

Usage: python scripts/prd_to_csv.py prd/v0.1/PRD-v0.1.md "v0.1 初始版本"
Columns follow the platform import synonyms: 编号 / 标题 / 描述 / 优先级 / 迭代 / 标签 / 验收标准.
"""
import csv
import re
import sys
from pathlib import Path

src = Path(sys.argv[1])
iteration = sys.argv[2]
text = src.read_text(encoding="utf-8")
blocks = re.split(r"^### (?=REQ-\d+)", text, flags=re.M)[1:]
rows = []
for b in blocks:
    head, _, body = b.partition("\n")
    m = re.match(r"(REQ-\d+) (.+?) 〔(P\d) · (.+?)〕", head.strip())
    if not m:
        raise SystemExit(f"bad heading: {head}")
    key, title, prio, label = m.groups()
    body = body.split("\n---")[0].strip()
    rule, _, ac = body.partition("**AC**")
    rule = re.sub(r"^\*\*规则\*\*：?\s*", "", rule.strip())
    ac = re.sub(r"^[：:]\s*", "", ac.strip())
    rows.append([key, title, rule.strip(), prio, iteration, label, ac.strip()])
out = src.parent / "requirements.csv"
with out.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["编号", "标题", "描述", "优先级", "迭代", "标签", "验收标准"])
    w.writerows(rows)
print(f"{out}: {len(rows)} requirements")
