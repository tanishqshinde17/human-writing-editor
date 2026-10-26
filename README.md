# Human Writing Editor

A research-informed AI writing and editing skill designed to improve clarity, specificity, voice, and narrative structure while preserving the author's intended meaning.

## Overview

**Human Writing Editor** helps revise prose so it reads naturally for its intended audience. It combines narrative diagnostics for fiction and memoir with practical editing checks for generic, inflated, repetitive, or robotic-sounding language.

Rather than applying superficial wording changes, the skill focuses on identifying and fixing underlying writing problems. For fiction, it considers character motivation, causality, relationships, information control, and character development. For everyday and professional writing, it focuses on purpose, audience, factual accuracy, voice, and sentence-level clarity.

## Features

- **General prose editing:** Improve essays, reports, blog posts, emails, cover letters, and professional messages.
- **Fiction and memoir analysis:** Review scene structure, character motivation, dialogue, pacing, causality, and endings.
- **Sentence-level diagnostics:** Identify vague wording, inflated phrasing, repetition, stock expressions, and formulaic structures.
- **Voice preservation:** Respect the author's preferences, original meaning, and genre conventions.
- **Factual fidelity:** Avoid inventing experiences, credentials, statistics, quotations, or sources.
- **Research-informed analysis:** Apply narrative dimensions discussed in *StoryScope: Investigating Idiosyncrasies in AI Fiction* as diagnostic tools.
- **Evaluation resources:** Include sample cases, scripts, and documented checks to support testing and review.

## Repository Structure

```text
human-writing-editor/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── references/
│   ├── fiction-toolkit.md
│   └── research-findings.md
└── evals/
    ├── test-samples.md
    ├── run_3_0_1.py
    ├── results-3.0.1.md
    ├── check_figures.py
    └── figure-check.md
```

### Key Files

| File | Description |
|---|---|
| `SKILL.md` | Main skill instructions and editing workflow |
| `references/fiction-toolkit.md` | Detailed framework for reviewing narrative writing |
| `references/research-findings.md` | Summary of relevant research findings and limitations |
| `evals/test-samples.md` | Sample inputs and evaluation cases |
| `evals/run_3_0_1.py` | Evaluation script |
| `evals/results-3.0.1.md` | Recorded evaluation results |
| `evals/check_figures.py` | Figure-related validation script |
| `evals/figure-check.md` | Figure validation notes |
| `CHANGELOG.md` | Version history and documented changes |

## Installation

This project is designed for AI assistant environments that support Markdown-based skills.

1. Clone or download this repository.
2. Place the skill directory in the appropriate skills location for your AI assistant.
3. Ensure `SKILL.md`, `references/`, and `evals/` remain together so the skill can access its supporting resources.
4. Follow the installation and activation instructions for your chosen AI assistant.
5. Test the skill with a sample writing task before using it in a larger workflow.

**Note:** The exact installation path and activation method depend on the AI assistant or agent framework you use.

## Usage Examples

Use the skill with requests such as:

- "Edit this email to make it clearer and more natural while preserving its meaning."
- "Review this short story for character motivation, causality, and pacing."
- "Improve this report without changing its factual claims."
- "Polish my professional summary using only the information I provided."
- "Identify repetitive and generic phrasing and suggest specific revisions."
- "Analyze this fictional scene for character development and narrative coherence."

## Editing Principles

The skill follows these principles:

1. Follow explicit user instructions and constraints.
2. Preserve the author's facts, intent, and meaning.
3. Adapt the writing to the intended audience and genre.
4. Improve structure before polishing individual sentences when necessary.
5. Make changes that address identifiable writing problems.
6. Flag uncertainty instead of inventing missing information.
7. Treat stylistic recommendations as context-dependent rather than universal rules.

## Research Background

The skill references the research paper *StoryScope: Investigating Idiosyncrasies in AI Fiction* (COLM 2026; arXiv:2604.03136).

The research-informed narrative dimensions are used to guide editorial analysis and identify potential weaknesses in writing. They are not intended to impose a single style on every author or genre.

The findings discussed in the research concern patterns in a particular corpus of English-language short fiction. They should not automatically be generalized to all forms of writing.

## Evaluation

The `evals/` directory contains test samples, evaluation scripts, recorded results, and validation notes.

These resources can help assess the skill's behavior and identify areas for improvement. Results should be interpreted within the scope of the included tests; passing a limited evaluation does not establish general effectiveness across every writing task.

## Limitations

- Editing quality depends on the input text, task instructions, and AI model used.
- Narrative conventions vary across genres, cultures, and authors.
- Research findings may not generalize beyond the datasets and tasks studied.
- Evaluation results are not independent proof of overall writing quality.
- The skill does not guarantee AI-detector outcomes or promise to evade AI-detection systems.

## Version

**Current skill version:** `3.0.1`

Refer to [`CHANGELOG.md`](CHANGELOG.md) for version history.

## License

No license is specified in this repository.

Before publishing or redistributing the project, verify the licensing terms for the original research, reference materials, evaluation resources, and any third-party content. Add an appropriate `LICENSE` file once redistribution rights have been confirmed.

---

*Built to support thoughtful, context-aware
