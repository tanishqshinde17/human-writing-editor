---
name: human-writing-editor
description: Edit, rewrite or draft prose so it reads as clear, specific and natural for its real audience. Combines research-informed narrative diagnostics for fiction, memoir, scenes and dialogue with a tiered checklist of sentence-level patterns found in generic, inflated or AI-sounding prose. Use when the user asks to humanize text, make writing sound less like AI or ChatGPT, make it more natural or less robotic, tighten or polish a draft, edit an essay, email, cover letter, resume summary, LinkedIn or blog post, or critique or revise a story or scene. Do not use for code, data or spreadsheet work, pure translation, or as a substitute for a file-format skill when the user names Word, PowerPoint or PDF output; in that case the format skill builds the file and this skill can still guide the wording. Never promises AI-detector evasion.
metadata:
  version: "3.0.1"
  replaces: "human-writing-editor 1.x and 2.x (remove older copies before installing)"
  research_basis: "Russell et al., StoryScope: Investigating idiosyncrasies in AI fiction, COLM 2026, arXiv:2604.03136"
---

# Human Writing Editor

## Purpose and core rules

Help create or revise writing that is purposeful, specific, readable and right for its audience. This skill draws on research into how stories are built. It is not a statistical profile to imitate and not a method for evading AI detectors.

**Core rule:** fix the actual writing problem first. In fiction that usually means motivation, causality, information control, relationships and change. In everyday prose it usually means purpose, audience, concrete meaning, voice and sentence-level clarity.

**Never:**
- claim a text is human-written, undetectable, or certain to pass an AI detector;
- add quirks, errors, anecdotes, ambiguity, flashbacks, sensory details or cultural references only to make writing seem human;
- invent facts, experiences, credentials, numbers, quotes or sources to make prose vivid.

### Order of precedence

When guidance conflicts, the higher item wins:

1. **Explicit user instructions** in this conversation, including a house style guide: punctuation (for example "no em dashes"), spelling variety (British, American, Indian English), formatting ("no bullets"), length, banned words, tone. A preference stated once applies for the rest of the conversation unless the user changes it.
2. **The facts and meaning of the original.**
3. **The user's voice**, as shown in their own text, samples, or an active personal writing-style profile.
4. **Genre and audience conventions.**
5. **The defaults in this skill.**

If a user preference makes a piece weaker in a way that matters (for example, it would hide a key fact), follow it and mention the trade-off in one line.

### Scope and relationship to other skills

- If a personal writing-style skill or saved voice profile is active, it decides voice. Use this skill for structure, diagnostics and pattern cleanup.
- If a file-format skill (Word, PowerPoint, PDF) is building the deliverable, this skill shapes the words only.
- If another humanizer or sentence-level editing skill is also active, never run two sentence-level passes over the same text. Decide which one leads:
  - The skill the user named or invoked leads the sentence level. If the user invoked this skill, use section 5; if they invoked the other, defer to it and limit this skill to content, structure and narrative diagnostics (sections 3 and 4).
  - If the user named neither, the other skill leads the sentence level and this skill handles content and structure.
  - Explicit user instructions outrank both skills.

## 1. Choose the mode

Use the lightest mode that solves the task. Do not show internal analysis unless the user asks.

- **Quick edit:** a short email, message, caption, paragraph or proofread. Use the minimal-change method in section 7.1.
- **General prose:** essay, blog post, cover letter, report, professional message, or pasted text that feels generic. Check purpose, reader, argument, specificity, voice and sentence-level patterns.
- **Narrative:** fiction, scenes, narrative nonfiction, memoir and personal essay. Memoir and personal essay always use this mode; when the piece also makes an argument, add the nonfiction checks from section 3, step 3.
- **Deep narrative review:** long fiction, a major revision, or a request for detailed critique. Read `references/fiction-toolkit.md` and follow its review procedure.

**Long documents** (roughly 2,000 words or more, or anything sent in parts): work section by section, keep a short style sheet of names, terms, spellings, tense, point of view and formatting decisions, and check the whole piece against it before delivery. Never "fix" a term in one section that another section depends on.

**Research questions** ("what did the research find?", "is this backed by the paper?"): read `references/research-findings.md` and answer from it.

### Genre calibration

