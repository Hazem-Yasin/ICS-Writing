# ICS: Interplanetary Corporate Solutions
## Health & Survival System Design

*This document covers how the player takes damage, survives, and heals in ICS: Interplanetary Corporate Solutions. The system must be consistent with who the player is (a human data analyst, not a soldier), what the world is (a corporate facility, not a battlefield), and what the horror is (a system that was designed to keep you compliant, not to kill you).*

---

## Design Principle: The Facility Was Not Designed to Hurt You

ICS Earth Branch was built to make employees productive, comfortable, and compliant. The physical environment was engineered to the highest safety standards. Every sharp edge is rounded. Every corridor is well-lit. Every fall hazard has a railing.

The horror is not that the facility hurts you. The horror is that the people in it do — and that the facility's own systems, turned against their purpose, can too.

This means damage in ICS: Interplanetary Corporate Solutions is always caused by one of three things:
1. **Other people** — PTKW security, EOD's effects, Omega-1 assets
2. **Modified or misused ICS equipment** — the player is not the only one who understands what a CRD-7R does
3. **Infrastructure failure** — steam lines, pressurized conduits, the cold of Level 0, falling through a maintenance crawl space

There are no environmental hazards that ICS designed to be hazards. Everything that can hurt the player was designed to do something else.

---

## The Health Representation: The Badge Vitals Display

The player's health is displayed on the back face of their badge — visible when the player looks down at the lanyard, or when it appears in the corner of the screen in HUD mode.

The badge already contains the EIMU biometric sensor. The reverse face of Tier 2 and above badges has a small status display — four indicators, each a tiny LED strip — that shows the player's current biometric condition as reported by the sensor. This was designed by ICS for wellness monitoring and manager check-ins; the manager can request a live badge status from any employee.

The player's four health indicators:

**Physical Integrity** — injuries, blood loss, CRD-7 exposure, structural damage. Depletes with direct damage. The LED strip is green → amber → red → dark.

**Neurological Status** — CRD-7/ACS-9 exposure effects. Separate track because compliance tool damage affects the nervous system differently from physical damage. High CRD-7 exposure without recovery produces movement impairment — fine motor control degrades (affecting tool use and modification), not gross motor control.

**Thermal Regulation** — exposure to Level 0 cold, steam line proximity, environmental extremes. Degrades gradually in cold environments without intervention. At critical levels: tunnel vision, slowed movement, decision-making impairment (the UI begins presenting fewer choice options, a deliberate design choice — the player experiencing hypothermia literally has fewer apparent paths).

**EIMU Coherence** — the system's read of the player's emotional state. Not a health meter in the conventional sense — a visibility meter. High EIMU Coherence means the facility's monitoring system has a strong read on the player. Low Coherence (achieved through badge stripping, EIMU-Jammer use, or being in unmonitored zones) means the player is effectively invisible to the monitoring layer. This track doesn't deplete from damage — it responds to player behavior.

**Why this design works:** The badge vitals display is already in the world. It's already explained. The player learns about it through Document 2.33 (EIMU sensor in the badge) and Document 2.46 (technical spec). When they understand the badge is monitoring them, and then see the health display is on the badge, the progression horror lands harder — even your health bar is ICS infrastructure.

---

## Damage Sources

### Direct Physical Damage (Physical Integrity track)

**CRD-7 contact (standard):** Significant Physical Integrity drain, significant Neurological Status drain. Recovery time: 3–5 minutes without intervention.

**CRD-7R contact (modified — 75V):** Near-lethal single hit on Physical Integrity. Neurological Status critical. Recovery without intervention: 15+ minutes, during which fine motor control is severely degraded.

**AMB-3 strike:** Moderate Physical Integrity drain per hit. Multiple hits in sequence are lethal. The AMB-3F (hardened steel face) escalates this to potentially lethal on critical hits.

**Fragment Launcher (BAR-FL) hit:** High single-hit Physical Integrity damage at close range. Lower at range. No Neurological effect.

**EOD — direct contact:** Not modeled as a health event. If EOD reaches the player in Phase 2–4, it is a game-over state regardless of health. He does not fight the player. He collects them. Health doesn't matter. Only avoidance does.

**Omega-1 contact:** Not survivable. If the player is in the facility when Omega-1 arrives and is exposed, game over. The 22-hour window exists precisely to ensure this does not happen.

### Environmental Damage

**Level 0 cold (Thermal Regulation track):** -1 pip per 90 seconds of exposure without insulation. The player can find a maintenance jacket in Level 0's supply recess — it slows but doesn't stop the decline. The warm air from Rania's hatch stops cold damage the moment the player reaches it.

