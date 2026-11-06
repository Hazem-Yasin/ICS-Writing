# ICS — Rigged Sphere
## Save System Design

*The save system is a design argument. Every save system makes an argument about what the player's time is worth and what the game considers reversible. This game's argument: the choices that matter are permanent. The choices that don't matter are frequently checkpointed. The player should never lose meaningful progress from a crash or a disconnection. They should also never be able to undo the decision to show Tarek his brother's name.*

---

## Autosave Architecture

The game autosaves continuously in the background. The autosave fires on the following triggers:

- **Room transition** — every time the player passes through a door or enters a maintenance passage opening
- **Item acquisition** — every item pickup
- **Conversation start** — the moment before a conversation branch opens
- **Significant time passage** — every 3 minutes of movement without a previous trigger
- **Phase transition** — immediately when a phase-change event fires

The autosave is invisible. There is no spinning indicator, no save icon. The badge display does not flag it. The player has no interface feedback that a save has occurred. Saving is simply what the world does — it persists. This is consistent with the facility itself: the CCN is always logging, the EIMU is always recording. The player's experience of the world is continuous whether or not they are watching the save process.

**Load behavior after a crash or quit:** The game returns to the last autosave point. In most cases, this is within the last 3 minutes of play. In the worst case — entering a large area with no room transitions and no item pickups — it is within 3 minutes. The player will rarely lose more than 3 minutes.

---

## The Conversation Autosave — The Critical Rule

The autosave fires immediately before a conversation branch opens. This means:

If the player approaches Tarek and triggers the conversation about Khalid's registry entry, the save fires at the moment the conversation activates — before the player selects any option. If the player quits during or after the conversation, they return to the start of that conversation.

**What this means:** The player cannot autosave after selecting a conversation option and before seeing its consequence. They can quit and return to the start of the conversation and make a different choice. This is the intended behavior for conversations.

**What this does not mean:** The player cannot undo a conversation that has fully completed and been walked away from. If the player showed Tarek the registry entry, had the full conversation, received Rania's note, and then saved naturally during the next room transition — that is permanent. `TAREK_REGISTRY` flag is set. Tarek has seen it. The note is in the player's inventory. This does not reset.

**The implication the player figures out:** If they are about to do something significant — show a document, make a choice, trigger an event — they have one last chance to not approach the object or person. The moment they trigger the conversation, it is happening. There is no preview of what will be asked, no warning that this is consequential. The game treats every conversation as one that might not be consequential, because not all of them are. The player learns which ones matter by having played through them.

---

## Manual Save — One Slot

The player has access to one manual save through the quarters safe interface. The manual save can be triggered at any time while in the player's quarters. It cannot be triggered elsewhere.

**The limit is one slot.** Not ten slots, not five — one. Writing a manual save overwrites the previous manual save.

The design intent: the manual save is for the player who needs to put the game down at a time that is not a clean room transition or a conversation checkpoint. It is not a strategy tool — it is a rest point. One slot prevents the player from using manual saves as a consequence-reversal system. If they write over their pre-Sera conversation save to capture a Phase 5 event, the pre-Sera save is gone.

**The quarters safe as the save interface:** This means the player must physically return to their quarters to save manually. In Phase 0–1, this is trivial. In Phase 5, returning to quarters requires navigating through a changed facility. The manual save becomes less accessible exactly when the player most wants it.

**In Phase 6:** The quarters restriction lifts in Phase 5 and does not re-restrict in Phase 6. The player can return to quarters. In the 22-hour window, returning to quarters to save is possible. It is also the decision to spend time going back instead of forward. The game does not tell the player their remaining time — they have to track it themselves from the in-world clock on the badge display. They know 22 hours. They know where they are in it by how much they've done.

---

## Irreversible Events — The Permanent List

These events cannot be undone regardless of save behavior. Once they occur, they are permanent in any playthrough that passes their save point:

| Event | What triggers it | Why it's permanent |
|---|---|---|
| Showing Tarek the registry | Conversation — `TAREK_REGISTRY` flag | He has seen his brother's name. He cannot unsee it. |
| Showing Sera the Yusra escalation flag | Conversation — `SERA_YUSRA` flag | She now knows. She cannot unknow it. |
| Marcus going to the printer | Triggered by player showing him the Board Charter section | The pages are printed. They're in the atrium. |
| Sending the Level 0 device message | Action — `L0_MESSAGE_SENT` flag | Sent. Received or not, it was sent. |
| Tarek reading Rania's note in the cafeteria | Phase 4 cutscene — fires automatically | Non-interactive. This is what happens on Day 21. |
| Category Omega threshold crossing | Phase 6 trigger — fires automatically | Non-interactive. The compound is released. |
| Sera's note delivered to Level 0 | Action — `SERA_NOTE_DELIVERED` flag | Left there. She wrote it. It exists in that place now. |

**The design argument:** These events are permanent because the people in them are real — as real as this world makes them. When Tarek sees Khalid's name, something happens inside him. The game does not let the player pretend it didn't happen because they reloaded. The player chose to show him. That choice was made by the player, for the player, and the world continues from it.

---

## The Death Save — What Happens When the Player Dies

Death states are defined in HEALTH_SURVIVAL.md. The save behavior on death:

**Standard death (health track failure):** The game returns to the last autosave point. No additional penalty. The player tries again with the same inventory, the same flags, the same world state as of the last autosave. Death from health depletion is the game's way of telling the player they were detected, or their route was wrong, or they stayed in the cold too long. The lesson is in the return, not in a punishment system.

**Caught by EOD:** Returns to last autosave. The reclassification screen — the document, the date, the asset number — is displayed for 8 seconds before the return. Long enough to read. The player is not penalized with the wait. The wait is the point.

**Caught by Omega-1 (Phase 6 only):** Returns to the latest Phase 6 autosave, or *"Last Entry"* if none exists; the 22-hour clock is restored from that save, not reset. The same reclassification screen. The date is Phase 6. The compound has been released. The player knows what the date means now — Omega-1 catching them is not a transition, it is a reclassification that happens inside the ending. This is the game insisting that even in the last 22 hours, the system still does what the system does.

---

## The Ending Save — Final Autosave

When Phase 6 begins — the moment the Category Omega threshold crosses — the game creates a permanent autosave that cannot be overwritten. This save is labeled in the menu as *"Day [X] — Last Entry."* It captures the full world state at Phase 6 start, including all flags, all relationships, all items in the player's inventory.

This save cannot be loaded to undo Phase 6 beginning. It can be loaded to replay Phase 6 with the same world state — to make different choices in the 22 hours, to explore what the player didn't reach in the first run. The player who wants to see what happens if they take Sera's note to Level 0 but didn't on their first run can load *"Last Entry"* and try.

**What cannot be reloaded:** Anything before Phase 6. The game does not offer a chapter select. There is no "return to Phase 3" option. The player's full playthrough, with all the choices that built toward this, is the version of the world they are in. A second playthrough means starting over. *"Last Entry"* is the one exception — a window into the ending from the exact world state the player built.

**The design argument:** The player spent 8–15 hours building the world state that Phase 6 inherits. That work is theirs. The ending should honor it by being replayable from the state they built, not from a generic starting point. But the path that built it cannot be rewound. The choice to show Tarek the registry or not was made hours ago. *"Last Entry"* does not change that. It only gives the player more time in the consequence of everything they already decided.

---

*→ See: HEALTH_SURVIVAL.md — the death states that return to save points.*
*→ See: NPC_COMPANIONS.md — the permanent relationship flags the save system tracks.*
*→ See: scene-notes/Phase 6 Final 22 Hours.md — the specific choices available in the 22-hour window.*