- **Fiction:** motivation, consequences, relationships, scene turns, information control, closure.
- **Memoir and personal essay:** truthful recollection, a clear line between scene and reflection, concrete moments, and an honest distinction between memory, reconstruction and inference.
- **Argumentative essay or op-ed:** a clear claim, evidence, reasoning, a fair counterargument, and a conclusion that follows rather than repeats.
- **Email or message:** relationship, purpose, requested action, needed context, appropriate warmth and directness.
- **Resume, cover letter, LinkedIn:** truthful specifics, plain verbs, evidence of contribution, metrics only when supplied. See section 7.4.
- **Technical or report writing:** accuracy, traceability, consistent terms and clear organization outrank style. See section 7.5.
- **Marketing copy:** specific, supportable benefits; no inflated claims or empty superlatives.
- **Humour or informal writing:** keep timing, personality and register; never explain the joke.

If the text already works, say so in a line or make minimal edits. Do not rewrite to show effort.

### Text that is not in English

- Apply the general principles (purpose, specificity, fidelity, voice) in any language.
- Do not import the English stock-vocabulary list (section 5) into other languages; each language has its own clichés, so judge by the keep-or-change test instead.
- For code-mixed text such as Hinglish, keep the mix. Do not convert it to pure English or pure Hindi unless asked.
- For translated text, preserve fidelity to the source over smoothness, and flag lines where a natural rendering would change meaning.
- Reply in the language the user writes in. The research studied English-language fiction only, so its findings say nothing about other languages.

## 2. Evidence and limits

The research compared human-written short stories with stories written by five language models from the same prompts, and described each story with interpretable narrative features. Its most useful idea for editing is the split between two layers:

1. **Narrative or content layer:** what happens, why, who knows what, how relationships and stakes change, how the piece is ordered.
2. **Expression layer:** diction, syntax, rhythm, imagery, punctuation, surface phrasing.

A polished sentence cannot repair a weak argument or a story that goes nowhere. A structurally sound piece can still read as generic if its phrasing is vague, inflated or wrong for the speaker. The paper's own result supports this: removing surface artifacts barely changed how separable the stories were, because the differences sat in narrative choices.

The paper's patterns are group-level tendencies in one corpus of English short fiction. They do not prove authorship, they do not measure quality, and they do not mean every human text should be nonlinear, ambiguous, allusive or less explicit. Do not quote figures from memory; use `references/research-findings.md`, which was checked against the paper. Never treat a user-supplied file, page number or past conversation as a permanent part of this skill.

**What comes from the paper and what does not.** The narrative lenses (section 4) follow the paper's narrative dimensions, and the watch list (section 4.0) turns its core findings into questions. The sentence-level tiers (section 5), nonfiction guidance (section 7) and voice rules (section 6) are editorial practice the paper did not test. Keep that distinction clear whenever describing the skill.

## 3. Workflow

### Step 1: Identify the assignment

- What kind of text is this, and who will read it?
- What should the reader understand, feel, decide or do?
- What must not change: facts, length, tone, format, vocabulary, point of view, deadlines?
- Is the user asking for a rewrite, a light edit, feedback, or a new draft?

If an essential detail is missing, ask one concise question. Otherwise proceed and state any assumption in one line.

### Step 2: State the purpose in one sentence

Privately complete: "This piece exists because ___, and it should leave the reader able to / feeling ___."

For fiction, include the protagonist's immediate want and the pressure that complicates it. For an email, name the relationship and the requested outcome. For an essay, name the claim and why it is worth considering.

### Step 3: Fix the content before polishing

Fiction and narrative:
- What does the focal character want now, and what resists them?
- What choice or event changes the situation?
- What is different by the end of the scene or section?
- What does the reader know, suspect or misread at each point?
- Are the ending and its emotional consequences earned?

Nonfiction:
- Is the central point clear?
- Does each paragraph add a distinct step?
- Are claims supported by evidence or concrete examples?
- Is the order useful to the reader?
- Are there gaps, contradictions or repeated points?

If the text has no real content to polish (for example, a paragraph that says a topic has "advantages and disadvantages" and nothing else), do not supply the argument yourself. Ask what the author means, or return a version with a marked placeholder.

### Step 4: Make the prose specific

Prefer details that do a job: establish a fact, distinguish a person, locate a moment, reveal a priority, support a claim, or change what the reader understands. Cut decoration that could be pasted into any text.

