---
description: Produce a Facebook caption + matching social card for a fact-check entry, in the house scorecard format (headline-first, verdict-consistent), with the length and em-dash checks baked in.
---

# /social-post

Generate a ready-to-post **caption + card** for a published fact-check (or a set of them, for a roundup). The argument is the entry slug/path, or a short description of what the post is about. If nothing is provided, ask.

This command exists so social posts start from the canonical format instead of being reinvented. It sits on top of the card toolkit (`social-media/lib/card.py`) and the post-format rules in `CLAUDE.md` ("Roundup / multi-claim post format") and the `social-post-scorecard-format` memory.

## Steps

1. **Anchor to the published entry(ies).** Read the frontmatter of each entry involved and record its **exact `verdict:`**. The post's verdict labels **must match** the published entry — never upgrade "Misleading" to "False" for punch (this is the whole credibility pitch and pre-publish failure mode #6 territory). If the post quotes the subject, confirm the quote's author is verified (mode #6) before using it.

2. **Draft the caption in the scorecard format:**
   - **Headline first** — the takeaway in one line (e.g., "128 fact-checks. His claims held up as accurate 4 times.").
   - **Then scannable triplets** — one block per claim/item:
     ```
     CLAIM: <his quoted words, or the donor+amount for a follow-the-money post>
     VERDICT: <label matching the entry>   (or "THEN:" for donor -> action)
     <one sentence of the documented reality>
     ```
   - **Framing precision:** "held up as accurate N times," not "X% completely accurate." For donor/pattern posts, keep the "documented sequence, not proof of a deal" line.
   - **Close** with "don't take our word for it, check his own votes and words" + the full URL.
   - Style: no em dashes; arrow bullets where useful; specific figures; cross-aisle tone.

3. **Run the two hard checks:**
   ```bash
   wc -m <<< "$CAPTION"                 # must be <= 2200 (FB limit); trim if over
   grep -F "—" <<< "$CAPTION" && echo "EM DASH — fix" || echo "no em dashes"
   ```

4. **Build the matching card** on the toolkit:
   ```python
   import sys; sys.path.insert(0, "social-media")
   from lib.card import Card, NAVY, RED, GREEN, GOLD
   c = Card()                       # scale=2 or 3 for supersampled/pie cards
   c.brand_bar()
   y = c.badge(64, "<PUBLISHED VERDICT>")
   y = c.title(y, "<short headline>")
   ...                              # panels / bullets / kicker per the content
   c.footer_bar()
   c.save("social-media/<slug>_card.png", to_desktop=True)
   ```
   `save()` auto-rejects em dashes in rendered text and drops a Desktop copy. Keep the card scannable — the caption carries the detail; the card carries the punch.

5. **Card audit (required, before committing).** Read the actual rendered PNG (not just the script) and check it against the two strongest house precedents — `beagle_count_contrast_card.png` (30 vs. 0) and `shared_earmarks_card.png` (54%/46% split bar + $17.7M/$14.9M). Both lead with one **big glanceable number**, not paragraphs. Verify:
   - **Stat-first, not quote-dense.** Is there one number, percentage, or two-word contrast a reader gets in ~2 seconds without reading a full sentence? If the card's main content is quote panels or prose blocks with no hero stat, that's a fail — find the number in the entry (a count, a dollar gap, a day-count, a percentage) and redesign around it; demote the quotes to short supporting snippets underneath.
   - **No dead space.** Look at the gap between the last content block and the footer bar. A large empty gray band means spacing wasn't distributed — enlarge panels/gaps proportionally (see the two Chautauqua-card iterations in git history for the before/after) rather than leaving it.
   - **Color logic.** Red/green (or red/navy) panels signal an adversarial contrast (claim vs. reality); plain navy-outlined panels signal parallel/chronological items (same thing said twice). Gold is for the verdict-reinforcing callout, not a primary panel color.
   - **Verdict badge and every rendered figure match the published entry** (re-check against the frontmatter, not memory).
   If any check fails, revise and re-render before moving to step 6 — don't present or commit a card that hasn't passed this pass.

6. **Commit** the card script + PNG and the post `.md` (house practice), EXCEPT do **not** commit third-party/AP-copyrighted photos or composites built from them (milestone/photo cards stay on the Desktop only). Then present the caption (with its character count) and the card image to the user.

## Guardrails
- Verdict labels match the published entry, always.
- No em dashes in rendered card text or caption body (the toolkit enforces the card; grep the caption).
- Caption <= 2200 characters.
- Quotes attributed to a named person need confirmed authorship (failure mode #6).
- Every card passes the Step 5 audit (stat-first, no dead space, correct color logic) before it's committed or shown to the user.
- Present, don't auto-post — the user posts to Facebook themselves.
