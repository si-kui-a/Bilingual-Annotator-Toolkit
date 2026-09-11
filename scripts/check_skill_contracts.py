"""
check_skill_contracts.py — 這個repo唯一能離線驗證的兩件事，零依賴、純標準庫。

命名注意：故意不叫`verify_project_contract.py`——那是
si-kui-a/web-scaffold-toolkit的canonical檔名，專門驗證PROJECT_PROFILE.yaml
本身欄位是否填齊（display_name/profile/offline_check等7個必填key），
跟這支腳本檢查的內容完全不同，撞名會誤導未來的人以為這是那支腳本的
本機副本。

背景：PROJECT_PROFILE.yaml的offline_check欄位原本寫
`python scripts/verify_project_contract.py && python scripts/run_profile_checks.py`，
但這兩支腳本從未真的存在於這個repo（2026-09-11全倉庫稽核發現，跑這行offline_check
只會得到"No such file or directory"）。這個repo是純prompt engineering（SKILL.md
指令文件+範例HTML），沒有程式碼可以lint/typecheck/build，能機械驗證的只有下面
這兩件事——不是套用web-platform剖面那套「lint/typecheck/test/build」清單，
而是直接對應CONTRIBUTING.md自己講的審查重點：
  1. 每個 skills/<name>/SKILL.md 的YAML frontmatter要能解析、要有name/description，
     且name必須等於它所在的資料夾名（CONTRIBUTING.md：Claude Code靠這個做skill
     discovery，格式錯了skill就不會被載入，不是「風格」問題是「能不能用」問題）。
  2. examples/README.md表格裡列出的每個檔案路徑都要真的存在（避免文件內容跟
     examples/目錄實際內容各自漂移——README.md宣稱的範例列表沒有機制保證
     跟目錄實況同步）。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check_skill_frontmatter():
    errors = []
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        return errors
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{skill_dir.name}/: 缺少 SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not m:
            errors.append(f"{skill_md.relative_to(ROOT)}: 找不到YAML frontmatter（開頭須為---...---）")
            continue
        frontmatter = m.group(1)
        name_m = re.search(r'^name:\s*(\S+)\s*$', frontmatter, re.MULTILINE)
        desc_m = re.search(r'^description:', frontmatter, re.MULTILINE)
        if not name_m:
            errors.append(f"{skill_md.relative_to(ROOT)}: frontmatter缺少name欄位")
        elif name_m.group(1) != skill_dir.name:
            errors.append(f"{skill_md.relative_to(ROOT)}: frontmatter的name「{name_m.group(1)}」與資料夾名「{skill_dir.name}」不一致")
        if not desc_m:
            errors.append(f"{skill_md.relative_to(ROOT)}: frontmatter缺少description欄位")
    return errors


def check_examples_readme_refs():
    errors = []
    readme = ROOT / "examples" / "README.md"
    if not readme.is_file():
        return errors
    text = readme.read_text(encoding="utf-8")
    for m in re.finditer(r'`([\w./-]+\.html)`', text):
        rel = m.group(1)
        if not (ROOT / "examples" / rel).is_file():
            errors.append(f"examples/README.md 引用的檔案不存在: examples/{rel}")
    return errors


def main():
    errors = check_skill_frontmatter() + check_examples_readme_refs()
    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("OK: 全部 SKILL.md frontmatter 合法且與資料夾名一致，examples/README.md 引用的檔案皆存在")


if __name__ == "__main__":
    main()