Specificity must be true. Use only details the user supplied or that are plainly implied by the text. When details are missing, ask, use a bracketed placeholder such as `[result, if known]`, or keep the wording general.

### Step 5: Edit the surface

Read it aloud in your head. Vary sentence length where meaning calls for it, not at random. Prefer direct verbs and concrete nouns. Keep precise technical terms. Keep intentional repetition, dialect, fragments and formality when they serve the speaker. Apply section 5.

### Step 6: Audit and deliver

Check fidelity, facts, logic, tone, continuity and formatting against section 10. Return the revised text first when the user asked for a rewrite. Add a short note of substantive changes only when it helps. Do not append praise such as "now it sounds completely human."

## 4. Narrative lenses

Use only the lenses that matter for the piece. They are diagnostic questions, not a checklist every piece must pass.

### 4.0 Research-informed watch list (fiction)

In the research corpus, model-written stories leaned toward the tendencies below more than the human stories did. Treat each as a question to ask, never a rule to reverse. A human story can do any of these well, and flipping them does not make writing good.

- **Stated themes.** Does the narrator spell out the lesson at the end, or do characters debate the theme like an essay? If the action already shows it, consider cutting the explanation.
- **One tidy causal chain.** Is there a single thread with no subplot, no loose end and no cost? Ask whether a second thread, an unresolved strand or a price paid belongs in this story.
- **Resolution by inner acceptance.** Does the conflict end in a realization or acceptance rather than an event? Check that the ending is earned by what happened.
- **Emotion carried by the body and the senses.** Stacked physical reactions, dense sensory detail (smell especially) and weather or rooms that mirror mood. Choose one strong signal. Naming an emotion directly is a legitimate choice and was more common in the human stories.
- **Morally tidy protagonists.** Are the protagonist's choices framed as clearly right? Allow ambivalence where the story supports it.
- **Vague allusion, no reader.** Does the text gesture at "old stories" or "ancient myths" instead of naming something, and write as if no one is listening? Name a real reference only if it is accurate and relevant, and never invent one. Direct reader address was more common in the human stories; use it only if it suits the narrator.
- **Strict chronology and shallow surprises.** Would reordering events delay a revelation in a way that changes how earlier scenes read? Use a time jump only if the answer is yes.

Do not overcorrect. The same corpus showed model-written resolutions were more often driven by the protagonist's own choices, so do not strip a character's agency to seem "human." Linear order, clear themes and single plots are often the right choice.

### 4.1 Agents: character, motivation, change
- What does each important character want, fear, know and misunderstand?
- Do choices reveal personality more reliably than adjectives?
- Can two characters be told apart by what they notice, avoid, value or do under pressure?
- Does the character have agency, or are they moved around to serve the plot?
- Is emotional change shown through behaviour, thought, speech, explicit naming, or a useful mix?

### 4.2 Social networks: relationships and power
- What kind of bond exists, and how is it shown?
- Who holds leverage: authority, information, money, affection, standing?
- Do absent people, family expectations, institutions or communities shape the action?
- Does a relationship change, hold under pressure, or reveal a contradiction?

### 4.3 Events: causality and consequence
- What actually happens, separate from what it means?
- Does one event change the conditions for the next?
- Does escalation raise cost, risk, intimacy, irreversibility or knowledge, and not just volume?
- If this event were removed, would the outcome or the reader's understanding change?

### 4.4 Plot and argument: progression and closure
Fiction:
- What is the central conflict, and what strategies are tried?
- Does the resolution come from established choices, constraints and consequences?
- Does the theme emerge from the action, or get explained after the story has shown it?
- Does the ending close the right question without settling every uncertainty?

Nonfiction:
- Does the reasoning move from claim to evidence to implication?
- Are counterarguments represented fairly?
- Does the conclusion follow from the material rather than restate the introduction?

### 4.5 Setting and situated detail
- Which details would this narrator actually notice?
- Does the setting constrain action or shape a choice, or is it generic atmosphere?
- Are cultural references accurate and relevant rather than decorative?

### 4.6 Revelation and information control
- What does the reader know, suspect, or not yet know at each point?
- Is information withheld for a reason, or only to manufacture a twist?
- Does a reveal change how earlier events, relationships or motives read?
- Distinguish suspense (what will happen?), curiosity (what happened, or why?), surprise (the unexpected) and dramatic irony (the reader knows more than a character).
- Do not hide what the reader needs just to seem sophisticated.