**Steam line release (Physical Integrity — brief burst):** The 8-second steam dispersal from valve 2-J-7 at close range causes moderate Physical Integrity damage. At the valve itself: significant. Used as a weapon on enemies at the right range.

**Fall damage:** The maintenance crawlways are navigable but narrow. A fall in the Type B passages (half-height, navigable but low) causes minor Physical Integrity damage. No fall damage in standard corridors — ICS designed the railings to work.

**ACS-9 extended exposure (Neurological Status track):** Sustained 18 Hz infrasound at Position 2–3 at close range degrades Neurological Status. This is how the ACS-9 functions against the player if they're caught in their own deployment — the peripheral visual disturbance begins affecting the player's HUD (subtle UI flicker at mild levels, partial UI blackout at severe).

---

## Healing: What Exists in a Corporate Facility

The player does not find medkits in lockers. This is a corporate office building in space. What it has is what a corporate office building has.

### Medical Centre (Level 3) — Full Restore
The Branch Medical Centre operates 24 hours a day. Free at the point of use. If the player can reach it without being caught, it restores all four tracks to full. 

The catch: it requires badge access and logs every visit. A visit to the Medical Centre generates an EIMU Coherence increase (the facility now knows exactly where you are and what your physical state was). In Phase 3 and beyond, it also triggers an automatic PWRP flag — *"Asset E-05682 accessed Medical Centre outside standard hours, Physical Integrity degraded."*

The Medical Centre is the most effective healing location and the most dangerous to use.

### Wellness Hub (Level 4) — Neurological / Thermal restore
The Wellness Hub has a rest suite — climate-controlled, designed for employees experiencing stress or exhaustion. Restores Neurological Status and Thermal Regulation completely. Partial Physical Integrity restore (the Wellness Hub treats stress, not injuries — but the body heals faster at rest).

Same catch as Medical Centre: logged, flagged above a certain Phase.

### Personal Quarters (Level 3) — Slow full restore over time
The player's residential unit is the safest healing location. All four tracks restore over time while the player is in their quarters — slowly, but without any monitoring flag. In Phase 1 (confined to quarters), this is the primary healing mechanic. In later phases, getting back to quarters requires navigating the maintenance network, which costs time and exposure.

### Rania's Hatch Crawlway (Level 0 → Level 1) — Thermal restore
The warm air from the water main above the crawlway stops Level 0 cold damage and slowly restores Thermal Regulation during the approximately 4-minute transit. This is the only "passive" healing location in the game — it heals while the player moves.

### ICS Medical Supplies (found — limited)
The Medical Centre storage has supplies the player can take: wound seals, neurological stabilizers (originally for CRD-7 welfare use — counteract the Neurological track depletion), thermal warming patches. Limited quantity. Not restockable after Phase 3 when the Medical Centre goes to restricted access.

### SOLCRED Canteen — Wellness items
Before Phase 3, the Canteen sells physical wellness products for SOLCRED. Over-the-counter pain relief, electrolyte supplements, warming drinks. Low-level Physical Integrity and Thermal Regulation restore. Cheap. Plentiful. Completely normal to buy. Does not trigger a flag.

---

## Death States

**Standard death** — Physical Integrity reaches zero. The screen goes to black. A single line appears: the player's asset number, and the ICS reclassification language: *"Productive capacity fully realized. Asset status updated to Schedule D completion."* Then the last autosave loads.

**CRD-7R overexposure death** — same screen, different line: *"Neurological failure. Asset Wellness record updated."* The clinical language is the horror.

**EOD capture** — not death. A specific cutscene: EOD collects the player. The game cuts to black, then to a PTKW reclassification document for E-05682, dated, signed. Then to the last autosave. The message is: you were not killed. You were processed.

**Omega-1 exposure / window closed** — the run-ending death state. If the player has not escaped the facility before Omega-1 arrives, or is caught by an Omega-1 asset, the screen shows the current time in the 22-hour countdown, the number of Phase 6 actions completed, and a single note: *"The 22-hour window closed."* The game then loads the latest Phase 6 autosave, or the permanent *"Day [X] — Last Entry"* save if none exists (see design/SAVE_SYSTEM.md). The 22-hour clock is restored to the value stored in that save, not reset.

This is the harshest death state, but it is not a permanent loss: Phase 6 is replayable from the state the player built. It exists to make the 22-hour window real, because the clock does not stop for a reload. *(Ruling: reconciled with design/SAVE_SYSTEM.md and design/ENEMY_AI.md, which both return the player to a save.)*

---

*→ See: design/PROGRESSION.md — the badge vitals display sits on the same physical object as the tier progression system.*
*→ See: canon/weapons/compliance/CRD-7 and CRD-7R — the primary combat damage source.*
*→ See: story/scene-notes/Level 0.md — the cold of Level 0 and the Thermal Regulation track.*
