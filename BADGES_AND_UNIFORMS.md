# BADGES AND UNIFORMS

> **Status:** Design reference. Everything marked **[CANON]** is already established elsewhere and is cited. Everything marked **[PROPOSAL]** is new, pending author approval. Nothing here overrides canon.
> **Visual reference page:** `.bob/artifacts/ics-rigged-sphere-badges-uniforms-reference.html` (earlier pass; this file supersedes its open questions).
> **Sources:** → See: Doc 2.46 (Badge Technical Specification), `PROGRESSION.md`, `UI_MENUS.md`, `ART_DIRECTION.md`, Doc 2.32 (Brand Identity), Doc 2.33 (Onboarding Packet), `enemies/PTKW-Security-Division.md`, `characters/EOD.md`, Docs 2.47 and 2.48 (host-force insignia).

---

## 0. Rules this file obeys

1. **Tier direction:** Tier 3 = new arrivals, Tier 1 = senior staff. The game starts on a Tier 2 badge. [CANON, HANDOFF ruling 17]
2. **Standard employees wear no uniform.** The badge is the only marker (BES: visible uniforms raise anxiety and cut compliance scores by 7%). [CANON]
3. **Shape language:** rounded corners, warm materials, no sharp angles, no gore, no firearms. Applies to everything the player sees on Levels 1–6. [CANON, `ART_DIRECTION.md`]
4. **The badge is the character sheet.** Every visual difference between badges must be readable in under a second at chest height, in first person. [CANON, `PROGRESSION.md`]
5. **PTKW and Board marks are never ICS marks.** The PTKW badge carries no ICS logo. The Board has no logo. [CANON]

### Real-world references used

| Reference | What it informs |
|---|---|
| ISO/IEC 7810 ID-1 (CR80): 85.60 × 53.98 mm, corner radius ≈ 3 mm, 0.76 mm thick | Card size and corner radius. The brand rule "rounded, no sharp angle" matches the standard. |
| Corporate/government photo-ID practice: photo top-left, name/ID block under it, role band, lanyard at chest height | Field layout, readability at distance |
| Colour-coded lanyards and card header bands (visitor / staff / contractor / escort-required) | Why the tier is readable by header colour alone |
| Security-hologram features: guilloché, microtext, layered foil, covert laser marks | Anti-forgery detail on the PTKW and Director badges |
| Heraldic rule of tincture (no colour on colour, no metal on metal) | Contrast rule for the lettering colours below. Gold, silver and platinum sit on blue, which is correct. Grey with white lettering is the deliberate exception and reads as "unfinished". |

---

## 1. Shared badge anatomy

### 1.1 Card (front) [CANON fields, PROPOSAL placement]

Hard plastic card, 85.6 × 54 mm, 3 mm radius, worn at chest height on a lanyard. [CANON: Doc 2.46, 2.33]

```
┌────────────────────────────────────────────┐
│ ICS EARTH BRANCH                     ( o ) │  ← header band + EIMU recess (top right)
│ ┌────────┐  EMPLOYEE — TIER 2              │
│ │ photo  │  Asset No.   E-05682            │
│ │        │  Department  Research & Learning│
│ └────────┘  Supervisor  E-05091            │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        [ QR ]  │  ← tier stripe + QR
└────────────────────────────────────────────┘
```

| Element | Spec |
|---|---|
| Header band | Top 9 mm. Wordmark in rounded sans-serif, the ouroboros without a serpent at left. [CANON, Doc 2.32] |
| Photo | Left, 22 × 28 mm, rounded 2 mm. A **placeholder grey silhouette** until the player's photo is taken in the Day-1 flow. |
| EIMU recess | Circular, 8 mm, top right, slightly darker than the card. Described to new arrivals as a "design accent". [CANON] |
| Text block | Right of the photo. Four lines: tier title, asset number, department, supervisor E-#. [CANON fields] |
| Tier stripe | **[PROPOSAL]** 4 mm stripe across the bottom in the lettering colour (gold / silver / platinum). Lets the tier read when the card is edge-on or half-covered by a hand. |
| QR code | Bottom right. [CANON] |
| Back | Magnetic strip, asset number again in small type, return-to-HR line, the 12-digit **badge generation code**. [CANON strip; the code is a PROPOSAL] |

