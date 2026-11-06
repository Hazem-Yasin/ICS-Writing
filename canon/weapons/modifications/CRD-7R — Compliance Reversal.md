# CRD-7R — Compliance Reversal
*Base Tool: CRD-7 (Compliance Restraint Device) | Category: Lethalization | Junction: B | Available: Phase 3*

---

## What You Start With

The CRD-7 delivers a targeted electromagnetic pulse at up to 40 volts — calibrated to interrupt voluntary motor nerve signals without damaging the nervous system. The 40-volt ceiling is a hard limit: a safety capacitor in the discharge circuit bleeds off any charge above 40V before it reaches the prongs. The PTKW manual describes this as a "non-damage threshold" — meaning ICS engineers tested what voltage causes permanent nerve damage and built in a ceiling at the last safe point.

They wrote down the unsafe point to establish the safe point. That number is in the document.

---

## Components Required

**1. The CRD-7 itself.** Already in the player's inventory.

**2. Safety capacitor bypass — sourced from:** The Level 5 electrical maintenance cabinet, Junction D. The cabinet contains spare components for facility electrical systems, including bypass capacitors used during maintenance procedures when a system needs to run outside its normal operating range for testing. The specific component is a 75V ceramic capacitor, part number ICS-EL-47, stored in a small plastic tray in the third drawer. There are twelve of them.

**3. Copper wire wrap — sourced from:** The wire spool in the Level 1 junction room (Junction B). 22-gauge copper wire, used for basic electrical maintenance. A 30cm length is sufficient.

**4. Heatshrink tubing — sourced from:** Any maintenance tool cart. The hydraulic work cart at Junction A has a roll. Needed to insulate the modified discharge circuit so it doesn't arc to the casing.

---

## The Modification Process

**Junction required:** B (the Level 1 junction room workbench — needs the vice clamp to hold the CRD-7 housing open while working).

The CRD-7 housing opens at the handle base with a quarter-turn release — designed for battery replacement. Inside: the battery, the charge circuit, the safety capacitor, and the discharge relay. The safety capacitor is a small blue cylinder with two leads soldered to the main circuit board. It is labeled, in ICS component notation, "ICS-C-40V-SAFE." The label is accurate.

Remove the ICS-C-40V-SAFE. Replace it with the ICS-EL-47 from the Level 5 cabinet — which is rated for 75V and will not bleed off the charge the way the original does. Rewire the discharge relay directly to the battery positive without the intervening bleed circuit. Insulate with the heatshrink.

The modification takes approximately 35 minutes. The main challenge is the soldering — the Level 1 junction room does not have a soldering iron, so the player uses the heat gun from the Junction A tool cart, brought to Junction B, which provides enough heat for the solder joints but requires care to avoid damaging adjacent components.

---

## What You End Up With

The CRD-7R looks mostly the same as the CRD-7. The housing is closed, the prongs are the same, the charge indicator still works. The heatshrink on the discharge circuit is visible through the battery access port if you look — a small detail that would flag on close inspection but doesn't affect the external appearance significantly.

The difference is entirely in the output.

The CRD-7R delivers up to 75 volts through the prongs or directed-field emitter. At that voltage, the pulse does not simply interrupt motor nerve signals — it damages them. Contact application at 75V produces:

- Immediate full-body convulsive response (not simply loss of voluntary motion — involuntary full-muscle contraction)
- Loss of consciousness: 3–8 seconds post-contact in most subjects
- Recovery time: 8–15 minutes to partial motor function, 30–45 minutes to full function
- Residual neurological effects: fine motor impairment for 2–6 hours post-exposure; in subjects with prior cardiac history, risk of arrhythmia

At maximum repeated use — multiple contacts on the same subject — the CRD-7R can cause permanent nerve damage.

**The directed-field emitter at 75V (≤3m range):** This is the lethal configuration. The PTKW manual's Tier 2 description of the directed-field mode notes that "at range, the electromagnetic field disperses and reduces in intensity." At 40V with dispersal, the range effect is reduced but non-damaging. At 75V with dispersal, the concentrated core of the field — at direct line-of-sight within 1.5 meters — delivers approximately 55–60V equivalent to the target. This is above the cardiac fibrillation threshold for a human adult under stress. At this range, directed-field use of the CRD-7R is potentially lethal.

The charge indicator on the CRD-7R glows differently after modification: where the original glows amber when charged, the CRD-7R glows a slightly brighter, warmer orange. It is a small difference. The player notices it before the first use.

---

## What It Means

The safety capacitor in the original CRD-7 was ICS-C-40V-SAFE. The engineers labeled it with its function. They were proud of it — or careful enough about it to name it clearly. The 40-volt ceiling was a design choice, not a limitation. They chose not to make it worse than it was.

The player removed that choice.

The CRD-7R is the first thing in the game that ICS specifically chose not to build, that the player built anyway. Everything before this was repurposing. This is inverting. The safety mechanism was the last thing standing between a compliance tool and something else.

The player took it out and held it in their hand and put something else in its place.

---

*→ See: canon/weapons/compliance/CRD-7 — Compliance Restraint Device — the base tool and its three knowledge tiers.*
*→ See: MODIFICATIONS.md — the junction system and modification principles.*
*→ See: Document 2.14 (Planetary Disciplinary Protocol) — the legal framework that, at the PTKW level, specifies exactly what these tools are authorized to do. The CRD-7R exceeds that authorization.*
