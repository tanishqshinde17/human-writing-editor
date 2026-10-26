# Changelog: human-writing-editor

## 3.0.1

Fixes from the follow-up review of 3.0.0.

| Review item | What changed | Where |
| --- | --- | --- |
| 1. Untested | Ran nine of the ten samples with mechanical checks for invention, words dropped and added, em dashes and bullets. No invention found; the run exposed one contradiction between the test file and the skill and two fidelity slips in draft outputs, all fixed. This is a smoke test by the same model that wrote the skill, not a blind evaluation; the results file says so and lists what is still needed. | evals/results-3.0.1.md, evals/run_3_0_1.py |
| 2a. "Three factors" invented a number | Example now uses a placeholder and says not to supply a number or list. | SKILL.md 5.3 |
| 2b. 7.6 kept a four-item list its own Tier 2 rule would trim | Added a framing-versus-claims rule: framing is cut, substantive claims are kept and flagged, and the author decides which claims go. Tier 2 triplets now trim only lists that repeat one idea; the triplet example uses near-synonyms. The 7.6 note explains why the four claims stay. | SKILL.md 5.1, 5.3, 7.6 |
| 2c. Further slips found in the same scan | "Remote work can boost" softened the author's certainty; now keeps it. "The app still has" implied a duration; removed. | SKILL.md 5.2 |
| 3. Watch list duplicated in the toolkit | Toolkit section 8 now maps each watch-list question to a review pass instead of repeating it. Two details only the toolkit had (characters debating the theme, direct reader address) moved into SKILL.md 4.0. | references/fiction-toolkit.md 8, SKILL.md 4.0 |
| 4. Overlap rule could suppress another humanizer | Now states who wins: the skill the user named or invoked leads the sentence level; if neither was named, the other skill leads it and this one handles content and structure; user instructions outrank both. | SKILL.md purpose |
| 5. Size | Merged the research-relationship section into section 2 and shortened the testing section. Size is essentially unchanged; see the budget below. | SKILL.md |
| 6. Figures unverified | Every figure in the findings file was checked by script against the text of arXiv:2604.03136v6: 84 of 84 found. arXiv still lists v6 as current. The check corrected one loose phrase about the size of the gaps. | evals/figure-check.md, evals/check_figures.py |

**Size budget.** SKILL.md is 487 lines and about 5,800 words: roughly 43% more lines and 75% more words than v2. Cap it at 500 lines and 6,000 words. New material goes into `references/` unless it changes everyday (non-fiction or quick-edit) behaviour; anything added to SKILL.md should replace something of similar length.

## 3.0.0

Addresses every issue in the v2 evaluation report. Remove v1 and v2 before installing; v3 keeps the same name and replaces them.

| Report issue | Priority | What changed | Where |
| --- | --- | --- | --- |
| 6.1 Examples break the no-invention rule; resume example reads like one person's CV | High | Every "after" now uses only details in the "before" or in facts the user supplied. Neutral resume example with supplied facts plus a placeholder version. Essay example now shows the author's stated point, and says to ask when there is none. Email has a direct and a warmer version. Fiction examples carry a note that new events are offered as suggestions, not silent changes. | SKILL.md 7.2 to 7.6, 8 |
| 6.2 Sentence-level section hedged, untiered, incomplete | High | Keep-or-change test; three tiers (fix whenever unsupported, fix when repeated, context-dependent); a before and after for each pattern; default rule for bare "make it human" requests. Added significance tails, plain-verb avoidance, synonym cycling, formulaic challenges paragraphs, generic upbeat endings, bold-lead-in bullets, stock-vocabulary clusters and false ranges. | SKILL.md 5 |
| 6.3 Fiction depth cut too far | Medium | Restored deep-review procedure (passes A to G and a report format), scene card, four-question dialogue diagnostic, opening and ending checks, subgenre weighting, continuity sheet. Loaded only in deep review mode. | references/fiction-toolkit.md |
| 6.4 Research link mostly nominal | Medium | Restored a caveated watch list of the paper's core findings, framed as questions with an overcorrection warning. Added a findings file checked against arXiv v6 so research questions can be answered accurately, including the paper's own internal inconsistencies. | SKILL.md 4.0; references/research-findings.md |
| 6.5 Generic description, imprecise triggering | Medium | Description now lists trigger phrases and exclusions. New "scope and relationship to other skills" section. | Frontmatter; SKILL.md purpose |
| 6.6 No user-preference override; "restore a plausible voice" contradiction | Medium | Order of precedence puts explicit user style instructions first. Neutral register plus an offer to match a sample when no sample exists. | SKILL.md purpose, 6, 7.6 |
| 6.7 Same name, no changelog | Low | This file; `metadata.replaces` in the frontmatter. | CHANGELOG.md |
| 6.7 Evaluation without samples | Low | Ten sample texts with expected behaviour, failure signs, a rating sheet and trigger tests. | evals/test-samples.md |
| 6.7 No guidance for detector-evasion requests | Low | Short decline-the-framing response, then normal editing; one line on disclosure rules. | SKILL.md 9 |
| 6.7 No non-English guidance | Low | Section on other languages, code-mixed text and translations. | SKILL.md 1 |
| 6.7 Memoir in two modes | Low | Memoir and personal essay always use narrative mode, plus argument checks when needed. | SKILL.md 1 |
| 6.7 Fragile question numbering | Low | Quality checks are named; short-message subset listed by name. | SKILL.md 10 |
| 6.7 Long documents | Low | Section-by-section method with a style sheet. | SKILL.md 1 |
| Section 8 gaps (memoir, resume structure, technical writing, email tone, quick edits) | Low | Memoir scene-versus-reflection example; resume line structure; technical writing rules; two email registers; minimal-change method. | SKILL.md 7, 8 |

Other fixes not in the report:
- `version` was a top-level frontmatter key, which skill validation rejects. It now sits under `metadata`.
- The skill's own prose no longer uses em dashes, since models imitate the text of their instructions.
- Changelog moved out of SKILL.md so it is not loaded on every use.

Main file: about 480 lines. Reference files load on demand; `evals/` is not packaged.

## 2.0.0

Mode selection, genre calibration, sentence-level patterns, voice preservation, nonfiction examples, evaluation protocol. Removed hard-coded file references and unverified figures.

## 1.0.0

Initial StoryScope-based fiction skill.