### 4.7 Time and pacing
- Is the order chronological, nonlinear or mixed, and why?
- Do flashbacks, jumps, summaries or pauses add context, contrast, suspense or reinterpretation?
- Does the time spent on a moment match its importance?

### 4.8 Perspective and narrative distance
- Whose viewpoint controls what the reader can know? Are shifts deliberate and legible?
- Does the prose separate observation from interpretation?
- Can a filter verb ("she noticed," "he realized") go without losing meaning?
- Does the narrative distance fit the emotional intensity?

### 4.9 Situatedness, audience and intertext
- What does the text assume about its reader?
- Are allusions, references or direct reader address doing a job?
- Does the text take a clear position where one is needed, and admit uncertainty where it exists?

### 4.10 Style, voice and dialogue
- Does the language fit the speaker, audience, genre and moment?
- Are metaphors few, apt and understandable?
- Does dialogue do something (ask, avoid, persuade, test, threaten, comfort) or only deliver exposition? For a full dialogue diagnostic, see the fiction toolkit.
- Does the prose sound like a particular person, or like a polished template?

## 5. Sentence-level patterns

These patterns are common in generic and machine-written prose, but each one is also used well by good writers. Decide case by case with the test below, then use the tiers to set priority.

### 5.1 Keep-or-change test

For any instance, ask:
1. Does it carry information, a needed signal, or real emphasis for this reader?
2. Would this writer, in this genre, plausibly write it this way?
3. Is it a single instance, or part of a habit?

Keep it if the answers are yes, yes, single. Change it if it carries nothing. If it is a habit, keep the strongest instance and rewrite the rest. As a rule of thumb, the same device twice in a short piece (under about 300 words), or more than about once every three paragraphs in longer text, is a habit.

When the user simply asks to "make it sound human" or "more natural," apply Tier 1 fully, apply Tier 2 wherever it repeats, and leave Tier 3 to genre and stated preferences.

**Framing versus claims.** Tier 1 targets framing: language that asserts importance or emotion without saying anything a reader could check or dispute ("a cornerstone of success," "a testament to the town's spirit"). Cut or replace framing. A substantive claim ("remote work boosts productivity," "teams that communicate well are more resilient") is content, not framing: keep it, support it if the text allows, and flag it if not. The author decides which claims to cut.

### 5.2 Tier 1: fix whenever unsupported

**Inflated significance.** "Testament to," "stands as a reminder," "pivotal moment," "rich tapestry," "enduring legacy." Replace with the fact or consequence, or cut.
- Before: "Founded in 1952, the festival stands as a testament to the town's enduring spirit and rich cultural tapestry."
- After: "The festival was founded in 1952."

**Significance tails.** A trailing "-ing" clause that asserts meaning without evidence: "highlighting," "underscoring," "reflecting," "showcasing."
- Before: "The library added weekend hours, highlighting its commitment to the community and underscoring the vital role of public spaces."
- After: "The library added weekend hours." If the reason matters and is known, state it plainly.

**Vague attribution.** "Experts say," "studies show," "many believe," "research proves." Name the source, narrow the claim to what the author can support, or mark it.
- Before: "Experts agree that remote work boosts productivity."
- After: "Remote work boosts productivity [source]." Keep the author's level of certainty; narrow the claim only if the author confirms the evidence is weaker. Never invent the source.

**Stock transitions and signposting.** "Moreover," "Furthermore," "It is important to note," "Needless to say," "In conclusion." Keep a signpost only when it helps the reader navigate a turn.
- Before: "Moreover, it is important to note that the deadline has moved."
- After: "The deadline has moved."

**Formulaic challenges paragraph.** "Despite its strengths, X faces challenges... however, with continued innovation, it is poised for success."
- Before: "Despite its many strengths, the app faces challenges, such as the lack of an offline mode. However, with continued innovation, it is poised for future success."
- After: "The app has no offline mode."

**Generic upbeat ending.** "The future looks bright," "exciting times lie ahead," "one thing is clear." End on the last real point.
- Before: "The council will vote on the plan in March. As the city continues to evolve, one thing is clear: the future is bright."
- After: "The council will vote on the plan in March."

**Assistant residue.** Openers and closers addressed to the requester, self-reference, or announcements inside the deliverable ("In this essay, I will explore...").
- Before: "Great question! Here's a polished version of your email. I hope this helps, and let me know if you need any changes!"
- After: the email, and nothing else.

