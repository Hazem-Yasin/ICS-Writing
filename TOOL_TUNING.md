# ICS — Rigged Sphere
## Tool Tuning — Numbers

*Every tool in this game already has a number somewhere: a charge count, a duration, a range, a build time. They live in six different files. This sheet puts them in one table, marks which are canon and which are placeholders, and sets the few numbers that no document has chosen yet.*

*The design argument: tools are tuned for tension, not for power. A charge count should make the player ask "is this worth it?" A duration should be long enough to act in and short enough to feel. EOD and Omega-1 are not tuned at all, because they are not balanced. They are fixed.*

---

## How to read this sheet

| Tag | Meaning |
|---|---|
| **Canon** | Already stated in an existing document. The source is named. |
| **[PROPOSAL]** | New. Needs sign-off and playtest data before it becomes canon. |

---

## 1. Base tools

| Tool | Slots | Uses | Effect and range | Source |
|---|---|---|---|---|
| **CRD-7** | 1 | 8 charges | Contact: 90 s incapacitation. Directed field ≤3 m: 40 s. Recovery for the target 90–180 s. | **Canon** — `INVENTORY.md`, `weapons/compliance/CRD-7 — Compliance Restraint Device.md` |
| **ACS-9** | 1 | 4 uses | 18 Hz "presence" field. About 8 m effective range. Position 3, 10+ minutes: lasting unease. | **Canon** — `INVENTORY.md`, `weapons/compliance/ACS-9 — Acoustic Compliance System.md`, `ACS-9D` file |
| **AMB-3** | 1 | 3 deployments, not recoverable | Atmospheric modifier | **Canon** — `INVENTORY.md` |
| **EIMU-Jammer** | 1 | Continuous; 8-minute battery | False EIMU signal | **Canon** — `INVENTORY.md` |
| **CCN-Spoofer** | 1 | 3 sessions before ID burn | Source: Level 8 network closet, Phase 4 | **Canon** — `INVENTORY.md` |
| **Maintenance Bar** | 1 | Unlimited | Pry; Tier 3 use on the Level 0 glyph panels | **Canon** |
| **Olfactory Canister** (OLF-04, 07, 11, 14) | 1 | 2 deployments | OLF-14: 8-minute effect, reaches EOD | **Canon** |
| **AIDEN Unit (improvised)** | 1 | 1 use | 2 m proximity; 30-minute review pause (Tier 2) | **Canon** |
| **Pressurized Pipe Tool** | 1 | 5 uses | Steam valve 2-J-7: 90 s window. Freight elevator stall: 12 minutes. | **Canon** |
| **EIMU Diagnostic Accessory** | 1 | Passive | Four-ring readout | **Canon** |

## 2. Modifications

| Mod | Base | Build time | Result | Source |
|---|---|---|---|---|
| **CRD-7X** (Extended Burst) | CRD-7 | 20 min | Range ≤7 m at 60% strength | **Canon** — `weapons/modifications/CRD-7X — Extended Burst.md` |
| **CRD-7R** (Compliance Reversal) | CRD-7 | ~35 min | 40 V and 75 V settings. Lethal under 1.5 m at 75 V. Target recovery 8–15 min partial, 30–45 min full. | **Canon** — `weapons/modifications/CRD-7R — Compliance Reversal.md` |
| **ACS-9D** (Directed Beam) | ACS-9 | **[PROPOSAL]** 25 min | 25° beam, 22 m (from about 8 m). | **Canon** for range |
| **ACS-9RS** (Resonance Shell) | ACS-9 | 50 min | Charge a space for 40–60 min; 90 s exposure to charge | **Canon** |
| **AMB-3F** (Fracture Baton) | AMB-3 | 40 min | 40-minute effect | **Canon** |
| **BAR-FL** (Fragment Launcher) | Bar + pipe | 60 min | One shot, 4–6 m, 3-minute reload | **Canon** |
| **ECT-4C** (Cascade Broadcast) | ECT-4 | 50 min | 4 m → 18 m radius, 40-minute broadcast | **Canon** |
| **Ignition Canister** | Olfactory | 45 min | 1.5 m cloud, 4–7 s | **Canon** |

Build times stated in `weapons/MODIFICATIONS.md` range from 15 to 60 minutes. Time costs are converted to real seconds in `TIME_MODEL.md`.

---

## 3. Tuning principles

| Principle | Meaning |
|---|---|
| **Charges are scarce on purpose.** | 8 CRD-7 charges is enough for a decision, not a route. |
| **No recharge.** | No tool recovers charges except where stated (BAR-FL reload). |
| **Duration is the verb.** | A 90 s window is long enough to cross a corridor and short enough to feel. |
| **Range is a risk.** | Longer range means a worse effect or a heavier cost. |
| **Combat is a failure mode.** | `weapons/OVERVIEW.md`. Tools are not tuned to make fights viable. |
| **No tool beats EOD or Omega-1.** | They are not a balance target. |

---

## 4. Detection numbers the tools interact with

