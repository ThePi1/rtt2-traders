# Changes to check

Quest changes on the `quest-updates` branch that still need checking in game, plus text and design items left open. Tick items off as you go.

Zone positions are the box centre in game coordinates (x, y, z). Sizes are width × height × depth in metres.

## Zones to check in game

New zones are in `db/CustomQuestZones/C1_C4_C6_C7_C8_C9.json`. The first four are the least certain.

- [ ] **`C7_1` – Loot Lord 2, Woods depot Biotoilets.** Centre (-706, 9.35, 98), 4 × 3 × 5. The game has no floor data here, so the height was guessed from the objects. Check that standing inside the toilets completes the step.
- [ ] **`C7_2` – Loot Lord 2, Woods railway office (bunk beds).** Centre (-656, 9.1, 181.4), 9 × 3.5 × 16. Height guessed the same way as `C7_1`.
- [ ] **`C8` – Loot Lord 3, Lighthouse.** Centre (129, 10.922, -584.5), 9 × 4 × 12. Placed on the rocks past the minefield east of the Water Treatment Plant. Check that the spot matches the quest text and can see the machine guns.
- [ ] **`C4_2` – Back To The Future, Customs dorm 206.** Centre (229.6, 3.91, 138.4), 2 × 2.5 × 2.4, turned 3.5°. This is a place-item zone in the hallway outside room 206 in the two-story dorm. It overlaps the game's own zone `huntsman_020`, so check that the place-item prompt still appears.
- [ ] **`C9` – The Gungeon, Reserve.** Centre (-148.53, -8.067, -10.25), 49.9 × 2.9 × 16.9, turned 15.5°. Placed in Black Bishop's basement, where the bunker comes out, to follow the quest text. The sheet says Black Pawn; if it should be Black Pawn, the zone has to move.
- [ ] **`C6` – Loot Lord 1, Shoreline.** Centre (-628.01, -18.436, -236.04), 13.3 × 8.6 × 30, turned 17°. Placed in the Agrocomplex hangar with the toolboxes and welding machine (the sheet's "tool warehouse"). The other candidate is the pier warehouse.
- [ ] **`C1_1` – Deja-Vu, Ground Zero.** Centre (-13, 31.471, 76), 16 × 4 × 30. Open-plan office on the TerraGroup building's second floor. Check it on both Ground Zero versions.
- [ ] **`C1_2` – Deja-Vu, Ground Zero.** Centre (81.5, 15.734, 100.5), 8 × 4 × 17. Underground meat truck and the lane beside it. Check it on both versions.
- [ ] **`C7_3` – Loot Lord 2, Woods cultist bunker.** Centre (-273, 8.94, -413), 17 × 3.5 × 15.
- [ ] **`C4` – Back To The Future, director's door.** Not a new zone: the step now uses the existing `C4` outside the Tarcone director's office, instead of the missing `C4_1`.
- [ ] **`C10` – Loot Lord 4, Labyrinth.** Not a new zone: the step pointed at `C9` and now uses the existing `C10`.

## Quest fixes to check in game

### Not committed yet

- [ ] **Hooligan Hunt 1:** kills count on Customs only.
- [ ] **Healthy nor Wealthy nor Wise 3:** counts on both Ground Zero versions.
- [ ] **Auto Price 3:** counts on Reserve only.
- [ ] **Auto Price 1:** counts on Woods only. This map limit is new.
- [ ] **DevOps 3:** counts on Streets only. This map limit is new.
- [ ] **Healthy nor Wealthy nor Wise 1:** has 9 room steps now. Step 10 (room 223) was dropped because that room doesn't exist.
- [ ] **Q14 The Laboratory:** gives a TerraGroup Labs keycard on completion.
- [ ] **Q15 Big Brained:** the Signal Booster offer at Chimera unlocks only after this quest.
- [ ] **Q18 My Cherry:** gives 4 Electronic components.

### Committed in `aafd085`

- [ ] **Q22 The Eye Looks Back and Q23 The Case:** each one only unlocks once the previous quest is turned in.
- [ ] **Q23 The Case:** the statues can be placed at the Woods cultist circle (zone `F11`).
- [ ] **Q24 My Prayers Are Answered:** Secure Folder 0052 spawns at the Woods cultist circle, at (196.0, 0.6, -7.2). It's the custom copy, so base-game quests don't take it.
- [ ] **Q25 Daedalus' Curse:**
  - The quest gives 1 Labrys keycard.
  - Voron's Labrys keycard offer (121,000 RUB, LL1) unlocks.
- [ ] **Q26 Into The Maze:** gives both Bitcoins.
- [ ] **Q27 Purgatory:** only unlocks after Q26 is turned in.
- [ ] **Q28 Refusal and Q29 Acceptance:** turning one in fails the other.
- [ ] **Q30 Thank You For Playing:** gives 1,000 XP and 1 Bitcoin.

## Text for you to fix

- [ ] **Q20 Offering to the Eye:** a step says "church on Shoreline"; it should say Woods.
- [ ] **Bird Hunting:** the text says Lighthouse, but the drive spawns on Reserve.
- [ ] **The Gungeon:** says Black Bishop, which matches where `C9` is now. Only change it if the zone moves to Black Pawn.
- [ ] **Healthy nor Wealthy nor Wise 1:** the description still says "(Not implemented yet, please skip)".

## Still open

- [ ] **Q25 Daedalus' Curse:** Priest doesn't always drop the keycard. `Plugin.cs` raises its weight in his pockets but doesn't guarantee it, while the sheet asks for a guaranteed spawn.
- [ ] **Q28 Refusal and Q29 Acceptance:** the Demon Stim and Angel Stim rewards don't exist as items yet.
- [ ] **Q30 Thank You For Playing:** the 1,000 XP is a placeholder.
- [ ] **Before opening a PR:** merge `origin/main` into this branch. Main has `Plugin.cs` and README changes this branch doesn't have.
