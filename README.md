# Bilingual Annotator Toolkit

Claude Skills for turning any document into a bilingual, color-coded, dual-column annotated HTML page — plus a companion set of study-visual generators (quiz cards, knowledge maps, flashcards, concept breakdowns).

Language-agnostic. Document-type-agnostic. Not tied to any specific source/target language pair or document genre.

## What's inside

| Skill | Purpose |
|---|---|
| [`skills/bilingual-doc-annotator/SKILL.md`](skills/bilingual-doc-annotator/SKILL.md) | Source text (color-highlighted by argumentative/structural dimension) + target-language translation, side-by-side, with per-paragraph annotations in a right-hand column. Presets for academic papers, articles, legal documents, literary texts, and technical writing — or fully custom dimensions. |
| [`skills/study-visual-generator/SKILL.md`](skills/study-visual-generator/SKILL.md) | Companion toolkit: collapsible Q&A cards, knowledge maps, flashcards, concept-breakdown pages. Same visual system, any output language. |

## Install

**Claude Code (project-level):**
```bash
git clone https://github.com/<your-username>/bilingual-annotator-toolkit.git
mkdir -p .claude/skills
cp -r bilingual-annotator-toolkit/skills/* .claude/skills/
```

**Claude Code (personal, all projects):**
```bash
mkdir -p ~/.claude/skills
cp -r bilingual-annotator-toolkit/skills/* ~/.claude/skills/
```

## Usage

Hand Claude a document and say what language pair / document type you want:

> "Turn this into a bilingual annotated HTML page, English source, Traditional Chinese translation, academic paper preset."

> "Same thing but legal document preset, German to English."

For the study-visual companion:

> "Make me flashcards from this vocabulary list, output in Japanese."

## Design system

- Navy header (`#0A192F`) + off-white paper background (`#F8F9FA`)
- Body font: Lora (serif); CJK (Chinese/Japanese/Korean) source/target text gets serif fallback fonts (Noto Serif TC/JP/KR) — RTL scripts (Arabic, Hebrew, etc.) instead get `dir="rtl"` on the relevant text block, not a CJK font fallback. Two separate rules, see `skills/bilingual-doc-annotator/SKILL.md` STYLE/RULE sections for the source of truth.
- UI font: IBM Plex Sans
- 5-dimension color highlighting — semantic mapping remaps per document-type preset, see each `SKILL.md`
- Fully responsive — single column on mobile

## Examples

See [`examples/`](examples/README.md) for sample HTML output produced from both skills (source/license notes included).

## Contributing

Open to PRs — see [CONTRIBUTING.md](CONTRIBUTING.md). Found a case where Claude ignores the layout or preset? Open an issue.

## License

MIT — see [LICENSE](LICENSE).