| Value | Number | Source |
|---|---|---|
| Detection build time | 1.5–3 s | **Canon** — `STEALTH_DETECTION.md` |
| Alert State 1 | Times out after 20 s | **Canon** |
| Alert State 2 | Lasts until 45 s without line of sight | **Canon** |
| PTKW patrol cycle | 8 minutes | **Canon** — `ENEMY_AI.md` |
| Badge EIMU detection range | 15 m | **Canon** — `STEALTH_DETECTION.md` |
| Curious window (accessibility) | +4 s | **[PROPOSAL]** — `DIFFICULTY_ACCESSIBILITY.md` |

---

## 5. Enemy numbers

### PTKW
| Phase | Group | Notes | Source |
|---|---|---|---|
| 2 | Pairs on 8-minute cycles | Do not enter Type B passages | **Canon** |
| 4 | Triples with ACS-9 | Advance team: two assets, one manifest check | **Canon** |
| 5 | NPC obstacles | Marcus, Lani, Cho, Dayo, Priti | **Canon** |

### EOD
Not balanced, by design. The numbers are about the player's experience.

| Parameter | Value | Status |
|---|---|---|
| Appears | Day 4 (entered Day 3 night) | **Canon** — `characters/EOD.md` |
| Beatable | Never | **Canon** — `weapons/OVERVIEW.md` |
| Capture screen | 8 s | **Canon** — `SAVE_SYSTEM.md` |
| Capture rate per encounter | See `EOD_ENCOUNTERS.md` | **[PROPOSAL]** |
| Immune to ACS-9 | No; he feels it | **Canon** |
| OLF-14 effect | 8 minutes | **Canon** |

### Omega-1
| Parameter | Value | Status |
|---|---|---|
| ETA | 18–24 hours general; 22 hours for Labor Source #349 | **Canon** — `enemies/HQ-Response-Protocol.md` |
| Detection | Full-spectrum | **Canon** |
| Movement | Structured sweeps | **Canon** |
| Level 0 message sent | One sweep 12 minutes late | **Canon** |
| Type C crawlways | Safe | **Canon** — `SOLUTION_MATRIX.md` |
| Time in Type C | EIMU Coherence declines after 40 min | **Canon** — `SOLUTION_MATRIX.md` |
| Number of sweeps in Phase 6 | **[PROPOSAL]** 6–8 | Placeholder |
| Sweep interval | **[PROPOSAL]** 25–40 min | Placeholder |
| Warning before a sweep | **[PROPOSAL]** 60–90 s audible, from the Diagnostic readout | Placeholder |

---

## 6. Health numbers

| Track | Effect | Source |
|---|---|---|
| Thermal, Level 0 cold | −1 pip per 90 s without insulation | **Canon** — `HEALTH_SURVIVAL.md` |
| CRD-7 contact | Significant drain; recovery 3–5 min | **Canon** |
| CRD-7R contact | Near-lethal; recovery 15+ min | **Canon** |
| Cafeteria ration pack | Physical +2 | **Canon** — `INVENTORY.md` |
| Level 3 medical kit | Thermal +3, Physical +1 | **Canon** |
| Tarek's supply cache kit | Full thermal reset + Physical +2 | **Canon** |
| Comfort beverage | Neurological +1, EIMU Coherence +2 | **Canon** |
| Water | Physical +1, Thermal +1 | **Canon** |

The number of pips per track is not stated in any document. **[PROPOSAL]** 5 pips per track, as four LED strips with five segments each.

---

## 7. Targets for playtesting

**[PROPOSAL]** These are what to measure, not what to ship.

| Metric | Target | Why |
|---|---|---|
| Uses of CRD-7 per playthrough | 3–5 | Scarcity |
| Tool charges left at end of Phase 5 | 20–30% | The player has spent most of them |
| Mods built | 3–5 of 8 | No one builds everything |
| Time spent at a junction | 4–10 real minutes per visit | See `TIME_MODEL.md` |
| Share of players who use CRD-7R | < 20% | Lethal use should be a choice |

---

## Open questions

1. **CRD-7 source.** `INVENTORY.md` says Level 3 storage. `weapons/compliance/CRD-7 — Compliance Restraint Device.md` says Level 5 security storage, Phase 2. One of them is wrong.
2. **ACS-9 range.** The base range is "about 8 m" in `ACS-9D`; the base file gives no number.
3. **AMB-3 deployment vs AMB-3F.** If AMB-3 is not recoverable, how is it modified into AMB-3F? Presumably the player modifies it before deployment.
4. **Pressurized Pipe Tool location.** `INVENTORY.md` says Level 0 maintenance room; the tool file says it is available wherever the network runs.
5. **Health pip count.** Undefined.

---

*→ See: INVENTORY.md — the uses table.*
*→ See: weapons/OVERVIEW.md — the principles.*
*→ See: weapons/MODIFICATIONS.md — the modification index.*
*→ See: HEALTH_SURVIVAL.md — the four tracks.*
*→ See: STEALTH_DETECTION.md — the detection numbers.*
*→ See: ENEMY_AI.md — PTKW and Omega-1.*
*→ See: EOD_ENCOUNTERS.md — EOD.*
*→ See: SOLUTION_MATRIX.md — tool answers per obstacle.*
*→ See: TIME_MODEL.md — time costs.*
