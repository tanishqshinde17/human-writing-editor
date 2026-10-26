# Research Findings: Verified

Load this file only when the user asks what the research found, whether a piece of advice is backed by the paper, or how the skill relates to it. For editing, the questions in SKILL.md section 4.0 are enough.

Every figure below was checked by script against the text of arXiv:2604.03136 version 6 (10 August 2026); the check is recorded in `evals/figure-check.md` in the source folder. Later versions of the paper may revise them. Cite the paper's sections and tables, not page numbers of any particular copy.

## Citation

Jenna Russell, Rishanth Rajendhran, Chau Minh Pham, Mohit Iyyer (University of Maryland, College Park) and John Wieting (Google DeepMind). *StoryScope: Investigating idiosyncrasies in AI fiction.* Conference on Language Modeling (COLM) 2026. arXiv:2604.03136. Code, prompts, model-written stories and features: github.com/jenna-russell/storyscope. The human-written stories are not released, for copyright reasons.

## One-paragraph summary (safe to paraphrase to users)

The authors asked whether model-written fiction differs from human fiction in how stories are built, not just in word choice. They described about 61,600 stories (one human story and five model-written versions for each of 10,272 prompts) using interpretable narrative features such as plot shape, character agency and chronology, with style features held out. Narrative features alone separated human from model-written stories well, and the five models clustered together in a region of "narrative space" distinct from the human stories, which were more varied. In the corpus, model stories tended to explain their themes, follow one tidy causal thread, and convey emotion through the body and senses; human stories more often used time jumps, moral ambivalence, named references and direct reader address.

## Setup (Section 2, Appendix A)

