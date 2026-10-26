# Figure check: research-findings.md against the paper

Run on 25 October 2026 against arXiv:2604.03136v6 (10 August 2026). arXiv still listed v6 as the current version on that date.

**Method.** The paper PDF was converted to text with pdftotext (layout and raw modes). For each figure quoted in `references/research-findings.md`, `check_figures.py` searches for the exact sentence or table row it comes from, after normalising whitespace and dash characters. A figure passes only if that exact text is present.

**Rerun:** `pdftotext -layout paper.pdf paper.txt; pdftotext paper.pdf paper_raw.txt; python3 check_figures.py paper.txt paper_raw.txt`

**Result: 84 of 84 figures found.**

| Status | Figure |
| --- | --- |
| found | 10,272 human stories / prompts |
| found | Books3 anthologies |
| found | Prompts reverse-engineered with Gemini 2.5 Flash |
| found | Models: Claude Sonnet 4.6 |
| found | Models: GPT-5.4 |
| found | Models: Gemini 3 Flash |
| found | Models: DeepSeek V3.2 |
| found | Models: Kimi K2.5 |
| found | 61,608 stories |
| found | Mean length 4,753 words |
| found | Gemini median 2,967 |
| found | DeepSeek median 2,693 |
| found | Kimi median 3,005 |
| found | 408 candidates |
| found | 304 features after dedup |
| found | 47 style features excluded |
| found | 257 narrative-only features |
| found | 30 core and 75 fingerprint features |
| found | Krippendorff alpha 0.90 |
| found | Mean human-model kappa 0.84 |
| found | Human-human kappa 0.74 |
| found | 240 items across 12 stories |
| found | Binary: Narrative 93.2 |
| found | Binary: Core only 84.8 |
| found | Binary: Core+FP 91.1 |
| found | Binary: Narrative+Style 96.0 |
| found | Binary: Style only 85.8 |
| found | Binary: ModernBERT 99.9 |
| found | Binary: Stylometric 99.8 |
| found | Binary: TF-IDF 99.7 |
| found | Binary: Binoculars 55.9 |
| found | Six-way: Narrative 68.4 |
| found | Six-way: Core only 46.5 |
| found | Six-way: Core+FP 63.4 |
| found | Six-way: Narrative+Style 77.3 |
| found | Six-way: Style only 60.4 |
| found | Six-way: ModernBERT 99.8 |
| found | Six-way: TF-IDF 99.5 |
| found | LAMP on 278 Gemini stories |
| found | LAMP 93.9 after vs 95.5 before |
| found | Length-matched 93.2 |
| found | No topic effect, p = 0.46 |
| found | Topic test over six topics |
| found | Memorization filter leaves results unchanged |
| found | Per-class F1, narrative only |
| found | Thematic explicitness 3.28 / 3.94 |
| found | Moral weighting 3.26 / 3.68 |
| found | Narrator theme commentary 52% / 77% |
| found | Dialogue as debate 34% / 59% |
| found | Implicit echoes 50% / 72% |
| found | Embodied emotion 38% / 81% |
| found | Smell 57% / 82% |
| found | Setting mirror 3.58 / 4.07 |
| found | Causal chain 3.92 / 4.20 |
| found | Protagonist-choice resolution 46% / 69% |
| found | No subplots 57% / 79% |
| found | Internal resolution 27% / 47% |
| found | External description intro 30% / 52% |
| found | Named references 47% / 24% |
| found | Balanced references 37% / 16% |
| found | Explicit emotion labels 29% / 8% |
| found | Morally mixed 59% / 38% |
| found | Parallel subplots 42% / 21% |
| found | Recontextualization 3.28 / 2.95 |
| found | Chronological discontinuity 2.40 / 2.12 |
| found | Anachrony 2.58 / 2.31 |
| found | Fourth wall in Table 16 as ordinal 0.67 / 0.39 |
| found | Reader address in Table 16 as ordinal 0.28 / 0.07 |
| found | Fourth wall in text as 67% vs 39% |
| found | Reader address in text as 28% vs 7% |
| found | Rarity 0.71 vs 0.49 |
| found | Cohen's d 0.83 |
| found | Human rarest 57.8% |
| found | 24.7% vs 7.1% in rarest tenth |
| found | Rarity over 25 nearest neighbours |
| found | Claude continuist 62% vs 39-56% |
| found | GPT gossip 64% vs 44-55% |
| found | GPT subverts 41% vs 27-36% |
| found | Gemini bleak 88% |
| found | Per-source fingerprint counts |
| found | Dimension list includes Structure |
| found | Situatedness used in tables |
| found | Test set 1,377 prompts (8,262 stories) |
| found | Test set 1,384 prompts (8,301 stories) |

**Derived claims also checked**

- Gaps on Table 16's non-percentage features run from 0.20 to 0.65 points. The findings file originally said "a quarter to two-thirds of a point"; corrected to "about 0.2 to 0.65" in 3.0.1.
- The paper's per-source fingerprint counts sum to 90, against 75 stated in the methods footnote. The findings file reports this as an inconsistency rather than choosing a number.
- Both forms of the fourth-wall and reader-address figures exist in the paper (percentages in Section 4.1, ordinal means in Table 16). The findings file says only that human stories did both more often.

**Not covered by this check:** paraphrased descriptions (for example, "Claude: quiet endings") were reviewed by reading, not by script.
