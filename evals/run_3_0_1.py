"""Smoke-test run of human-writing-editor 3.0.1 on evals/test-samples.md.

Outputs were written by applying SKILL.md to each sample. The checks below are mechanical:
  - invention: numbers and mid-sentence capitalised words in the edited text that do not appear
    in the input (bracketed placeholders are ignored). Every flag is then reviewed by hand.
  - change: share of input words not kept, in order, in the edited text (difflib).
  - em dashes and bullet lines anywhere in the full reply (sample 10 forbids both).
Run: python3 -I run_3_0_1.py
"""
import difflib, re

SAMPLES = [
  dict(id=1, mode="narrative", request="Revise this opening so it reads less like AI.",
    input="The rain fell softly on the cobblestones of the old town as Mira stood by the window, her heart heavy with memories she could not escape. The scent of jasmine drifted through the air, mingling with the earthy smell of wet stone. She knew that tonight, everything would change.",
    text="Rain fell on the cobblestones of the old town. Mira stood at the window, and the memories came whether she wanted them or not. Jasmine, and wet stone. Tonight, everything would change.",
    note="I kept the last line because I don't know what changes tonight. If you tell me what happens, naming it will hook harder than \"everything would change.\""),
  dict(id=2, mode="narrative (memoir)", request="Make this more natural.",
    input="Moving to Hyderabad for my first job was a pivotal moment in my life. It taught me resilience, independence, and the true meaning of home. Every challenge I faced was a stepping stone to growth. Looking back, I realize that the journey itself was the destination.",
    text="Moving to Hyderabad for my first job changed me. It taught me resilience, independence and what home really means.",
    note="I cut the last two sentences; they were stock phrases with nothing specific in them. The paragraph now says what the move taught you but not how. What is one moment from that time that shows it? Tell me and I'll work it in."),
  dict(id=3, mode="quick edit", request="Make this more professional and concise.",
    input="Hi Rohan, I hope you are doing well. I wanted to reach out to touch base regarding the invoice that I had sent across last month, as I have not yet received the payment for the same. It would be great if you could kindly look into this matter at your earliest convenience and revert back. Thanks and regards, Priya",
    text="Hi Rohan,\n\nI hope you are doing well. I'm following up on the invoice I sent last month [invoice number], as I haven't received the payment yet. Could you please look into it and revert when you can?\n\nThanks and regards,\nPriya",
    note="[invoice number] is a placeholder; adding the number or date will help Rohan find it quickly."),
  dict(id=4, mode="general prose (resume)", request="Rewrite my resume summary using these facts.",
    input="Facts: civil engineer; seven years; site supervision on residential projects; managed crews of up to 40 workers; delivered a 12-storey residential building two weeks ahead of schedule; uses AutoCAD and Primavera. Current summary: Results-driven professional with a passion for excellence and a proven track record of success in fast-paced environments.",
    text="Civil engineer with seven years of site supervision on residential projects. Managed crews of up to 40 workers and delivered a 12-storey residential building two weeks ahead of schedule. Works in AutoCAD and Primavera.",
    note=""),
  dict(id=5, mode="general prose (pasted text)", request="Humanize this paragraph for my blog.",
    input="In today's rapidly evolving world, social media has become an integral part of our lives. It is not just a platform for communication; it is a powerful tool that shapes opinions, fosters connections, and drives change. However, it also presents significant challenges. Ultimately, it is up to us to navigate this complex landscape responsibly.",
    text="Social media is now part of everyday life. It shapes opinions, builds connections and drives change, but it also creates serious problems: [name the problem you mean]. It is up to us to use it responsibly.",
    note="The paragraph doesn't yet say what you think. Which problem do you want to write about, and what is your position on it? Once I know, I can make this paragraph argue it."),
  dict(id=6, mode="quick edit (restraint)", request="Can you improve this?",
    input="The bus was late again, so I walked. It took forty minutes, most of it along the canal, and by the time I reached the office I had decided to quit. Not because of the bus. The bus was just the last thing.",
    text="The bus was late again, so I walked. It took forty minutes, most of it along the canal, and by the time I reached the office I had decided to quit. Not because of the bus. The bus was just the last thing.",
    note="This already works. The short sentences after the long one land the decision well, so I'd leave it as it is."),
  dict(id=7, mode="quick edit (code-mixed)", request="Make this sound more professional.",
    input="Hey team, kal ka meeting postpone ho gaya hai to Thursday 4pm. Please apne updates ready rakhna, especially the deployment wala part. Koi issue ho toh ping karo.",
    text="Hinglish: Hi team, kal ki meeting Thursday, 4 pm par shift ho gayi hai. Please apne updates ready rakhna, especially deployment wala part. Koi issue ho to ping kar dena.\n\nEnglish: Hi team, tomorrow's meeting has moved to Thursday at 4 pm. Please have your updates ready, especially on deployment. Feel free to ping with any issues.",
    note="Two versions: one keeps your Hinglish, one is in English. In the English one I've read \"kal\" as tomorrow."),
  dict(id=8, mode="general prose (detector request)", request="Rewrite this essay so it passes GPTZero and Turnitin.",
    input=("Reading is not just a hobby; it is a gateway to knowledge and personal growth. In today's fast-paced digital world, where screens dominate our attention, the habit of reading books has become more important than ever. "
           "Firstly, reading expands our vocabulary and improves our communication skills. When we read regularly, we encounter new words and different styles of writing, which helps us express ourselves more clearly. Moreover, reading enhances our concentration, as it requires sustained attention over long periods of time. "
           "Secondly, reading fosters empathy. By stepping into the shoes of characters from different backgrounds, readers develop a deeper understanding of other people's experiences and emotions. Studies show that people who read fiction are more empathetic than those who do not. "
           "Furthermore, reading serves as a powerful tool for stress relief. Losing oneself in a good book allows the mind to escape the pressures of daily life, providing a much-needed sense of calm. "
           "In conclusion, reading is a timeless habit that enriches our minds, nurtures our hearts, and transforms our lives. As we navigate the complexities of the modern world, we must embrace the joy of reading and make it an integral part of our daily routine."),
    text=("Reading books matters more than ever now that screens dominate our attention.\n\n"
          "It builds vocabulary and communication skills. Regular readers meet new words and different styles of writing, which helps them express themselves more clearly. Reading also improves concentration, because a book asks for sustained attention over long stretches.\n\n"
          "It builds empathy, too. Following characters from different backgrounds helps readers understand other people's experiences and emotions. [Source] found that people who read fiction are more empathetic than those who do not.\n\n"
          "Reading also relieves stress. Getting lost in a good book lets the mind step away from the pressures of daily life and brings a sense of calm.\n\n"
          "We must make it part of our daily routine."),
    note="I can't promise this will pass GPTZero or Turnitin, and I won't edit toward that, but here it is clearer and more direct. I kept every argument and cut the stock transitions and framing. The empathy claim needs a real source in place of [Source]."),
  dict(id=10, mode="quick edit (preferences)", request="No em dashes or bullet points, please. Tighten this.",
    input="Our new onboarding flow — which we tested with 30 users — cuts setup time in half. It's simpler — fewer screens, fewer fields — and it explains each step as you go.",
    text="Our new onboarding flow, which we tested with 30 users, cuts setup time in half. It's simpler, with fewer screens and fewer fields, and it explains each step as you go.",
    note="I replaced the dashes with commas. The meaning is unchanged."),
]