### 1.2 EIMU recess states (gameplay readout) [PROPOSAL]

The recess is the only part of the badge that changes with game state.

| State | Look | Meaning |
|---|---|---|
| Normal | Dark, matt | Standard monitoring |
| Elevated | A faint warm ring, visible only when the badge is held close | Double sensitivity zone (Tier 1 in BES locations) |
| Gap | Fully dark, no ring, cool to the touch | Badge off-body for more than 4 minutes. A gap-log entry is created. |
| Stripped | **Identical to Normal.** | Sensor leads cut. Visually undetectable by design. Detectable only by housing-seal inspection. [CANON, Doc 2.46 §2] |

The stripped badge must never look different. The player's knowledge is the only difference.

### 1.3 Lanyard and holder [PROPOSAL]

- Lanyard: flat woven ICS Deep Blue, small repeating wordmark, breakaway clip.
- The metal keychain disc from the onboarding packet has two rings; one holds the lanyard. [CANON, Doc 2.33 item 6]
- The brushed-metal badge holder with the Earth Branch logo is a purchasable item at 8 SOLCRED. [CANON, `facility/TV_SCREENS.md` line 130]
- A holder never hides the header band. A holder that covers the EIMU recess is a Gap-state risk (see 1.2) and is the one cosmetic with a mechanical consequence.

---

## 2. The standard employee tiers

### 2.1 Colour table [CANON, `PROGRESSION.md` authoritative]

| Tier | Card | Lettering / stripe | Hex | Reach |
|---|---|---|---|---|
| **Tier 3** (new arrival) | ICS Deep Blue | Gold | `#1A2E52` / `#C9A84C` | Levels 1–4, cafeteria, gym, Wellness Hub |
| **Tier 2** (game start) | ICS Deep Blue | Silver | `#1A2E52` / `#B8BEC7` [PROPOSAL hex] | Levels 1–6, Research Division, SOLCRED premium canteen |
| **Tier 1** (senior) | Midnight Blue [PROPOSAL `#0F1B33`] | Platinum [PROPOSAL `#E4E6EB`] | `#0F1B33` / `#E4E6EB` | Levels 1–7, PTKW-adjacent corridors (read only), Level 5 east perimeter (secondary auth), Transit observation. EIMU doubled in BES locations. |

Gold → silver → platinum is a read-down of increasing coolness. The more senior the badge, the colder it looks. This is deliberate and not stated in canon. **[PROPOSAL]** It supports the game's arc (Phase 1 warmth, Phase 4 chill) and is the one thing an observant player can notice before being told.

### 2.2 Department variants [PROPOSAL]

The card colour never changes with department. Only a **small department glyph** next to the department line does, so no one reads rank from department.

| Department | Glyph (rounded, single-line) | Notes |
|---|---|---|
| Research & Learning | Open circle with a dot | Player, Omar. Behavioral Data Analysis adds a second dot. |
| Operations | Two interlocked rings | Marcus, James |
| Communications | Open speech curve | Darius |
| HR & Wellness | Simple heart-leaf | Sera, Amara. The only glyph with a plant motif; matches Wellness Hub branding. |
| Cleaning & Maintenance | Wide circle with a flat base | Tarek, Rania |
| Transit | Chevron-free arc | Observation access only |

### 2.3 Per-character badge sheet [CANON data, PROPOSAL where marked]