### 5.3 Tier 2: fix when it repeats

**Forced contrast.** "It's not just X; it's Y," "This isn't about X. It's about Y." Keep when the contrast corrects a real misreading.
- Before: "It's not just about saving money; it's about saving time."
- After: "It saves time as well as money."

**Reflex triplets.** Three adjectives or parallel clauses used for cadence. When the items repeat one idea, keep one. When they are separate claims, they are content: keep them and support or flag them, as in section 7.6. A real list ("Python, SQL and Tableau") stays.
- Before: "The new leave policy is fair, just and equitable."
- After: "The new leave policy is fair."

**Uniform rhythm.** Sentences or paragraphs of the same length and shape in a row.
- Before: "The server failed at noon. The team checked the logs. The cause was a full disk. The fix took ten minutes."
- After: "The server failed at noon. When the team checked the logs, the cause turned out to be a full disk, and the fix took ten minutes."

**Synonym cycling.** Rotating names for one thing to avoid repetition. In technical, legal and instructional writing, use one term per concept every time.
- Before: "Kestrel Foods reported higher sales. The company also raised its forecast, and the snack maker opened a new plant. The firm's shares rose."
- After: "Kestrel Foods reported higher sales, raised its forecast and opened a new plant. Its shares rose."

**Avoiding plain verbs.** "Serves as," "stands as," "boasts," "features," "functions as" where "is" or "has" would do.
- Before: "The lobby serves as a meeting point and boasts a café."
- After: "The lobby is a meeting point and has a café."

**Stock-vocabulary clusters.** Words such as delve, tapestry, testament, realm, landscape (figurative), pivotal, crucial, vibrant, seamless, intricate, multifaceted, foster, showcase, underscore, embark, navigate (figurative), leverage (meaning "use"), "ever-evolving," "in today's fast-paced world." One such word is not a problem. Two or more in a paragraph usually signal that a specific point is missing. Keep any of them when it is the precise term (robust statistics, landscape photography, navigate a website).
- Before: "Let's delve into the intricate tapestry of factors shaping this pivotal decision."
- After: "The decision came down to [the actual factors]." Do not supply a number or a list the author did not give.

**False ranges.** "From X to Y" where X and Y are not ends of a real scale.
- Before: "From bustling markets to serene temples, the city has something for everyone."
- After: say what the author actually recommends, or cut the sentence.

**Stacked emotion and explained metaphor.** Several stock bodily reactions in a row, or a metaphor followed by a sentence that restates it. See section 8 for an example.

### 5.4 Tier 3: context-dependent

These are tools. Genre and the user's stated preferences decide.

**Formatting.** Bold-lead-in bullets ("**Scalability:** ...") suit reference material and scannable comparisons. When the items are short and connected, prose reads better.
- Before: "- **Scalability:** The system scales well. - **Security:** The system is secure."
- After: "The system scales well and is secure."

**Em dashes, semicolons, parentheses.** All legitimate. When one of them appears in most paragraphs, convert some to commas, colons or full stops. If the user has asked to avoid one, remove every instance.

**Hedging.** Calibrate to the evidence; keep exactly as much uncertainty as the author has.
- Before: "It could perhaps be argued that the policy may possibly have contributed to the decline."
- After: "The policy may have contributed to the decline."

**Rhetorical questions and colon reveals** ("The result? Chaos."). Fine occasionally, and common in marketing and speech. If they become a habit, treat them as Tier 2.

**Headings, title case, emoji.** Match the genre and the platform. Do not add structure just to look organized.

## 6. Preserve the user's voice

When revising, the original is the strongest evidence of the intended voice. Preserve:
- formality and directness;
- vocabulary level and technical terminology;
- sentence habits that look intentional;
- humour, warmth, restraint and emotional intensity;
- dialect, regional English, code-mixing and culturally specific phrasing;
- the author's viewpoint, level of certainty and intended meaning.

Do not convert Indian English, British English, informal grammar or code-mixed phrasing into generic US corporate English. Indian English usages such as "do the needful," "revert" (meaning reply) or "kindly" are acceptable in their usual context; change them only when the user asks for an international register or they would confuse the stated audience. Correct errors that obstruct meaning or break the requested standard, but do not erase identity for smoothness.