- **Human stories:** 10,272 short stories extracted from published anthologies in the Books3 collection.
- **Prompts:** reverse-engineered from each human story with Gemini 2.5 Flash; the same prompt went to all five models.
- **Models:** Claude Sonnet 4.6, GPT-5.4, Gemini 3 Flash, DeepSeek V3.2, Kimi K2.5.
- **Corpus:** 61,608 stories, mean length 4,753 words. Gemini, DeepSeek and Kimi wrote well under the requested lengths (medians around 2,700 to 3,000 words).
- **Features:** grounded in the NarraBench taxonomy, across ten dimensions. 408 candidate features were deduplicated to 304; 47 style-related features were removed to give 257 narrative-only features. A subset of 30 "core" features separates human from model stories consistently across all five models; 75 "fingerprint" features (as stated in the paper) identify individual sources.
- **Feature assignment:** done by Gemini 3 Flash. Repeat-run agreement was high (Krippendorff's alpha 0.90). On a 240-item human check across 12 stories, mean human-model agreement was Cohen's kappa 0.84, against 0.74 between the two human annotators.

## Detection results (Tables 2 and 3)

Macro-F1, held-out test set.

| Feature set | Human vs. model | Which of six sources |
| --- | --- | --- |
| Narrative only (257) | 93.2 | 68.4 |
| Core only (30) | 84.8 | 46.5 |
| Core + fingerprint | 91.1 | 63.4 |
| Narrative + style (304) | 96.0 | 77.3 |
| Style only (39) | 85.8 | 60.4 |
| Supervised raw-text baselines (ModernBERT, TF-IDF, stylometric) | 99.7 to 99.9 | 99.5 to 99.8 |
| Binoculars, zero-shot detector | 55.9 | not reported |

- **Surface edits barely mattered.** After a span-level rewrite that removed clichés, purple prose and similar artifacts from 278 Gemini stories, the narrative classifier still scored 93.9, against 95.5 before editing (Section 4.2).
- **Not a length artifact.** On a length-matched subset the narrative model still scored 93.2 (Appendix G).
- **No significant topic effect** across six genres (Appendix G).
- **Not driven by memorized classics.** Removing prompts with likely memorized outputs left results essentially unchanged (Appendix F).
- **Per-source attribution (narrative only):** human 0.89, Claude 0.77, GPT 0.73, Gemini 0.60, DeepSeek 0.57, Kimi 0.55 F1. Most confusions were between models, especially Gemini, DeepSeek and Kimi.

Important for honest use: raw-text classifiers were near-perfect, so the paper does not show that style stops mattering. Its claim is that narrative differences persist even when style is removed or edited.

## Core differences (Section 4.1, Table 16)

Human value first, then the average across the five models. Scale features are 1 to 5 means; percentages are the share of stories with that option.

**Higher in model-written stories**

| Feature | Human | Models |
| --- | --- | --- |
| Thematic explicitness and moralizing (1 to 5) | 3.28 | 3.94 |
| Moral or philosophical weighting (1 to 5) | 3.26 | 3.68 |
| Narrator comments on the theme | 52% | 77% |
| Dialogue used for philosophical debate | 34% | 59% |
| References are mostly implicit echoes | 50% | 72% |
| Emotion conveyed mainly through the body | 38% | 81% |
| Smell among the dominant senses | 57% | 82% |
| Setting mirrors inner states (1 to 5) | 3.58 | 4.07 |
| Continuity of a single causal chain (1 to 5) | 3.92 | 4.20 |
| Resolution driven by the protagonist's choice | 46% | 69% |
| No subplots | 57% | 79% |
| Resolved through internal understanding or acceptance | 27% | 47% |
| Central character introduced by external description | 30% | 52% |

**Higher in human-written stories**

| Feature | Human | Models |
| --- | --- | --- |
| Explicit, named references to other works | 47% | 24% |
| Balanced mix of explicit and implicit references | 37% | 16% |
| Emotion conveyed mainly through explicit labels | 29% | 8% |
| Protagonist's choices framed as morally mixed | 59% | 38% |
| Subplots that parallel the theme | 42% | 21% |
| Reinterpretation of earlier scenes after a surprise (1 to 5) | 3.28 | 2.95 |
| Chronological discontinuity (1 to 5) | 2.40 | 2.12 |
| Flashback and flash-forward intensity (1 to 5) | 2.58 | 2.31 |
| Fourth-wall breaking and direct reader address | higher | lower |

Gaps on the scale features run from about 0.2 to 0.65 points. The separation comes from many small differences combined, not from any single feature.

## Rarity (Section 5, Appendix H)

- Rarity was measured as a story's average distance to its 25 nearest neighbours in feature space, used as a proxy for originality.
- Mean rarity percentile: human 0.71, models 0.49 (Cohen's d 0.83).
- For a given prompt, the human story was the rarest of the six versions 57.8% of the time, against 16.7% expected by chance.
- 24.7% of human stories fell in the rarest tenth of the corpus, against 7.1% of model stories.
- Distributions overlap substantially, and model stories appear in every rarity tail. Rarity is not a quality measure.

## Model fingerprints (Section 5, Table 17)

Use only if the user asks; these describe five specific model versions and will date quickly.

- **Claude:** the flattest event escalation, the most uniform narrative voice, a conventional ("continuist") stance toward literary tradition (62% against 39% to 56% for others), more epilogues, few dream sequences, quiet endings.
- **GPT:** gossip and rumour as a plot device (64% against 44% to 55%), distant retrospective narration, ensemble casts, more subverted expectations (41% against 27% to 36%), ambiguous reconciliations.
- **Gemini:** the tidiest endings, long denouements, bleak settings (88% tagged bleak or oppressive), characters introduced by external description.
- **DeepSeek:** front-loads crucial context that others reveal later.
- **Kimi:** the fewest fingerprints; sits at the generic centre of the model cluster, with in-medias-res openings and characters introduced in action.

## Limits to state when relevant

- English short fiction of about 5,000 words, by published authors. Not emails, essays, resumes or other nonfiction.
- Five specific model versions from 2025 to 2026; model behaviour changes.
- Features were assigned by a language model and checked on a small human sample.
- Group-level tendencies with overlapping distributions; no single story can be judged by them.
- The paper measures separability and rarity, not quality or reader preference.
- The sentence-level tiers in SKILL.md section 5 are not from this paper.

## Inconsistencies in the paper itself

Mention these rather than repeat a figure that may be wrong.

- **Fourth-wall breaking and reader address:** Section 4.1 describes them as "67% vs. 39%" and "28% vs. 7%", but Table 16 lists the same numbers as means on an ordinal scale (0.67 vs. 0.39; 0.28 vs. 0.07). Say only that human stories did both more often.
- **Dimension names:** Section 2.1 lists Structure among the ten dimensions, while the tables and ablations use Situatedness in that slot.
- **Core feature count:** "30 core features" appear as 33 rows in Tables 14 to 16 because three features contribute one model-leaning option and one human-leaning option. Both counts are consistent once this is understood.
- **Fingerprint count:** 75 fingerprint features are stated; the per-source counts given in the appendix (human 32, Claude 26, GPT 11, Gemini 11, DeepSeek 7, Kimi 3) sum to more. Quote the per-source counts only with that caveat.
- **Test-set size:** Section 3 gives 1,377 prompts (8,262 stories); Appendix D gives 1,384 prompts (8,301 stories).
