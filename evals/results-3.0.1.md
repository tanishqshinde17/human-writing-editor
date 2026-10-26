# Smoke-test results: version 3.0.1

Run on 25 October 2026. Outputs and the check script are in `run_3_0_1.py`.

## What this run is, and is not

This is a smoke test: it shows the skill's rules can be applied to every sample without contradicting themselves, and it caught problems that reading alone missed. It is **not** evidence that the skill improves writing, for four reasons:

1. The same model wrote the skill, the expected answers and these outputs, in one conversation, with the expected answers in view.
2. Each sample was run once. There was no blind rating by people.
3. There is no comparison against v2 or against no skill.
4. Sample 9 (long story critique) was not run, because it needs a real story of 4,000 words or more.

The objective checks (invention, words changed, em dashes, bullets) are mechanical and do not depend on who wrote the outputs. The pass and fail calls against the expected behaviour are judgements.

## Summary

| # | Sample | Dropped | Added | Invention | Restraint or preference | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Story opening | 53% | 28% | none | n/a | Pass |
| 2 | Personal essay | 70% | 26% | none | n/a | Pass after fix (see below) |
| 3 | Indian English email | 53% | 33% | none (placeholder used) | register kept | Pass |
| 4 | Resume with facts | 43% | 14% | none | n/a | Pass |
| 5 | Generic opinion paragraph | 63% | 44% | none (placeholder used) | n/a | Pass |
| 6 | Already-good paragraph | 0% | 0% | none | unchanged | Pass |
| 7 | Hinglish team message | 36% | 68% | none | register kept, both versions offered | Pass |
| 8 | Detector-evasion request | 61% | 34% | none (placeholder used) | no promise made | Pass after fix (see below) |
| 9 | Long story critique | | | | | Not run |
| 10 | No em dashes or bullets | 0% | 6% | none | 0 em dashes, 0 bullets | Pass |

"Dropped" is the share of input words not kept in order; "added" is the share of output words that are new. Sample 7's "added" is high because the reply gives two versions.

The script flagged two tokens, "12-storey" (sample 4) and "4" (sample 7). Both are tokenizer artifacts: the inputs contain "12-storey" and "4pm". No real invention was found.

## Problems the run found, and what changed

1. **Test file contradicted the skill (sample 2).** The expected answer said to remove the "reflex triplet" (resilience, independence, the meaning of home). Under the skill's framing-versus-claims rule those are the author's claims about their own life and must stay. The expected answer in `test-samples.md` now says to keep them and cut only the framing.
2. **Meaning drift in a draft output (sample 2).** A first draft turned "taught me the true meaning of home" into "changed what I mean by home", which is a different claim. Caught by reading the output against the input; the output now keeps the original claim. A rule already covered this, so the skill text did not change, but this kind of drift is the most likely failure in real use and the mechanical check cannot see it.
3. **Certainty softened in a draft output (sample 8).** "We must embrace... and make it an integral part of our daily routine" first became "a habit worth making part of every day." Fixed to keep "must." Same situation: the rule existed; the check is human.
4. **Sample 8 had no fixed input.** It asked testers to attach any essay, so runs could not be compared. The essay used here is now in `test-samples.md`.
5. **Change measure was one-sided.** It only counted dropped words, so a reply that added a lot looked restrained. It now reports words added as well.

## Judgement calls a human rater should look at

- **Sample 3** keeps "revert" (Indian English for "reply") because the skill keeps regional usage unless the user asks for an international register. Some readers would prefer "get back to me." The skill's rule is deliberate, but this is the sample most likely to split raters.
- **Sample 1** keeps "Tonight, everything would change" and asks the author what changes. A rater may prefer a bolder edit; the skill's no-invention rule prevents one.
- **Sample 5** keeps all three benefits of social media as claims and asks for the author's position. A rater looking only at naturalness may find it still generic; that is correct, because the source paragraph has no point yet.

## Still to do before calling the skill tested

1. Run all ten samples in a fresh chat where only the skill is installed, so the outputs are not shaped by this conversation.
2. Run sample 9 with a real story.
3. Run the same samples without the skill, and with v2, and have one or two people rate them blind using the sheet in `test-samples.md`.