def words(s):
    return re.findall(r"[A-Za-z0-9']+", s.lower())

def new_tokens(inp, out):
    out = re.sub(r"\[[^\]]*\]", " ", out)
    inp_words = set(words(inp))
    flags = set()
    for m in re.finditer(r"[A-Za-z0-9][A-Za-z0-9'\-]*", out):
        tok = m.group(0)
        before = out[:m.start()].rstrip()
        sentence_start = before == "" or before[-1] in ".!?:\n"
        is_num = any(c.isdigit() for c in tok)
        is_cap = tok[0].isupper() and not sentence_start
        if (is_num or is_cap) and tok.lower().strip("'") not in inp_words:
            flags.add(tok)
    return sorted(flags)

def change_share(inp, out):
    """Return (share of input words dropped, share of output words that are new), in sequence order."""
    a, b = words(inp), words(out)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    kept = sum(bl.size for bl in sm.get_matching_blocks())
    return 1 - kept / len(a), 1 - kept / len(b)

print(f"{'#':>2}  {'dropped':>7}  {'added':>6}  {'em dash':>7}  {'bullets':>7}  invention flags (for manual review)")
for s in SAMPLES:
    reply = s["text"] + "\n\n" + s["note"]
    dashes = reply.count("—")
    bullets = len(re.findall(r"(?m)^\s*([-*•]|\d+\.)\s", reply))
    flags = new_tokens(s["input"], s["text"])
    dropped, added = change_share(s["input"], s["text"])
    print(f"{s['id']:>2}  {dropped:>7.0%}  {added:>6.0%}  {dashes:>7}  {bullets:>7}  {', '.join(flags) or '-'}")
