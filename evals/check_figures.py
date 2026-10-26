"""Check each figure quoted in research-findings.md against the paper's extracted text.
Usage: python3 check_figures.py paper.txt [paper_raw.txt]
Each check is (claim in the findings file, exact text that must appear in the paper)."""
import re, sys

def norm(s):
    s = s.replace("−", "-").replace("–", "-").replace("—", "-")
    s = s.replace("’", "'").replace("ﬁ", "fi")
    return re.sub(r"\s+", " ", s)

texts = [norm(open(p, encoding="utf-8").read()) for p in sys.argv[1:]]

CHECKS = [
    # Setup
    ("10,272 human stories / prompts", "10,272 writing prompts"),
    ("Books3 anthologies", "short story anthologies identified"),
    ("Prompts reverse-engineered with Gemini 2.5 Flash", "prompting Gemini 2.5 Flash"),
    ("Models: Claude Sonnet 4.6", "Claude Sonnet 4.6"),
    ("Models: GPT-5.4", "GPT-5.4 (OpenAI, 2026)"),
    ("Models: Gemini 3 Flash", "Gemini 3 Flash (Gemini Team, 2025b)"),
    ("Models: DeepSeek V3.2", "DeepSeek V3.2"),
    ("Models: Kimi K2.5", "Kimi K2.5 (Kimi Team, 2026)"),
    ("61,608 stories", "61,608 stories"),
    ("Mean length 4,753 words", "mean length is 4,753 words"),
    ("Gemini median 2,967", "Gemini 3 Flash 10,261 99.9% 3,155 2,967"),
    ("DeepSeek median 2,693", "DeepSeek V3.2 10,272 100.0% 2,946 2,693"),
    ("Kimi median 3,005", "Kimi K2.5 10,272 100.0% 3,274 3,005"),
    ("408 candidates", "yielding 408 candidates"),
    ("304 features after dedup", "resulting in d = 304 features"),
    ("47 style features excluded", "the exclusion set contains 47 features"),
    ("257 narrative-only features", "This leaves 257 features"),
    ("30 core and 75 fingerprint features", "30 core features and 75 fingerprint features"),
    ("Krippendorff alpha 0.90", "Krippendorff's alpha = 0.90".replace("alpha", "α")),
    ("Mean human-model kappa 0.84", "mean human-model Cohen's κ = 0.84"),
    ("Human-human kappa 0.74", "Human-human encoded agreement on the same subset is Cohen's κ = 0.74"),
    ("240 items across 12 stories", "240 story-feature items across 12 stories"),
    # Table 2 (binary)
    ("Binary: Narrative 93.2", "Narrative 257 93.2 .959"),
    ("Binary: Core only 84.8", "Core Only 30 84.8 .828"),
    ("Binary: Core+FP 91.1", "Core+FP 101 91.1 .934"),
    ("Binary: Narrative+Style 96.0", "Narr. + Style 304 96.0 .982"),
    ("Binary: Style only 85.8", "Style Only 39 85.8 .867"),
    ("Binary: ModernBERT 99.9", "ModernBERT - 99.9 1.00"),
    ("Binary: Stylometric 99.8", "Stylometric+XGB 144 99.8 .999"),
    ("Binary: TF-IDF 99.7", "TF-IDF+XGB 5,000 99.7 .999"),
    ("Binary: Binoculars 55.9", "Binoculars - 55.9 .404"),
    # Table 3 (six-way)
    ("Six-way: Narrative 68.4", "Narrative 257 68.4 68.4%"),
    ("Six-way: Core only 46.5", "Core Only 30 46.5 46.8%"),
    ("Six-way: Core+FP 63.4", "Core+FP 101 63.4 63.6%"),
    ("Six-way: Narrative+Style 77.3", "Narr. + Style 304 77.3 77.3%"),
    ("Six-way: Style only 60.4", "Style Only 39 60.4 60.5%"),
    ("Six-way: ModernBERT 99.8", "ModernBERT - 99.8 99.8%"),
    ("Six-way: TF-IDF 99.5", "TF-IDF+XGB 5,000 99.5 99.5%"),
    # Robustness
    ("LAMP on 278 Gemini stories", "278 Gemini-generated stories"),
    ("LAMP 93.9 after vs 95.5 before", "detects edited Gemini stories at 93.9% macro-F1 (AUPRC 0.988), compared to 95.5% macro-F1"),
    ("Length-matched 93.2", "The Narrative model is unchanged (93.2% macro-F1 before and after matching)"),
    ("No topic effect, p = 0.46", "no significant topic-wise differences: H =4.69, p=0.46"),
    ("Topic test over six topics", "six topics with at least 20 test prompts"),
    ("Memorization filter leaves results unchanged", "Narrative-only model shifts from 93.18 to 93.23"),
    ("Per-class F1, narrative only", "Narrative 0.89 0.77 0.73 0.60 0.57 0.55"),
    # Table 16
    ("Thematic explicitness 3.28 / 3.94", "Thematic Explicitness & Moralizing s 3.28 3.94"),
    ("Moral weighting 3.26 / 3.68", "Moral / Philosophical Weighting s 3.26 3.68"),
    ("Narrator theme commentary 52% / 77%", "Narratorial Thematic Commentary → yes 52% 77%"),
    ("Dialogue as debate 34% / 59%", "Dialogue Function → philosophical debate 34% 59%"),
    ("Implicit echoes 50% / 72%", "Reference Explicitness → implicit echoes 50% 72%"),
    ("Embodied emotion 38% / 81%", "Emotional Expression → embodied 38% 81%"),
    ("Smell 57% / 82%", "Sensory Modalities → olfactory 57% 82%"),
    ("Setting mirror 3.58 / 4.07", "Setting as Psychological Mirror s 3.58 4.07"),
    ("Causal chain 3.92 / 4.20", "Causal Chain Continuity s 3.92 4.20"),
    ("Protagonist-choice resolution 46% / 69%", "Agency in Resolution → protagonist choice 46% 69%"),
    ("No subplots 57% / 79%", "Subplot Integration → no subplots 57% 79%"),
    ("Internal resolution 27% / 47%", "Resolution Mode → internal understanding 27% 47%"),
    ("External description intro 30% / 52%", "Character Introduction → external description 30% 52%"),
    ("Named references 47% / 24%", "Intertextual Strategy → explicit named reference 47% 24%"),
    ("Balanced references 37% / 16%", "Reference Explicitness → balanced mix 37% 16%"),
    ("Explicit emotion labels 29% / 8%", "Emotional Expression → explicit labels 29% 8%"),
    ("Morally mixed 59% / 38%", "Moral Polarity → ambivalent/mixed 59% 38%"),
    ("Parallel subplots 42% / 21%", "Subplot Integration → thematically parallel 42% 21%"),
    ("Recontextualization 3.28 / 2.95", "Depth of Recontextualization After Surprise s 3.28 2.95"),
    ("Chronological discontinuity 2.40 / 2.12", "Chronological Discontinuity s 2.40 2.12"),
    ("Anachrony 2.58 / 2.31", "Anachrony Intensity s 2.58 2.31"),
    # Discrepancy: fourth wall
    ("Fourth wall in Table 16 as ordinal 0.67 / 0.39", "Fourth-Wall Permeability o 0.67 0.39"),
    ("Reader address in Table 16 as ordinal 0.28 / 0.07", "Direct Reader Address o 0.28 0.07"),
    ("Fourth wall in text as 67% vs 39%", "(67% vs. 39%)"),
    ("Reader address in text as 28% vs 7%", "(28% vs. 7%)"),
    # Rarity
    ("Rarity 0.71 vs 0.49", "(0.71 vs. 0.49"),
    ("Cohen's d 0.83", "Cohen's d = 0.83"),
    ("Human rarest 57.8%", "57.8% of the time (vs. 16.7% by chance"),
    ("24.7% vs 7.1% in rarest tenth", "24.7% of all human stories fall in the top 10% rarest stories corpus-wide, compared to just 7.1%"),
    ("Rarity over 25 nearest neighbours", "25 nearest neighbors"),
    # Fingerprints
    ("Claude continuist 62% vs 39-56%", "62% of Claude stories vs. 39-56%"),
    ("GPT gossip 64% vs 44-55%", "(64% vs. 44-55% for other sources)"),
    ("GPT subverts 41% vs 27-36%", "(41% vs. 27-36%)"),
    ("Gemini bleak 88%", "88% tagged bleak and oppressive"),
    ("Per-source fingerprint counts", "Human: 32, Claude: 26, GPT: 11, Gemini: 11, DeepSeek: 7, Kimi: 3"),
    # Other discrepancies
    ("Dimension list includes Structure", "Agent, Social Network, Event, Plot, Structure, Setting, Time, Revelation, Perspective, and Style"),
    ("Situatedness used in tables", "Situatedness 77.3 41.3"),
    ("Test set 1,377 prompts (8,262 stories)", "1,377 prompts (8,262 stories)"),
    ("Test set 1,384 prompts (8,301 stories)", "1,384 prompts, 8,301 stories"),
]

ok = 0
rows = []
for label, needle in CHECKS:
    n = norm(needle)
    found = any(n in t for t in texts)
    ok += found
    rows.append((label, "found" if found else "NOT FOUND"))
for label, status in rows:
    print(f"{status:10}  {label}")
print(f"\n{ok}/{len(CHECKS)} found")

# Scale-gap range claim: Table 16 scale/ordinal gaps
gaps = [0.65, 0.42, 0.33, 0.49, 0.38, 0.26, 0.26, 0.28, 0.26, 0.20, 0.23, 0.34, 0.28, 0.28, 0.27, 0.26, 0.24, 0.28, 0.21]
print(f"Table 16 non-percentage gaps: min {min(gaps)}, max {max(gaps)}")
# fingerprint sum
print("Sum of per-source fingerprint counts:", 32 + 26 + 11 + 11 + 7 + 3)