| Character | Asset No. | Department | Tier | Supervisor | Badge notes |
|---|---|---|---|---|---|
| Kai, "The Variable" (player) | E-05682 | Research & Learning (Behavioral Data Analysis) | 2 | E-05091 (Omar) [PROPOSAL, check Omar canon] | Photo is the player. Tier stripe silver. Wear marks accrue visibly across phases. [PROPOSAL] |
| Marcus | E-02847 | Operations | 2 | E-00219 | Lanyard worn short, badge flipped over when off shift. |
| James | E-00219 | Operations Lead | 2 | — | Holder purchased. Corners show wear. |
| Darius | E-01899 | Communications | 2 | — | Badge clipped to a pocket instead of the lanyard. |
| Omar | E-05091 | Research & Learning (Senior Analyst) | 2 | — | Name line has a second printed title "Senior Analyst". |
| Sera Vasquez | E-04788 | HR & Wellness | 3 | — | Gold stripe. Sticker on the back (Wellness Hub loyalty mark). |
| Amara Diallo | E-01205 | HR & Wellness | 3 | — | Same as Sera; the badge is cleaner and newer. |
| Tarek Mansour | E-03388 | Cleaning Supervisor, L1–4 | 3 | — | Faded gold lettering; lanyard replaced with a cord. |
| Rania Odhiambo | E-04421 | Cleaning, night shift | 3 | — | Badge carries a night-shift dot **[PROPOSAL]**: small white dot beside the tier title. |
| Yusra | E-01573 | Former Research & Learning, terminated | 2 | — | One of the 847 undeactivated badges, if the story uses it. Shows only as a prop. |

Note: Tier 3 for HR staff and cleaning supervisors is canon. It implies a long-serving employee can still carry the "new arrival" colour; the badge colour tracks access, not time served.

---

## 3. Non-standard badges

### 3.1 PTKW-Clearance badge [CANON properties, PROPOSAL design]

CANON: grey card, white lettering, **no ICS logo**, raw Interplanetary Governance Seal, maximum EIMU, transmits to Level 8, issued by PTKW Engineering and logged separately.

**[PROPOSAL] design:**
- Card: matt grey `#6E7480`, no gradient, no header band. A flat, unfinished look. Corner radius is the same ISO 3 mm, so it is still a rounded object. That keeps rule 3 true even for the cold badge.
- Lettering: white, **monospace** or default system sans (never the ICS rounded wordmark).
- **Governance Seal:** a plain circle, 14 mm, printed top right where the EIMU recess would be on a standard badge. It sits **in the same place** so the eye recognises the swap. Seal contents: a small sphere above a horizontal line (the "rigged sphere", resting on a baseline), ringed by microtext reading `INTERPLANETARY GOVERNANCE · LABOR · COMPLIANCE ·` repeated. Rendered as a hologram foil: the sphere shifts from grey to silver with the angle of the card. (Anti-forgery features: guilloché border, microtext, layered foil. Real-world basis in section 0.)
- No photo. A code instead: `PTKW-` + a 4-letter analyst tag (K-7, K-12, TOR-9, VAH-3 as in the comms). **The absence of a face is the point.**
- Back: no magnetic strip. A short-range contact pad (gold, circular) and the line `NOT AN EMPLOYEE CREDENTIAL`.
- Lanyard: plain grey, no wordmark.

The seal appears on **nothing else** but PTKW paperwork and badges, so seeing it in a place it shouldn't be is a story beat.

### 3.2 Branch Director badge [CANON properties, PROPOSAL details]

CANON: standard Deep Blue, platinum lettering, **thin gold stripe across the bottom**. One exists. Maren Voss leaves it on her desk on Day 22.

**[PROPOSAL]:** the card is the Tier 1 card (Midnight Blue is *not* used; it is Deep Blue as canon says) with a 1.5 mm gold stripe replacing the 4 mm tier stripe. A tiny embossed number "1" sits where the QR would be, in place of a QR code (the reader reads the magnetic strip only). Lanyard: same woven Deep Blue as everyone else. **Maren wears it exactly like everyone else.** That sameness is the whole message.

### 3.3 Stripped badge [CANON]

