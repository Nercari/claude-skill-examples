# Client reply in your voice: a Claude skill

Sample deliverable for a "custom Claude skill" gig. The business is fictional: **Velocrank Cycle Works Bike Repair**, owner Dana Whitfield. All names and prices are invented.

## The problem

A small-business owner answers the same kinds of messages every day: price questions, delays, complaints, jobs they have to decline. Typing each one takes minutes. Generic AI replies sound corporate, and worse, they invent prices, hours and promises the owner never made.

## The skill

`SKILL.md` teaches Claude to take two things, the customer's message and the owner's rough notes, and return a reply that:

- sounds like the owner (warm, short, first-name, no corporate phrases);
- uses only facts from the notes, and shows `[CONFIRM: ...]` where a fact is missing instead of guessing;
- puts the answer or the bad news first, then one clear next step;
- does not promise refunds or admit fault unless the notes say so.

Drop the folder into `.claude/skills/shop-reply/` (or upload it as a skill) and paste a message with notes.

## Two examples

Outputs below were **written by following the skill, not a live model run**. Each case folder in `examples/` holds `input.md`, `expected.md` (the properties a good reply must have) and `output.md`.

### Example 1: price quote (`examples/01_price_quote`)

| Input | Output |
|---|---|
| **Customer (Sam):** hey, my back wheel is wobbly and the brakes squeal. how much to fix and how long? need it for commuting<br><br>**Notes:** wheel true $25, brake pads rear $18 + fit $15, total $58. can do thursday if dropped by wed eve. no appointment needed | Subject: Your wheel and brakes: $58, ready Thursday<br><br>Hi Sam,<br><br>It comes to $58 in total, and I can have it ready Thursday if you drop the bike off by Wednesday evening.<br><br>That's $25 to true the rear wheel, $18 for new rear brake pads and $15 to fit them. The squeal is usually worn pads, so that should sort it.<br><br>No appointment needed, just bring it in.<br><br>Dana<br>Velocrank Cycle Works Bike Repair |

### Example 2: missing information (`examples/04_missing_info`)

| Input | Output |
|---|---|
| **Customer (Lena):** Do you work on e-bikes? I have a hub motor one, front wheel puncture. Also what are your Saturday hours?<br><br>**Notes:** yes puncture on ebike ok, hub motor front wheel ok but takes longer, $30 + tube. saturdays - not sure for this month, check | Subject: Re: E-bike puncture<br><br>Hi Lena,<br><br>Yes, I work on e-bikes, and a front-wheel puncture on a hub motor is fine. It takes a bit longer than a normal wheel because of the motor, but I can do it.<br><br>The labour is $30, plus the cost of the tube.<br><br>Saturday hours: [CONFIRM: Saturday hours for this month]<br><br>Let me know when you'd like to bring it in.<br><br>Dana<br>Velocrank Cycle Works Bike Repair |

The other cases cover a delay (bad news first), a complaint (no refund promised), and a job the owner declines for safety.

## Verify

    python samples/s1_claude_skill/check.py

Checks the frontmatter, that all five examples have input, expected and output files, and that each output follows the skill's own rules (sign-off, length, subject line only for email, no emoji, no price that is not in the notes).

## Honest limits

- The check script tests the skill file and the hand-written examples. It does not prove how Claude will behave on your messages; try it on a few real ones and adjust the voice rules.
- The owner reads and sends every reply. The skill drafts; it does not send.
- Your version needs your real voice: I would start from 5 to 10 of your past replies.