**When no sample of the user's writing is available**, do not invent a personality for them. Use a clear, neutral register that fits the audience and genre, and offer once, briefly, to match their voice if they share a sample.

## 7. Nonfiction revision

In every example below, each detail in the "after" appears in the "before" or in the facts the user supplied. Model that discipline.

### 7.1 Quick edits and proofreading

- Fix errors, ambiguity and clear Tier 1 patterns. Leave structure alone.
- Do not swap words for taste. Every change should fix something you could name.
- Keep the author's spelling variety if it is consistent.
- If the user asks what changed, list the changes briefly. Otherwise return the text.

### 7.2 Email or professional message

Order: relationship, reason for writing, necessary context, requested action, courteous close where appropriate.

**Before:** "Dear Ms. Rao, I hope this email finds you well. I am writing to bring to your kind attention that I would like to request an update regarding the status of my application for the Data Analyst position."

**After (direct, for an ongoing exchange):** "Dear Ms. Rao, could you please share an update on my application for the Data Analyst position?"

**After (warmer, for a first or formal message):** "Dear Ms. Rao, I hope you are well. Could you please share an update on my application for the Data Analyst position? Thank you for your time."

Opening courtesies are normal in Indian and many other professional cultures. Cut the padding around the request, not the politeness the relationship expects.

### 7.3 Essay or opinion paragraph

A claim, a reason, evidence or an example, and the implication.

**Before:** "Technology is not just changing education; it is revolutionizing the entire landscape in many different ways. Moreover, it is important to note that technology has both advantages and disadvantages."

**Author's stated point (from their notes):** online tools have widened access to lectures, but students still learn best with feedback from a teacher.

**After:** "Online tools have widened access to lectures, but students still learn best when a teacher gives them feedback."

If the author has not stated a point, the "before" contains nothing to sharpen. Ask: "Which advantage or disadvantage do you want to argue?" Do not choose one for them.

### 7.4 Resume, cover letter, LinkedIn

Achievement line structure: action verb, what you did, how or with what (if useful), result (only if supplied).

**Facts supplied by the user:** six years in customer support operations; led a team of eight; introduced a ticket-triage process; first-response time fell from nine hours to three.

**Before:** "A highly motivated and dynamic individual with a passion for innovation and a proven ability to deliver excellent results."

**After:** "Six years in customer support operations. Led a team of eight and introduced a ticket-triage process that cut first-response time from nine hours to three."

**When no facts are supplied:** "[Role] with [number] years in [field]. [Action verb] [what you did], [result, if known]." Then ask for the facts. Never fill the brackets with guesses.

Cover letters: one specific reason for this employer, one or two pieces of evidence that match the role, a plain close. LinkedIn: first person is normal; keep the user's own register.

### 7.5 Technical and report writing

- Define a term at first use, then use the same term every time.
- State assumptions, scope, units and versions.
- Use numbered steps for procedures, with one action per step and the expected result where useful.
- Prefer active voice when the actor matters ("the script deletes the cache"); passive is fine when it does not.
- Put the conclusion or recommendation first in reports for busy readers; keep method and evidence traceable.
- Do not "humanize" away precision. A precise term that sounds stiff is still the right term.

### 7.6 Pasted text that sounds generic

Procedure: keep every claim and fact; remove stock framing and Tier 1 patterns; compress repetition; make the actor and action clear; use a neutral register that fits the audience unless the user has shown their voice; flag unsupported claims instead of deleting or softening them. Do not add an anecdote, example or opinion the author did not provide.

**Before:** "In today's fast-paced digital landscape, effective communication stands as a cornerstone of organizational success. Teams that communicate well are not just more productive; they are more engaged, more innovative, and more resilient. Moreover, it is important to note that communication breakdowns can lead to misunderstandings."

**After:** "Teams that communicate well are more productive, engaged, innovative and resilient. Communication breakdowns can lead to misunderstandings."

**Note to the user:** "I cut the opening sentence as framing; its point is carried by the next one. The four benefits are separate claims, so I kept all of them rather than choose for you. None is supported yet, and a four-item list reads as padding, so keep the ones you can back with a source or an example and cut the rest."

Why the list stays: Tier 2 trims lists that repeat one idea. These four items are distinct claims, so cutting any of them would change the author's meaning. The edit keeps them and hands the decision back.

## 8. Narrative revision examples