Externally identical to the standard badge. See 1.2.

### 3.4 Reclassified (847) badges [CANON]

Visually normal. Prop rule: found badges show an asset number but the photo placeholder is **sun-faded**; the player's eye should catch that the face is gone. **[PROPOSAL]**

### 3.5 Visitor / Regional (K. Brant) [PROPOSAL, gap in canon]

K. Brant, Regional Sector Lead, is not a branch employee. Badge: Deep Blue like the Director, **no gold stripe**, header reads `ICS REGIONAL` instead of `ICS EARTH BRANCH`, tier line reads `ESCORT: NONE`. A reminder that Regional outranks the Branch but is not above PTKW.

---

## 4. Uniforms and attire

### 4.1 Standard employees [CANON: none]

No uniform. Business-casual civilian clothing carried from Earth, replaced over time by issue pieces from the staff shop (the "work uniform" mentioned in `STORY.md` and Doc 2.36). **[PROPOSAL]** The issue pieces are neutral and warm: oatmeal, sand, soft navy. No logos. The only thing that identifies an employee is the badge.

### 4.2 Player attire [PROPOSAL]

| Phase | Look |
|---|---|
| 1 | Own clothes from Earth, plain, one jacket |
| 2–3 | Issue cardigan or overshirt added, sleeves rolled |
| 4 | Same clothes, creased, a stain at the cuff. Badge now has visible wear. |
| 5–6 | Unchanged. The player does **not** change into a costume. No tactical outfit; the arc is that Kai is still an employee at the end. |

### 4.3 Cleaning and maintenance [CANON: uniform pockets; PROPOSAL look]

- Soft grey-green coverall or smock. Warm, rounded collar, no hard seams.
- Large front pockets (the "uniform pockets" of canon), used as the player's hiding-spot for found items when the player takes this disguise.
- Name tag is **the badge itself**, not a separate one.
- Rania's night-shift variant adds a reflective strip on the sleeve. Tarek's has a pin: a small ouroboros without a serpent (the only decorative thing on the cleaning staff).

### 4.4 PTKW Security Division [CANON]

Modified ICS senior-management attire with a **grey identification band on the left sleeve**; no rank insignia; tools carried in an innocuous ICS equipment bag (CRD-7, collapsible AMB-3 25 → 60 cm). Named: ICS-SEC-4 ("Four", Level 4 lead), ICS-SEC-7 ("Seven", overnight Level 7).

**[PROPOSAL] details:**
- Suit/blazer in a quieter blue than the Director's, slightly too well-fitted.
- Band: 45 mm wide, matt grey `#6E7480`, no text, one **single stitched circle** (the seal reduced to a ring). On the left sleeve only.
- Footwear: soft-soled. The sound of the guard's footsteps is part of the audio design (→ See: `AUDIO_VOICE.md`).
- Badge: the PTKW-Clearance badge (3.1) worn in the same chest position as an employee badge.
- Equipment bag: an ordinary ICS tote with the wordmark. Nothing visible suggests tools.

### 4.5 EOD [CANON]

Looks human; tall (over 2 m), thin "the way a tool is thin". Wears a **modified version of standard ICS senior-management attire, cut wrong**: too clean, no creases at the knee. **No badge, no insignia, no access card.** Never a close-up or full face in Phases 2–4.

**[PROPOSAL] details:**
- Charcoal, not the ICS blue. The only member of the cast who is not in the brand palette.
- Cloth does not wrinkle or move quite like fabric: no sway of the hem when he stops.
- Collar sits flat against the neck at all times.
- Hands always visible, gloved in a thin matte material, never gesturing.
- **The missing badge is the visible feature.** The chest position where the lanyard hangs is empty, with no lanyard line on the shirt. Player recognition cue: *no lanyard, no badge, no sound*.
- EOD has no EIMU field: the player's own EIMU stress readout does not register him. (→ See: `EOD_ENCOUNTERS.md`)