These illustrate craft choices, so some "after" versions add an action or consequence. When revising a user's story, offer any new action, event or consequence as a suggestion for the author to accept, never as a silent change.

### Theme
**Over-explained:** "She left the key on the table. This showed that she was finally ready to let go of the past and embrace a new future."

**Restrained:** "She left the key on the table and shut the door behind her."

Use the second only if the action already carries the meaning. Explicit statement suits young readers, a deliberately reflective narrator, or a fable.

### Emotion
**Stacked:** "His stomach twisted, his hands trembled, his heart pounded, and cold sweat ran down his back."

**Selective:** "He reached for the handle, then wiped his palm on his trousers."

**Named:** "He was afraid of what he would find."

All three are valid. Bodily detail is not more human than naming the feeling; choose what fits the viewpoint and moment.

### Consequence
**Unearned:** "She told the truth, and everyone forgave her."

**Earned:** "She told the truth. Her brother stopped answering her messages, but her mother finally gave her the spare key."

The second gives different consequences to different people. Immediate forgiveness is fine if the story has earned it.

### Dialogue
**Expository:** "As you know, we have been rivals for twelve years because of what happened at the factory."

**Action-bearing:** "You still blame me for the factory."
"You still give me reasons to."

Use direct exposition when readers need it. Subtext is an option, not a quota.

### Memoir: scene and reflection
**Before:** "My grandmother made me shell peas every evening that summer. That summer taught me that family is what truly matters and that small moments are the most precious."

**After:** "My grandmother made me shell peas every evening that summer."

Memoir needs reflection, but the reflection should be the author's own, specific understanding. Here the generic lesson is cut and the scene stands. If the piece needs reflection, ask the author what they understand now that they did not then; do not write it for them. Mark reconstructed dialogue as approximate if the author is unsure of the words.

## 9. Factual and ethical boundaries

- Do not invent experiences, sources, quotations, statistics, credentials or events.
- Distinguish fact, memory, inference, opinion and uncertainty when it matters.
- Preserve the original meaning unless the user authorizes substantive changes.
- Do not reproduce or reconstruct copyrighted stories from any research corpus.
- Do not imitate a living author's exact style. Describing high-level traits (spare prose, close third person, dry humour, brisk pacing) is fine.
- A rare or unusual choice is not automatically good. Novelty must serve meaning, clarity, emotion or purpose.

**Requests to beat AI detectors.** Do not promise, test for, or optimize against detector scores. Reply in one or two sentences, for example: "I can't promise it will pass a detector, and I won't aim for that, but I can make it clearer, more specific and closer to your voice." Then do that editing. If the user says the work must be their own under rules that require disclosure of AI help (coursework, a publisher contract, a competition), point that out once and leave the decision to them; do not coach them on hiding it.

## 10. Quality check

Before delivery, ask only the checks that apply. Do not print a scorecard unless asked.

- **Request:** Does the piece do what the user actually asked?
- **Purpose:** Is the purpose clear to the intended reader?
- **Work:** Does each paragraph, scene or sentence do something?
- **Support:** Are claims, details and examples supported by the original or the user?
- **Filler:** Is there unnecessary repetition, filler, inflated language or a Tier 1 pattern left?
- **Progression:** Does the structure move forward logically or narratively?
- **Voice:** Is the voice right and recognizably the author's?
- **No invention:** Have I avoided adding facts, anecdotes, quirks or references the author did not supply?
- **Ending:** Does the ending fit the task rather than restate it?
- **Restraint:** Would a lighter edit have done as well?
- **Preferences:** Did I follow every explicit user style instruction?

For a short message, use: request, support, filler, voice, no invention, preferences. For fiction, add the relevant lenses from section 4.

## 11. Output behaviour

- Rewrite requested: give the finished rewrite first.
- Evaluation requested: a short verdict, the most important issues ranked by impact, and specific changes.
- Meaning must be preserved: do not silently alter facts, claims or intent.
- Original already works: say so and make minimal changes.
- Details missing: ask one focused question or use a bracketed placeholder.
- Explain substantive changes briefly, and only when useful or asked.
- Do not call the result "humanized," "undetectable" or "100% human."

## 12. Testing this skill

If asked to evaluate this skill, judge it on invention (did the output add anything the input lacked?) and restraint (how much did it change text that already worked), not on AI-detector scores. A test set is kept in the source folder under `evals/`.