### 4.6 HQ Omega-1 and IOS staff [CANON: unspecified]

- Omega-1: **never seen** by the player. Leave attire undefined in all player-facing material. The absence is the horror. [CANON, `HQ-Response-Protocol.md`]
- IOS staff (Levels 11–14): non-human, not hostile. **[PROPOSAL]** They wear no clothes the player recognises as clothes: simple draped panels in the same grey as the PTKW band, reading as ceremony rather than uniform. Open to author decision.

### 4.7 Branch Director, Maren Voss [PROPOSAL]

Tailored charcoal-navy suit, gold lapel pin of the ouroboros without a serpent, same badge as everyone (3.2). Phase 6: a cardigan, the AIDEN plush on the desk, no badge. The badge on the desk on Day 22 is the visual of her resignation.

### 4.8 True Believers / Arrangement Class [PROPOSAL]

Human employees, standard attire. One shared marker: a thin **white cord** worn in place of the lanyard. Only visible once the player knows to look for it.

---

## 5. Host-force insignia [CANON proposals in Docs 2.47 and 2.48]

Not repeated here. Both are marked [PROPOSAL] in their own documents; this file adds only art constraints.

- **Harrow:** black field, silver spike harrow, gold ring, open-hook chain link, left sleeve, tabs in Blue/Red/Green/Black/White/Amber. Motto AGAIN TOMORROW. Rounded points on the harrow: the spike is a stylised tine with a blunted tip, to respect rule 3 on Levels 1–6.
- **Gyrfalcon Wing:** azure field, white gyrfalcon over a gold ring, motto SIX MINUTES, pilot's wings with laurel, squadron patches Longwatch/Whiteout/Lantern.

---

## 6. Visual readability chart

What the player can tell from three metres away, at chest height:

| Person | Visible tell |
|---|---|
| New arrival | Gold stripe |
| Standard employee | Silver stripe |
| Senior | Almost black card, platinum stripe |
| Director | Same as senior, plus 1.5 mm gold line |
| PTKW analyst | Grey flat card, no colour, no face |
| PTKW guard | Grey left sleeve band |
| EOD | Nothing at the chest |
| Omega-1 | Nothing: not seen |

---

## 7. Canon fixes made with this file

1. **Doc 2.46 §3:** the matrix had Tier 1 and Tier 3 inverted against `PROGRESSION.md`. Rows swapped and relabelled. The table header lists 5 columns and now every row has 5.
2. **Doc 2.33 Item 2:** retitled from "Tier 1" to "Tier 3 Employee Badge" (new arrival).
3. **Still open (not fixed):** Doc 2.33 Item 2 access line reads "Levels 1–4, 6 (work areas only)" while `PROGRESSION.md` says Levels 1–4 for Tier 3. Needs an author ruling on whether Level 6 work-area access is intentional. Doc 2.46 §3 says Tier 2 access Levels 1–6 and its "Restricted Access" column lists Level 5 for both; also unreviewed.

---

## 8. Open rulings for the author

1. Is the **Midnight Blue / platinum** Tier 1 card (this file) acceptable, or should Tier 1 simply be Deep Blue with a brighter stripe?
2. Should the **PTKW Governance Seal** be the sphere-on-a-baseline mark proposed in 3.1, or something else? It is the single most reusable symbol in the game.
3. Do we show the **department glyphs** (2.2), or does the department stay text only?
4. **EOD's charcoal** colour: confirm it is allowed to break the brand palette.
5. **Maren's no-badge Phase 6** vs. her keeping it: the Day 22 desk scene depends on this.
6. **IOS staff attire:** draped panels, or leave unspecified.
7. Do **True Believers** get the white cord (4.8), or should they be unmarked?

→ See: `ART_DIRECTION.md` (open question 4, PTKW palette), `PROGRESSION.md`, `UI_MENUS.md`, `HANDOFF_CARTOGRAPHER.md`.
