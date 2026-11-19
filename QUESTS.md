# Quest tracker

The design and build status of every rtt2-traders quest. This file replaced the "Quest Sheet _ Quest Items" spreadsheet on 2026-11-19; edit quests here, not in the sheet.

**Status**
- **Built:** in the repo, not yet audited (quests built after the 2026-11-19 audit start here).
- **Audited:** in the repo and checked against the design. Fixes are in Notes.
- **Needs check:** built, but something can only be confirmed in game. See [Check in game](#check-in-game).
- **To build:** not in the repo yet.
- **Flagged:** needs a decision or information from you. See [Flags for you](#flags-for-you).
- **Skipped:** can't be built as designed. The reason is in Notes.

Quest ids are the quest's `_id` in `db/CustomQuests/<trader>/Quests`. Unlocked-by and Reward are the original design notes; the built quest may differ, and Notes says how.

## Flags for you

### Text to fix

- [ ] **Q20 Offering to the Eye:** a step says "church on Shoreline"; it should say Woods.
- [ ] **Bird Hunting:** the text says Lighthouse, but the drive spawns on Reserve.
- [ ] **The Gungeon:** says Black Bishop, which matches where `C9` is now. Only change it if the zone moves to Black Pawn.
- [ ] **Healthy nor Wealthy nor Wise 1:** the description still says "(Not implemented yet, please skip)".
- [ ] **L94 Faster Dayo 2:** all three step texts still end "(wip, skip)". The steps work now.
- [ ] **L92 Gun Nut 3:** the step text says "the [blank] room on RB-ST (wip, please skip)". The step works now (zone `L92`).
- [ ] **L97 The Auto Price 2:** the step text says "Reach lv. with Price"; it needs loyalty level 3.
- [ ] **L80 Under the Knife 3:** the quest's name (`6a14f2e1…`) says "Part 2"; there are two Part 2s. It should say Part 3.
- [ ] **L72 Ok Boomer 1:** I wrote the two new step texts ("Find a bandage in raid", "Hand over a found in raid bandage"). Reword if you like.
- [ ] **L99 Twenty-Five Types of Ammo 1:** description and success text are my [PH] text.

### Open design questions

- [ ] **"MCC" (L35 Live, Laugh, Love 3; L59 Vipassana 3; S5):** built as Advanced current converter. If MCC means another item, say which.
- [ ] **C17 Bi-Lingual 4:** the design says an SSA AP *barter*; I added a cash offer (1,150 RUB a round, LL3) so the unlock shows something. Give me the barter if you want one.
- [ ] **Counts and rewards that differ from the design** (left as built, in case you tuned them): weapon-line XP is about half the sheet's (L2–L17); Advantage of Range 3 has 15 kills (design 20); Makita, Nikita 3 has 150 (200); Healthy nor Wealthy nor Wise 2 has 8 juice (10); Vipassana 3 has 2 tracer packs (10); Q9 gives 250 USD and EUR (500 each); C2 gives 50k (100k); Maxwell's Demon gives 0.6 Fence standing (0.3); White Whale gives 0.95 (0.65); Leg Up 1 unlocks after Hooligan Hunt 3 (design C11); Green Gold after Loot Lord 4 (design C8).

- [ ] **Q25 Daedalus' Curse:** Priest doesn't always drop the keycard. `Plugin.cs` raises its weight in his pockets but doesn't guarantee it, while the sheet asks for a guaranteed spawn.
- [ ] **Q28 Refusal and Q29 Acceptance:** the Demon Stim and Angel Stim rewards don't exist as items yet.
- [ ] **Q30 Thank You For Playing:** the 1,000 XP is a placeholder.
- [ ] **Before opening a PR:** merge `origin/main` into this branch. Main has `Plugin.cs` and README changes this branch doesn't have.


## Check in game

Zone positions are the box centre in game coordinates (x, y, z). Sizes are width × height × depth in metres.

### Zones to check in game

From the audit (existing zones):

- [ ] **`L94_1`, `L94_2`, `L94_3` – Faster Dayo 2, Reserve.** Now wired to the steps in order: red guard tower top floor, Black Knight rooftop post, White Bishop rooftop mortar. Check each zone is at the spot its step names. They sit at (118.4, 0.6, -86.2), (11.8, 0.1, -15.7) and (-74.0, 0.7, -29.7).
- [ ] **`L92` – Gun Nut 3, Reserve.** Now wired to the repair kit placement; at (103.3, -5.9, 49.9) by the repair base. Check it's in the RB-ST room.
- [ ] **`Q21` – An Eye Cannot Speak, Shoreline resort.** The box spans 1.5–2.5 m high, and the nearest floor the game maps is at -3.7 m. Fine if it's on an upper floor bots never walk; otherwise you can't reach it.
- [ ] **`z_q10_gzbench` – Load-Bearing Citizen 1, Ground Zero.** The box spans 30.4–31.4 m, and the nearest mapped floor is 23.4 m. Same as `Q21`.
- [ ] **`F11_2` – Sacramentum, Shoreline.** Renamed from `F5_2`, its only change. Check the rooster can still be placed.

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

### Quest fixes to check in game

#### Committed in `3bcf9ab`

- [ ] **Hooligan Hunt 1:** kills count on Customs only.
- [ ] **Healthy nor Wealthy nor Wise 3:** counts on both Ground Zero versions.
- [ ] **Auto Price 3:** counts on Reserve only.
- [ ] **Auto Price 1:** counts on Woods only. This map limit is new.
- [ ] **DevOps 3:** counts on Streets only. This map limit is new.
- [ ] **Healthy nor Wealthy nor Wise 1:** has 9 room steps now. Step 10 (room 223) was dropped because that room doesn't exist.
- [ ] **Q14 The Laboratory:** gives a TerraGroup Labs keycard on completion.
- [ ] **Q15 Big Brained:** the Signal Booster offer at Chimera unlocks only after this quest.
- [ ] **Q18 My Cherry:** gives 4 Electronic components.

#### Committed in `aafd085`

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


## Storyteller side lines (L)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| L0 | Storyteller | Welcome to RTT2! | Turn in 1 RUB | First quest! | 1000 XP, Q1 | `69bdfba39ea015fa709c681f` | Audited | Unlock status: Complete |
| L1 | Storyteller | Kill Time | Kill any 3 PMCs or Scavs | Q6 | 2500 XP | `6a0b8b6516ab7c2dcc5586cf` | Audited | Sheet: These are optional till first quest; Unlock status: Complete; Hooligan Hunt - Part 2 |
| L2 | Storyteller | Rest In Pieces - Part 1 | Kill PMC with Shotgun, 5 | L1 | 3000 XP, buy Benelli M3, Remington 870 | `6a0b8c6616ab7c2dcc5586d5` | Audited | Fixed: the kill step listed the weapon class id, which never matches; it now lists every vanilla shotgun (`2a9b9c5`).; Unlock status: Complete |
| L3 | Storyteller | Rest In Pieces - Part 2 | Kill PMC with Shotgun, 10 | L2 | 6000 XP, buy KS23, Saiga-12K, Both MPS Auto, | `6a0b8d9216ab7c2dcc5586df` | Audited | Fixed: the kill step listed the weapon class id, which never matches; it now lists every vanilla shotgun (`2a9b9c5`).; Unlock status: Complete; Hooligan Hunt - Part 3 |
| L4 | Storyteller | Rest In Pieces - Part 3 | Kill PMC with Shotgun, 15 | L3 | 8000 XP, Auto Saiga | `6a0b8e9f16ab7c2dcc5586f0` | Audited | Fixed: the kill step listed the weapon class id, which never matches; it now lists every vanilla shotgun (`2a9b9c5`).; Unlock status: Complete; Pistol Whip |
| L5 | Storyteller | Bullet Hose - Part 1 | Kill PMC with SMG, 5 | L1 | 2500 XP, buy Kedr, Kedr B, UZI Pistol | `6a0b8f4516ab7c2dcc5586f8` | Audited | Fixed: the kill step listed the weapon class id, which never matches; it now lists every vanilla SMG (`2a9b9c5`).; Unlock status: Complete; Im Hungry |
| L6 | Storyteller | Bullet Hose - Part 2 | Kill PMC with SMG, 10 | L5 | 5000 XP, buy MP5K,PP19,MP9(2), | `6a0b902116ab7c2dcc558705` | Audited | Fixed: the kill step listed the weapon class id, which never matches; it now lists every vanilla SMG (`2a9b9c5`). Built with Saiga-9 and MP9-N where the design says PP19.; Unlock status: Complete; Apex Predator - Part 1 |
| L7 | Storyteller | Bullet Hose - Part 3 | Kill PMC with SMG, 15 | L6 | 8000 XP, buy SR2M, UMP, UZI Pro SMG | `6a0b90bf16ab7c2dcc558714` | Audited | Fixed: the kill step listed the weapon class id, which never matches; it now lists every vanilla SMG (`2a9b9c5`).; Unlock status: Complete |
| L8 | Storyteller | Bullet Hose - Part 4 | Kill PMC with SMG, 20 | L7 | 12000 XP, buy P90,MP7(2),MPX | `6a0b913c16ab7c2dcc558721` | Audited | Fixed: the kill step listed the weapon class id, which never matches; it now lists every vanilla SMG (`2a9b9c5`).; Unlock status: Complete; Advantage of Range - Part 3 |
| L9 | Storyteller | Pistol Whip - Part 1 | Kill PMC with pistol, 5 | L1 | 3500 XP, buy Rhino(2),Deagle,Mackarov, APB | `6a0b929616ab7c2dcc55872f` | Audited | Unlock status: Complete; Rest In Pieces - Part 2 |
| L10 | Storyteller | Pistol Whip - Part 2 | Kill PMC with pistol, 10 | L9 | 7000 XP, M1911,M45a1, USP,PL-15,P226 | `6a0b93cd16ab7c2dcc55873f` | Audited | Unlock status: Complete; Rest In Pieces - Part 3 |
| L11 | Storyteller | Pistol Whip - Part 3 | Kill PMC with pistol, 15 | L10 | 9000 XP, Glock(3),57 | `6a0b945716ab7c2dcc55874e` | Audited | Unlock status: Complete; Advantage of Range - Part 2 |
| L12 | Storyteller | Advantage of Range - Part 1 | Kill PMC with DMR, 5 | L1 | 1500 XP, SVD, M1A, | `6a0b951416ab7c2dcc55875e` | Audited | Unlock status: Complete; Pistol Whip3 |
| L13 | Storyteller | Advantage of Range - Part 2 | Kill PMC with DMR, 10 | L12 | 3000 XP, G28, SR25, RSASS | `6a0b957816ab7c2dcc558768` | Audited | Kill counter typed Elimination (`c48be06`).; Unlock status: Complete |
| L14 | Storyteller | Advantage of Range - Part 3 | Kill PMC with DMR, 20 | L13 | 6000 XP,SWORD | `6a0b95e816ab7c2dcc558774` | Audited | Design says 20 kills; built with 15. Left as built.; Unlock status: Complete |
| L15 | Storyteller | Dialed In - Part 1 | Kill PMC with Sniper headshots, 2 | L1 | 4000 XP, VPO, M700 | `6a0b964516ab7c2dcc55877c` | Audited | Unlock status: Complete; AR Lover |
| L16 | Storyteller | Dialed In - Part 2 | Kill PMC with Sniper headshots, 4 | L15 | 8000 XP, DVL, T-5000, SV-98 | `6a0b971016ab7c2dcc558787` | Audited | Unlock status: Complete; Back To Basics |
| L17 | Storyteller | Dialed In - Part 3 | Kill PMC with Sniper headshots, 8 | L16 | 10000 XP, TRG,AXMC | `6a0b97bb16ab7c2dcc558794` | Audited | Kill counter typed Elimination (`c48be06`).; Unlock status: Complete; Advantage of Range |
| L18 | Storyteller | Apex Predator - Part 1/2 | Kill Tagilla | L27 | 7800 XP | `6a0b983a16ab7c2dcc55879e` | Audited | Unlock status: Complete; Apex Predator - Part 3 |
| L19 | Storyteller | Apex Predator - Part 2 | Kill Kollantay | L18 | 5600 XP | `6a0b995816ab7c2dcc5587ae` | Audited | Unlock status: Complete; Apex Predator - Part 4 |
| L20 | Storyteller | Apex Predator - Part 3 | Kill Sanitar | L19 | 6800 XP | `6a0b9a2716ab7c2dcc5587b8` | Audited | Unlock status: Complete; Pistol Whip2 |
| L21 | Storyteller | Apex Predator - Part 4 | Kill Goons | L20 | 12300 XP | `6a0b9a8d16ab7c2dcc5587c0` | Audited | Kill counter typed Elimination (`c48be06`).; Unlock status: Complete; Dialed In |
| L22 | Storyteller | Apex Predator - Epilogue | Kill Partisan | L21 | 6500 XP f1 RD assort | `6a0b9b4e16ab7c2dcc5587ce` | Audited | Unlock status: Complete; Dialed In - Part 2 |
| L23 | Storyteller | Apex Predator - Part 2/2 | Kill Killa | L27 |  | `6a0b98ea16ab7c2dcc5587a6` | Audited |  |
| L24 | Storyteller | Restock | Find FIR 1 bandage, 3x small tushonka | L22 | 1000 XP | `6a0bb5cc255fe4bc50f25826` | Audited | Fixed: beef stew hand-in is found in raid, like its find step (`a2cf888`).; Unlock status: Complete; Quest Name Bank |
| L25 | Storyteller | Hooligan Hunt - Part 1 | Kill 5 Scavs on Customs | L22 | XP | `6a0bb658255fe4bc50f2582b` | Audited | Got a Friend in Need \| Euphoric Retribution |
| L26 | Storyteller | Hooligan Hunt - Part 2 | Kill 8 Scavs on Woods or Shoreline at night 21-4 | L25 | XP | `6a0bb6bc255fe4bc50f25833` | Audited | Introductions |
| L27 | Storyteller | Hooligan Hunt - Part 3 | Kill 40 Scavs on any map | L26 | XP | `6a0bb7f9255fe4bc50f25842` | Audited | Hooligan Hunt |
| L28 | Storyteller | I'm Hungry | Handover 3 FIR noodes and 3 FIR Iskra | L29 | XP, Holodilnick bag | `6a0bb873255fe4bc50f2584a` | Audited | Apex Predator - Part 2 |
| L29 | Storyteller | Ammo Lover | Handover 8 boxes FIR ammo | L30 | XP | `6a0bb9e8255fe4bc50f25853` | Audited | Dialed In - Part 3 |
| L30 | Storyteller | Back To Basics | Kill 4 PMCs, 4 Scav with a pistol on Shoreline | L22 |  | `6a0bbb85255fe4bc50f2585a` | Audited | Rest In Pieces |
| L31 | Storyteller | Broad Consensus | Reach rep 2 with all new traders (minus Storyteller) | Q19 |  |  | To build | Bullet Hose |
| L32 | Storyteller | Domain Expansion | Reach lv2 rep with all modded traders | Q14 | Unlock all below pt.1 quests, 10k XP | `69f94677a49a5754e709dbae` | Audited | Sheet said "not working": it needs LL2 with Atlas, Needle and Price, who had no quests to raise standing. Reachable once their quests are built.; Sheet: not working |
| L33 | Storyteller | Live, Laugh, Love - Part 1 | Turn in FIR: 2x Air Filter, 3x GPU, 5x Hose, 5x ES Lamp | L32 | Hideout Management levels | `69f94739a49a5754e709dbb8` | Audited |  |
| L34 | Storyteller | Live, Laugh, Love - Part 2 | Turn in FIR: 2x AESA, 7x Screws, 7x Bolt, 1x Intelligence Folder, 2x Iskra | L33 | Hideout Management levels | `69f94af1a49a5754e709dbbe` | Audited | Fixed: asks for 2 Iskra (was 1), found in raid (`a2cf888`). |
| L35 | Storyteller | Live, Laugh, Love - Part 3 | Turn in FIR: 1x Vertex, 2x Blue Intelligence, 1x MCC, 4x Toolset, 2x LEDX | L34 | Hideout Management levels (max out) | `69f94bf2a49a5754e709dbc5` | Flagged | "MCC" was built as Advanced current converter. See Flags. |
| L36 | Storyteller | Molecular Assembly - Part 1 | Reach lv2 in each skill: LMG, HMG, Shotguns, Revolvers | L32 | Crafting levels | `69f94ec628f89593eb3bee78` | Audited | Sheet: get rid of hmg |
| L37 | Storyteller | Molecular Assembly - Part 2 | Turn in FIR: 4x Tetriz, 1x BTC, 10x M67 grenade, 5x Weapon Parts, 1x Tank Battery, 3x KEK, 2x Car Battery | L36 | Crafting levels | `69f94f6a28f89593eb3bee7e` | Audited | Fixed: weapon parts find step is found in raid, like the hand-in (`a2cf888`). |
| L38 | Storyteller | Molecular Assembly - Part 3 | Turn in FIR (yes, really): 1m RUB, 100k USD, 100k EUR | L37 | Crafting levels | `69f9502f28f89593eb3bee89` | Audited |  |
| L39 | Storyteller | Running on Empty - Part 1 | Kill 10 PMCs under the effects of stimulants | L32 | Metabolism levels | `69f9feebe53cfbf3b12f0784` | Audited |  |
| L40 | Storyteller | Running on Empty - Part 2 | Turn in FIR: 10x Iskra, 10x Water | L39 | Metabolism levels | `69fa0399e53cfbf3b12f078a` | Audited |  |
| L41 | Storyteller | Running on Empty - Part 3 | Kill 4 PMCs with while wearing PACA and a pompon hat, while light bleeding | L40 | Metabolism levels | `69fa050ce53cfbf3b12f078e` | Audited |  |
| L42 | Storyteller | Safe on Block - Part 1 | Mark all the red computers in the game dev room on Streets | L32 | Immunity levels |  | To build |  |
| L43 | Storyteller | Safe on Block - Part 2 | Shoot: 1 PMC in the left leg with a shotgun >50m, 1PMC in the right leg with a shotgun >50m, 1PMC in the torso with a shotgun >65m | L42 | Immunity levels |  | To build |  |
| L44 | Storyteller | Safe on Block - Part 3 | Survive with no food and no water for 10 minutes, then survive and extract | L43 | Immunity levels |  | To build |  |
| L45 | Storyteller | Dodge Caravan - Part 1 | Get 3 Scav kills with dehydration | L32 | Endurance levels | `69ff8a544a655e862e8149ce` | Audited |  |
| L46 | Storyteller | Dodge Caravan - Part 2 | Kill 10 PMCs using AUG 10-round mag | L45 | Endurance levels | `6a0ce468de041c7f96100a7e` | Audited | Fixed: rewarded Mag Drills; now Endurance like the rest of the line (`ca26ad1`). |
| L47 | Storyteller | Dodge Caravan - Part 3 | Use every flare extract in the game | L46 | Endurance levels | `6a093c1fe8af905ce4402881` | Audited |  |
| L48 | Storyteller | Two Million Year Old Ice Cube - Part 1 | Find and turn in 1x Holodilnik found in raid | L32 | Strength levels | `6ac6dcfea4ca66184b6db860` | Audited |  |
| L49 | Storyteller | Two Million Year Old Ice Cube - Part 2 | Find and turn in 2x Tank Battery fir | L48 | Strength levels | `6ac6dfc0a4ca66184b6db866` | Audited |  |
| L50 | Storyteller | Two Million Year Old Ice Cube - Part 3 | Get 5 melee PMC kills, 10 melee scav kills, while stunned | L49 | Strength levels | `6ac6e036a4ca66184b6db86b` | Audited |  |
| L51 | Storyteller | Flat Life Regen - Part 1 | Kill 10 Scavs while affected by light bleed | L32 | Vitality levels | `69ff946a30c5fd97a1313db6` | Audited |  |
| L52 | Storyteller | Flat Life Regen - Part 2 | Kill Killa while affected with heavy bleed | L51 | Vitality levels | `69ff951930c5fd97a1313dbd` | Audited | Fixed: kill target was empty, so Killa never counted; heavy bleed now counts on the right leg too (`505592c`). |
| L53 | Storyteller | Flat Life Regen - Part 3 | Heavy bleed for 10 minutes, survive and extract | L52 | Vitality levels | `69ff959630c5fd97a1313dc4` | Audited |  |
| L54 | Storyteller | Healthy nor Wealthy nor Wise - Part 1 | Enter all 10 prime-numbered rooms on 3story Dorms (101 103 107 109 113 211 223 307 311 313) in order | L32 | Health, Intellect levels | `6ac6e56ba4ca66184b6db879` | Audited |  |
| L55 | Storyteller | Healthy nor Wealthy nor Wise - Part 2 | Turn in 10x FIR pineapple juice | L54 | Health, Intellect levels | `6ac6e7e3a4ca66184b6db89b` | Audited | Design says 10 juice; built with 8. Left as built. |
| L56 | Storyteller | Healthy nor Wealthy nor Wise - Part 3 | Kill 6 PMC on Ground Zero between 12:00 AM and 1 AM | L55 | Health, Intellect levels | `6ac6e88ba4ca66184b6db8bf` | Audited |  |
| L57 | Storyteller | Vipassana - Part 1 | Find and Turn in FIR 1x pack Green Tracer 9mm | L32 | Perception, Attention levels | `69fa0ce3c23dface5a239261` | Audited |  |
| L58 | Storyteller | Vipassana - Part 2 | Turn in 20M RUB | L57 | Perception, Attention levels | `69fa298dc23dface5a239266` | Audited |  |
| L59 | Storyteller | Vipassana - Part 3 | Turn in FIR 10 BTC, 5x LEDX, 5x Blue Folder, 5x MCC, 10x pack 9x19 Green Tracer | L58 | Perception, Attention levels | `69fa2a1fc23dface5a23926a` | Flagged | Design says 10 packs of green tracer; built with 2. "MCC" built as Advanced current converter. See Flags. |
| L60 | Storyteller | A Fart in the Wind - Part 1 | Kill Sanitar at night | L32 | Covert movement levels | `69ff9c2905b2e8932302412c` | Audited | Fixed: kill target was empty, so no kill counted (`505592c`). |
| L61 | Storyteller | A Fart in the Wind - Part 2 | Kill 4 rogues on Lighthouse at night | L60 | Covert movement levels | `69ffa22805b2e89323024132` | Audited | Fixed: kill target was empty, so no kill counted (`505592c`). |
| L62 | Storyteller | A Fart in the Wind - Part 3 | Kill Killa at night | L61 | Covert movement levels | `69ffcc7f05b2e89323024139` | Audited | Fixed: kill target was empty, so no kill counted (`505592c`). |
| L63 | Storyteller | Kobe - Part 1 | 5 Scav kills with Grenades | L32 | Throwables | `69ff979dde23b7f4f68f23be` | Audited | Kill counter typed Elimination (`c48be06`). |
| L64 | Storyteller | Kobe - Part 2 | 5 PMC kills with Grenades | L63 | Throwables | `69ff98bfde23b7f4f68f23c3` | Audited |  |
| L65 | Storyteller | Kobe - Part 3 | 5 PMC kills with m67 grenade | L64 | Throwables | `69ff9905de23b7f4f68f23c9` | Audited | Quest id corrected (the sheet had Pulling Doubt 1's). |
| L66 | Storyteller | Pulling Doubt - Part 1 | 10 PMC kills with LMG | L32 | Mag drills levels | `6a094632ff1eccc62be30e8b` | Audited | Fixed: rewarded Aim Drills; now Mag Drills as designed (`ca26ad1`). Quest id corrected. |
| L67 | Storyteller | Pulling Doubt - Part 2 | 5 PMC kills on left arm, 5 PMC kills on right arm, with LMG | L66 | Mag drills levels | `6a09466eff1eccc62be30e92` | Audited | Fixed: rewarded Aim Drills; now Mag Drills (`ca26ad1`). Quest id corrected. |
| L68 | Storyteller | Pulling Doubt - Part 3 | Kill Kaban in legs with LMG | L67 | Mag drills levels | `6a0946c8ff1eccc62be30e9b` | Audited | Fixed: rewarded Aim Drills; now Mag Drills (`ca26ad1`). Quest id corrected. |
| L69 | Storyteller | As Sly as a Fox - Part 1 | Sell 5 whiskey to Price | L32 | Charisma levels | `6ac6ec80a4ca66184b6db8c8` | Audited |  |
| L70 | Storyteller | As Sly as a Fox - Part 2 | Sell 20 stims to Needle | L69 | Charisma levels | `6ac6ec81a4ca66184b6db8c9` | Audited |  |
| L71 | Storyteller | As Sly as a Fox - Part 3 | Sell 5 AESA to Weiss | L70 | Charisma levels | `6ac6ec82a4ca66184b6db8ca` | Audited |  |
| L72 | Storyteller | OK Boomer - Part 1 | Turn in 1 FIR bandage | L32 | Memory Levels | `6ac6fa6ebaae3403037837eb` | Audited | Fixed: had no steps, so it completed on accept; now hands in 1 found-in-raid Army or Aseptic bandage (`837f539`). |
| L73 | Storyteller | OK Boomer - Part 2 | Turn in 20 RUB | L72 | Memory Levels | `6ac6fa91baae3403037837ed` | Audited |  |
| L74 | Storyteller | OK Boomer - Part 3 | Kill 1 PMC | L73 | Memory Levels | `6ac6fdebbaae3403037837f6` | Audited |  |
| L75 | Storyteller | Mashed Potatoes - Part 1 | Find and Turn in 2 Police Batons,2 Cultist Knives FIR | L32 | Melee levels | `69ffd548ec2ed50f6bc01802` | Audited |  |
| L76 | Storyteller | Mashed Potatoes - Part 2 | Turn in 1 Red Rebel FIR | L75 | Melee levels | `69ffda9dec2ed50f6bc01809` | Audited |  |
| L77 | Storyteller | Mashed Potatoes - Part 3 | Find and Turn in 2 Taiga FIR | L76 | Melee levels | `69ffdb20ec2ed50f6bc0180e` | Audited |  |
| L78 | Storyteller | Under the Knife - Part 1 | Turn in FIR 7x Esmarch, 5x CMS, 4x SRV | L32 | Surgery levels | `6a14ee45b636566917f0c0fd` | Audited |  |
| L79 | Storyteller | Under the Knife - Part 2 | Turn in FIR 4x of each stim | L78 | Surgery levels | `6a14f097b636566917f0c107` | Audited | Fixed: Meldonin hand-in is found in raid (`a2cf888`). |
| L80 | Storyteller | Under the Knife - Part 3 | Get a kill with the blicky | L79 | Surgery levels | `6a14f2e1b636566917f0c134` | Flagged | Built as a second "Under the Knife - Part 2"; its name should say Part 3. See Flags. |
| L81 | Storyteller | Makita, Nikita - Part 1 | Kill 50 PMC | L32 | Aim Drills levels | `69ffcd72305570df33796f24` | Audited |  |
| L82 | Storyteller | Makita, Nikita - Part 2 | Kill 100 PMC | L81 | Aim Drills levels | `69ffcdb6305570df33796f2a` | Audited |  |
| L83 | Storyteller | Makita, Nikita - Part 3 | Kill 200 PMC | L82 | Aim Drills levels | `69ffcdf4305570df33796f30` | Audited | Design says 200 kills; built with 150. Left as built. |
| L84 | Storyteller | Senior DevOps Engineer - Part 1 | Get 10 PMC kills with an AK, without any dust covers | L32 | Troubleshooting levels | `6ac6feffbaae3403037837fe` | Audited | Fixed: needs 10 kills (was 1); every dust cover now excludes on its own (they were one group, which never excluded); stray magazine dropped from the AK list (`1623773`). |
| L85 | Storyteller | Senior DevOps Engineer - Part 2 | Sell 5x non-FIR repair kit to Atlas | L84 | Troubleshooting levels | `6ac6ff35baae340303783800` | Audited | Fixed: sells 5 repair kits (was 2) (`1623773`). |
| L86 | Storyteller | Senior DevOps Engineer - Part 3 | Kill Kollantay on Streets with an AK, no dust cover, no sights, no muzzle, and mag size 10 | L85 | Troubleshooting levels | `6ac6ff43baae340303783802` | Audited | Fixed: dust cover, sight and muzzle exclusions now work one by one; takes any AK 10-round magazine (`1623773`). |
| L87 | Storyteller | Fully Vested - Part 1 | Turn in <75 PACA | L32 | light vest, heavy vest levels | `6a14f73a3de7c9e706e258bb` | Audited |  |
| L88 | Storyteller | Fully Vested - Part 2 | Turn in <75% ghzel | L87 | light vest, heavy vest levels | `6a14f7d03de7c9e706e258c1` | Audited |  |
| L89 | Storyteller | Fully Vested - Part 3 | Turn in <75% Killa Vest | L88 | light vest, heavy vest levels | `6a14f8223de7c9e706e258c7` | Audited |  |
| L90 | Storyteller | Gun Nut - Part 1 | Turn in 1 FIR repair kit | L32 | Weapon Maintenence levels | `69ffcfb3ce2c12d1a7ec880d` | Audited |  |
| L91 | Storyteller | Gun Nut - Part 2 | Turn in 2 FIR repair kit | L90 | Weapon Maintenence levels | `69ffd2bbce2c12d1a7ec8813` | Audited |  |
| L92 | Storyteller | Gun Nut - Part 3 | Plant a FIR repair kit on reserve (RB-ST), survive and extract | L91 | Weapon Maintenence levels | `6aca8031a26d5245cb767407` | Needs check | Fixed: placement had no zone; now uses `L92` (`d2c7bba`). Step text still says "(wip, please skip)". |
| L93 | Storyteller | Faster Dayo - Part 1 | Kill 5 PMCs with any 10-round mag in the same raid | L32 | Recoil control | `6aca8288a26d5245cb767413` | Audited | Fixed: listed magazines as weapons, so nothing counted; now 5 PMC kills in one raid with any 10-round magazine fitted (`50c77a1`). |
| L94 | Storyteller | Faster Dayo - Part 2 | Plant 3 stanag 60 round at different spots around reserve Top FLoor Red Gaurd Tower, Black Knight Rooftop Post,White Bishop Rooftop Mortar Position | L93 | Recoil control | `6aca8300a26d5245cb767416` | Needs check | Fixed: the three placements had no zone; now `L94_1`-`L94_3` in step order (`fc2e35a`). Step text still says "(wip, skip)". |
| L95 | Storyteller | Faster Dayo - Part 3 | Turn in 20x FIR 60-rounder AK mag (the ice cream cones one) | L94 | Recoil control | `6aca830da26d5245cb767419` | Audited | Typed Completion (`fc2e35a`). |
| L96 | Storyteller | The Auto Price - Part 1 | Get 5 headshot Scav kills on Woods with the M700 | L32 | Bolt action rifle levels | `6aca868aa26d5245cb767427` | Audited |  |
| L97 | Storyteller | The Auto Price - Part 2 | Reach lv3 rep with Price | L96 | Bolt action rifle levels | `6aca86c4a26d5245cb76742a` | Flagged | Fixed: asked for standing 3.0; now loyalty level 3 (`73da404`). Step text says "Reach lv. with Price". |
| L98 | Storyteller | The Auto Price - Part 3 | Get 4 headshot kills on raiders on Reserve with the AMX | L97 | Bolt action rifle levels | `6aca86cfa26d5245cb76742d` | Audited |  |
| L99 | Storyteller | Twenty Five Types of Ammo - Part 1 | Kill 10 PMCs on Interchange with pistols | L32 | Pistol levels | `6aca8948a26d5245cb767438` | Audited | Built: was an empty shell. 10 PMC pistol kills on Interchange, Pistol skill, [PH] text (`8de90da`). |
| L100 | Storyteller | Twenty Five Types of Ammo - Part 2 | Kill all 3 Goons with Pistols | L99 | Pistol levels |  | To build |  |
| L101 | Storyteller | Twenty Five Types of Ammo - Part 3 | Kill Killa with Deagle | L100 | Pistol levels |  | To build |  |
| L102 | Storyteller | Revolving Door - Part 1 | Kill 10 PMCs on Woods with Revolvers | L32 | Revolver levels |  | To build |  |
| L103 | Storyteller | Revolving Door - Part 2 | Kill 5 raiders with Revolvers | L102 | Revolver levels |  | To build |  |
| L104 | Storyteller | Revolving Door - Part 3 | Kill Tagilla with Revolvers | L103 | Revolver levels |  | To build |  |
| L105 | Storyteller | P-Chan - Part 1 | Kill 10 PMC in legs with SMG | L32 | SMG |  | To build |  |
| L106 | Storyteller | P-Chan - Part 2 | Kill 10 Raiders in legs with SMG | L105 | SMG |  | To build |  |
| L107 | Storyteller | P-Chan - Part 3 | Kill 2 Rogues with SMGs | L106 | SMG |  | To build |  |
| L108 | Storyteller | Gun - Part 1 | Kill 10 PMCs with M4C9 | L32 | Assault |  | To build |  |
| L109 | Storyteller | Gun - Part 2 | Kill Glukhar with iron sighted ARs | L108 | Assault |  | To build |  |
| L110 | Storyteller | Gun - Part 3 | Kill Priest with ARs | L109 | Assault |  | To build |  |
| L111 | Storyteller | Such Shoot, Many Pellet - Part 1 | Kill 5 Rouges with KS-23 | L32 | Shotgun |  | To build |  |
| L112 | Storyteller | Such Shoot, Many Pellet - Part 2 | Kill 10 PMCs with Sawed off Double Barrel | L111 | Shotgun |  | To build |  |
| L113 | Storyteller | Such Shoot, Many Pellet - Part 3 | Kill Shturmann with a Shotgun | L112 | Shotgun |  | To build |  |
| L114 | Storyteller | Tech Tips - Part 1 | Kill 10 Scavs with LMGs | L32 | LMG |  | To build |  |
| L115 | Storyteller | Tech Tips - Part 2 | Kill 20 Scavs with LMGs | L114 | LMG |  | To build |  |
| L116 | Storyteller | Tech Tips - Part 3 | Kill 10 PMCs with LMGS NO armor | L115 | LMG |  | To build |  |
| L117 | Storyteller | Balance Needed - Part 1 | Kill 10 PMCs with M14 | L32 | DMR |  | To build |  |
| L118 | Storyteller | Balance Needed - Part 2 | Kill Glukhar with M14 | L117 | DMR |  | To build |  |
| L119 | Storyteller | Balance Needed - Part 3 | Kill Schturmann with AK50 | L118 | DMR |  | To build |  |
| L120 | Storyteller | Ace's Legacy | Kill all bosses, transiting in between |  | Has to be really good |  | To build |  |

## Main story (Q)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| Q1 | StoryTeller | Enter Tarkov | Survive and Exctract Shoreline | L0 | 1500 XP, 1 kit worth of stuff | `69cc8e901fda896ea59b50f0` | Audited |  |
| Q2 | StoryTeller | Gathering Supplies | Find FIR 3 medical items, Find 1 drinks, Find 1 Food | Q1 | 2000 XP | `69cc918b2e86c03e1e51974a` | Audited |  |
| Q3 | StoryTeller | Making Contact | Place Beacon on top of weather station in reserve | Q1 | 2300 XP, Chimera | `69cc9aaa1c5ce40c22fa3a8a` | Audited |  |
| Q4 | Chimera | Welcome Back | Survive and Extract Customs | Q3 | 2000 XP, Hideout? if possible | `69cd62bf473d11f1646c2269` | Audited |  |
| Q5 | Chimera | Getting Ahead | Kill 5 scavs on customs | Q4 | 2500 XP, Scav gun barters on chimera | `69cd770045b0c8b5f47878a4` | Audited |  |
| Q6 | Chimera | Terrorgroup? | Find and turn in documents linked to product R&D and testing. On factory office first floor | Q5 | 3000 XP, 65,000 RUB | `69cd7b7345b0c8b5f47878ae` | Audited |  |
| Q7 | Chimera | Getting Connected | Kill 3 PMCs | Q4 | 2500 XP, Fence Quests (set on F1) | `69cd7bf545b0c8b5f47878b3` | Audited |  |
| Q8 | Chimera | Old Pals | Find and turn in FIR 2 Alcohol Bottles, 3 pack of smokes | Q6 | 4000 XP, Price unlock | `69cd7c9645b0c8b5f47878ba` | Audited | Fixed: added the designed 4000 XP (`2a74bda`). |
| Q9 | Chimera | Time to Get Settled | Find FIR 2 nuts, 2 bolts, toolset | Q6 | 2500XP, 500 USD, 500 EUR | `69ce8e2896b54ce3c6d1fa2d` | Audited | Design says 500 USD and 500 EUR; built with 250 each. Left as built. |
| Q10 | Chimera | Load-Bearing Citizen - Part 1 | Find and turn in FIR 2 weapons parts, 3 handguard, 2 grip, Find ground zero weapon bench, machine gun overwatching construction site | Q6 | 5000 XP | `69cedc2dd2a219c316eb1c1e` | Needs check | Fixed: had no start condition; unlocks after Q6 (`8869a47`). Zone `z_q10_gzbench` may be too high to reach. See Check in game. |
| Q11 | Chimera | Load-Bearing Citizen - Part 2 | Hand over: 2 ADAR fir, 1 M4 fir | Q10 | 4500 XP, unlock Atlas | `69cedf01e4cc2cc2742682e2` | Audited |  |
| Q12 | Chimera | Long Time, No See | Find and Turn in 1 Intel Folder | Q6 | 10000 XP, Unlock Xiaoming | `69cee1057c3c785e39999475` | Audited | Fixed: had no start condition; unlocks after Q6 (`8869a47`). |
| Q13 | Chimera | Timmy or Stimmy? | Find and Turn in 3 morphine | Q6 | 4800 XP, Unlock Needle | `69cee334142467411393bf91` | Audited |  |
| Q14 | Chimera | The Laboratory | Transit from Customs to Factory, Transit from Factory to Labs, Survive and Extract from Labs | LVL15 and Q6 | 5000 XP, Labs Card | `69f27eed7d8e3164fcee106a` | Audited |  |
| Q15 | Chimera | Big Brained | Find Documents regarding labs personnel. Streets terragroup office | Q14 | 6500 XP, 100k RUB | `69f2c4dc5154f1f35e108593` | Audited | Sheet: item spawn is a little glitchy |
| Q16 | Chimera | Routed | Plant Signal Booster on top floor of skeleton overlooking middle of customs | Q15 | 7500 XP, Weiss Unlock | `69f2c5c43a52d68c927c3264` | Audited |  |
| Q17 | Weiss | My Paradise | 6 PMC kills under effect of Obdolbos 1 stim | Q16 | 4000 XP, Trimidol | `69f2c9c8baa27486f24e1267` | Audited |  |
| Q18 | Weiss | My Cherry | Find Red Ledx near X-Ray room streets | Q17 | 6500 XP, Electrtical components x4 | `69f2cb5f01fd39ae97fc0277` | Audited |  |
| Q19 | Xiaoming | My Muse | Find box of Chinese Peptides in labs chem lab near dome. | Q18 | 7500 XP, 300k roubles | `69f2cc7ed59fdbab1391cce5` | Audited |  |
| Q20 | Chimera | Offering to the Eye | Check cultist activity: Woods sunken village, Shoreline cultist Church. Turn in 4 FIR Raven statues | Q19 | 5600 XP, Cultist Knife,Voron Unlock | `69f2ce6bd57bec8bb79b77e1` | Flagged | Step text says the church is on Shoreline; it should say Woods. |
| Q21 | Voron | An Eye Cannot Speak | Stash 2 Intelligence in shoreline resort cultist room. | Q20 | 6900 XP, Cultist Funko | `69f2d088179e524ac52d63b0` | Needs check | Zone `Q21` may be too high to reach. See Check in game. |
| Q22 | Voron | The Eye Looks Back | Retrieve Briefcase in the Reserve Bunker Command Offices | Lvl 25 and Q21 | Xp, FLIR Thermal | `6a04b54fee995153b15a3e70` | Audited |  |
| Q23 | Voron | The Case | Plant Golden Rooster, Lion, Cat, Horse, at woods cultist circle by checkpoint | Q22 | Xp, Key to Labrynth first door. | `6a04b6d9ee995153b15a3e7b` | Audited |  |
| Q24 | Voron | My Prayers Are Answered | Retrieve secure folder at woods cultist circle by checkpoint | Q23 |  | `6a07ab1f8ff25d06e48d31e3` | Audited | Sheet: in but broken/half state |
| Q25 | Voron | Daedalus' Curse | Hunt down Priest and retrieve a Keycard for Labyrinth, Find and Turn in Keycard (EDIT PRIEST LOOT) Guaranteed Spawn | Q24 | XP, Labrynth keycard itself and barters with Voron | `6a07ab808ff25d06e48d31e8` | Audited |  |
| Q26 | Chimera | Into The Maze | Find Photo Album in main research room | Q25 | Xp, 2 Bitcoins | `6a08bc51ba598c93d9c09fcc` | Audited |  |
| Q27 | Storyteller | Purgatory | Survive and Extract any map | Q26 | XP | `6a08be635562066cb549e1bc` | Audited |  |
| Q28 | Storyteller | Refusal | Kill 20 PMC | Q27 | XP, Demon Stim | `6a08bea35562066cb549e1c1` | Audited | Sheet: 28/29 must fail if other is completed |
| Q29 | Storyteller | Acceptance | Turn in 100 Items | Q28 | XP, Angel Stim | `6a08bf145562066cb549e1c7` | Audited |  |
| Q30 | Storyteller | Thank You For Playing | Turn in 1 RUB | Q28/27 | XP, 1 Bitcoin | `6a08bfb85562066cb549e1cb` | Audited |  |

## Chimera (C)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| C1 | Chimera | Deja-Vu | Scout locations in ground-zero. Terragroup Office, and Meat truck | Q3 | Chimera Initial ,c18 | `6a0a9e0bdbc8c9a772fad9be` | Audited | Sheet: Trader level .2 each quest; Unlock status: (complete) |
| C2 | Chimera | Brothers in Arms | Kill 3 Rogues on Lighthouse | C1 | XP, 100k RUB | `6a0a9f56dbc8c9a772fad9cc` | Audited | Design says 100k RUB; built with 50k. Left as built. |
| C3 | Chimera | Bird Hunting | Find Diary in helicopter reserver between dorms | C2 |  | `6a0aa03adbc8c9a772fad9d5` | Flagged | Text says Lighthouse, but the drive spawns on Reserve. |
| C4 | Chimera | Back to the Future | Plant a tarkone directors key outside of the locked door on Customs, plant a water room key outside of the dorms water room | C1 |  | `6a0aa34edbc8c9a772fad9e7` | Audited |  |
| C5 | Chimera | Currency Of War | F/T in 1 120 BP and 1 120 BT | C1 |  | `6a0aa18cdbc8c9a772fad9de` | Audited |  |
| C6 | Chimera | Loot Lord - Part 1 | Tool werehouse shoreline | C1 |  | `6a0aaf43ee68f3757a5c85e2` | Audited | Unlock status: (complete) |
| C7 | Chimera | Loot Lord - Part 2 | Train Depot Location (Bunks/PortaPotty) and Hidden Bunker Cultist Circle | C6 |  | `6a0ab08eee68f3757a5c85ec` | Audited |  |
| C8 | Chimera | Loot Lord - Part 3 | Rogue Hunt/ Sniper Hill spot | C7 |  | `6a0ab234ee68f3757a5c85f7` | Audited |  |
| C9 | Chimera | The Gungeon | Black Pawn Bunker(Hideout and weaponcrates) | C3 |  | `6a0ab2daee68f3757a5c8601` | Audited | Unlock status: 5ee234c386f77447ee650e32 |
| C10 | Chimera | Loot Lord - Part 4 | Get access to the locked loot room on labrynth and visit it | Q25 |  | `6a0ab38cee68f3757a5c860b` | Audited |  |
| C11 | Chimera | Meet God? | Kill Zrachy | L21 | AK-50 unlock and ammo | `6a0d21c5d47f367b5bed547a` | Audited | Fixed: start condition had no quest status; now Apex Predator 4 completed. .50 BMG M21 unlock given LL1 (`1230d6e`). |
| C12 | Chimera | Leg Up - Part 1 | Hand in any 2 FIR reflex/collimator sights (Legs tribute quest) | C11 | Legs Cosmetics | `6a0d22f0d47f367b5bed548b` | Audited | Unlocks after Hooligan Hunt 3, not C11 as designed. Left as built. |
| C13 | Chimera | Leg Up - Part 2 | Hand in any 2 FIR 5.45 AKs | C12 | 1st Wave Custom guns | `6a0d2447d47f367b5bed5496` | Audited |  |
| C14 | Chimera | Bi-Lingual - Part 1 | Kill PMC in legs with five seven quest where the text is Russian | LVL 20 | XP 110k Rouble | `6a0d274cd47f367b5bed54b7` | Audited |  |
| C15 | Chimera | Bi-Lingual - Part 2 | Kill Tagilla with UMP 45 | C14 | XP 110k Rouble | `6a0d281bd47f367b5bed54bf` | Audited |  |
| C16 | Chimera | Bi-Lingual - Part 3 | Turn in military Checkpoint key | C15 | XP 110k rouble | `6a0d2895d47f367b5bed54c7` | Audited | Fixed: trader was Prapor, so it showed there; now Chimera (`8edb1f6`). |
| C17 | Chimera | Bi-Lingual - Part 4 | Turn in Dorm Gaurd Desk Key | C16 | XP, SSA AP barter | `6a0d28fcd47f367b5bed54ce` | Flagged | Fixed: the SSA AP unlock had no offer; added one at 1,150 RUB, LL3 (`af19b7e`). Design says a barter. See Flags. |
| C18 | Chimera | Born to Shit, Forced to Wipe | Find 3 TP | C1 | 1 Awl | `6a0d2538d47f367b5bed54a3` | Audited | Fixed: trader was Prapor, so it showed there; now Chimera (`8edb1f6`). |
| C19 | Chimera | Family Jewels | Find 2 Nuts | C18 | 2 Bolts | `6a0d25a5d47f367b5bed54a9` | Audited |  |
| C20 | Chimera | Green Gold | Find 4 RAM Sticks | C8 | 1 bitcoin | `6a0d25fbd47f367b5bed54b1` | Audited | Unlocks after Loot Lord 4, not C8 as designed. Left as built. |

## Fence (F)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| F1 | Fence | Return to the City | Kill 4 PMC on Streets of Tarkov | Q7 | 3200 XP, .10 Fence Rep | `69cf0b9dd7d2715797a83dac` | Audited |  |
| F2 | Fence | Silent Arrival | Kill 2 Bear, 2 USEC with any suppressed weapon | F1 | 4000 XP, .20 Fence Rep | `69cf0c7c185a5729e3c907bf` | Audited |  |
| F3 | Fence | Public Recognition | Mark Old Gas Pumps, Military Check.,top floor red skel, and gaurd house middle of map military areas on Customs | F2 | 5000XP, .15 Fence Rep | `69d1ebe31e775b89a6e4b034` | Audited |  |
| F4 | Fence | Arrest Order | Leave documents case, labs keycard behind guard house in trash, near Crossroads on Customs | F3 | 2500 XP, .20 Fence Rep | `69d2ae36dcdcf1b2b24fefaf` | Audited |  |
| F5 | Fence | Prison Corridor | Mark the sewer corridor on Labs and in the locked kollontay room on streets | F4 | 3000 XP, .25 Fence Rep | `69d2b09e2c0d9a9e7d54f7c1` | Audited |  |
| F6 | Fence | Question of Freedom | Kill 4 Scavs, 4 PMCs | F5 | 4500 XP, .15 Fence Rep | `69d2b175f16f7b56dfcc29f6` | Audited |  |
| F7 | Fence | Kiss at the Gate | Visit 6 gates (or however many) on Streets of Tarkov | F6 | 3000 XP, .10 Fence Rep | `69d2b42386866406273700cb` | Audited |  |
| F8 | Fence | Mightnight Dreary | Kill 5 PMCs with DMRs at night on Woods | F7 | 6000 XP, .30 Fence Rep | `69d2b51e90a2aa5fe6baa113` | Audited | Registered for modded marksman rifles (`287d269`). |
| F9 | Fence | Weak and Weary | Survive 180s with a heavy bleed | F8 | 4000 XP, .20 Fence Rep | `69d2b662895cab8824541f2a` | Audited |  |
| F10 | Fence | Maxwell's Demon | Kill 1 PMC heasdshot, 1 torso, 1 left arm, 1 right arm, 1 left leg, 1 right leg, 1 stomach | F9 | 5000 XP, .30 Fence Rep | `69d2b794e60486f553169c9d` | Audited | Fixed: had no stomach step, and two leg steps had swapped text; now 7 steps matching their text (`2ebf040`). Standing 0.6, design 0.3. |
| F11 | Fence | Sacramentum | Plant 1 M4 on Woods cultist site 1, plant rooster in Shoreline cultist church | F10 | 6000 XP, .10 Fence Rep | `69d2b9049e4d407d16211b15` | Needs check | Fixed: its Shoreline zone shared the id `F5_2` with Prison Corridor's Streets zone; renamed `F11_2` (`04b4949`). |
| F12 | Fence | White Whale | Kill Kollantay | F11 | 12000 XP, .65 Fence Rep | `69d2ba09925d6e3592c00dd2` | Audited | Standing 0.95, design 0.65. Left as built. |
| F13 | Fence | Neronian Debasement | Give Fence 2000 USD, 2000 Euro, 1M RUB | F12 | 6500 XP, .40 Fence Rep | `69d2bbd26b10b0f1eed6a2ab` | Audited |  |
| F14 | Fence | The Crying of Lot 49 | Plant intelligence in the potted plant in Streets Financial locked room (financial institution locked office key) (F14_1), and the Streets real estate locked room (real estate agency office room key) (F14_2). Kill Reshala. Next, mark 4 different grafitti: Big skelly (F4_3), Outside of Mechanics (F14_4), Big Kitty (F14_5), Big Panda (F14_6) in customs, survive and extract. Then, in different raid, plant a gold chain at ambulance in backyard of Sanitars House in Shoreline (F14_7). Kill Sanitar. | F13 | 15000 XP, 2 Fence Rep | `69d2bd9aae6b63b659469685` | Audited |  |

## Atlas (A)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| A1 | Atlas | Screwed Up | Find 4 packs of screws | L31 | XP, unlock A3 | `6afeaa3204a15e3fbedf2f2f` | Built | Built: hand in 4 FIR packs of screws. Unlocks when Atlas does (Q11), not L31: L31 needs LL2 with Atlas, which needs Atlas quests first; Sheet: Trader Level .14 each quest; Unlock status: complete (initial Atlas) |
| A2 | Atlas | Deregulated Material | Handover 2x FIR military battery, 3x FIR OFZ shell | L31 | XP, unlock A4 | `6afeaaf15d1fdb09ec4b2e0d` | Built | Built: hand in 2 FIR tank batteries and 3 FIR OFZ shells. Unlocks with Atlas (Q11), not L31 (see A1); Unlock status: complete (initial Atlas) |
| A3 | Atlas | 500 Cigarettes | Drop 25 pack winstons at near-relax safe on Streets; Plant time 4s each |  |  | `6afeaaf28d3229c33858b35c` | Needs check | Built: leave 25 Wilston packs (4 s each) at new zone `A3`, the Cardinal apartments sauna on Streets: no safe found near the relaxation area, so the sauna is my reading of "near-relax" |
| A4 | Atlas | Close Contact | 2 PMC kills <20meters on Customs |  |  | `6afeaaf3c51077a145c068c1` | Built | Built: 2 PMC kills within 20 m on Customs |
| A5 | Atlas | Operation Benchmark | Mark 3 workbenches |  |  | `6afeab5a9e8e49793d89e912` | Needs check | Built: mark 3 workbenches with new zones `A5_1`, `A5_2` (Customs) and `A5_3` (Streets); unlocks after A3 and A4. Map and benches my choice |
| A6 | Atlas | Civil War on Drugs | Some amount of kills with a status effect |  |  | `6afeab5b8e5e78e85f08ab64` | Built | Built: 8 Scav kills while in pain (no painkillers). The design only said "kills with a status effect"; pain fits the anti-drug joke |
| A7 | Atlas | Fraternizing with the Enemy | Some combo quest with Xiaoming (X4-X6) - mark certain things "false intel" |  |  | `6afeab5c279977913a65a40b` | Built | Built: plant an Intelligence folder (the "false intel") at Xiaoming's D2 power room on Reserve, zone `X1`, which X1 also uses. The design wanted a combo with X4-X6; this is a simple stand-in. Check the design |
| A8 | Atlas | English Opening - Part 1 | Find and turn in quest item hidden at railway bridge extract on Shoreline | A7 | XP, unlock A9 | `6afeaba6250382525a4cbe0c` | Needs check | Built: find and hand in Atlas' Hidden Shipment, which now spawns at the railway bridge extract on Shoreline (new forced spawn, `shoreline_forced.json`) |
| A9 | Atlas | English Opening - Part 2 | Find and turn in quest items:  one at crash heli, one at USEC camp heli,on Lighthouse | A8 | XP, unlock A10 | `6afeaba7eefdf24932868cba` | Built | Built: find and hand in Secure Folder Case and Secure Folder Case 2 on Lighthouse (their spawns were already in `lighthouse_forced.json`) |
| A10 | Atlas | English Opening - Part 3 | Kill Tagilla, turn in FIR tagilla helm | A9 | XP, unlock Price | `6afeaba8a529a1a8f7e54840` | Built | Built: kill Tagilla and hand in a FIR Tagilla welding mask. The design's reward "unlock Price" was left out: Q8 already unlocks Price |
| A11 | Atlas | Paramilitary Pasta | Find the "spaghetti corner" - in the reserve food room. Plant a superwater. Then also kill "Spaghetti Joe" aka Gluhkar |  |  | `6afeac84d3cd2d70e7794577` | Needs check | Built: visit the existing zone `A11`, then leave a superwater (Canister with purified water) at new zone `A11_2` inside it, and kill Glukhar |
| A12 | Atlas | Training Arc | Level strength to 10 |  |  | `6afeac85ca77a07b0c58ff66` | Built | Built: reach Strength level 10 |
| A13 | Atlas | Filler Episode | Finding different figurines: 1x Tagilla, Killa, Reshala |  |  | `6afeac863a8863df58c72b03` | Built | Built: hand in 1 FIR Tagilla, Killa and Reshala figurine each |
| A14 | Atlas | Atlas of Worlds | Survive and extract once from every map, including Labs (not labyrinth) |  | Unlock all maps? Maybe Labs card? or labs barter? | `6afeac8722c2567678149911` | Built | Built: survive and extract from every map (Labyrinth excluded); rewards a Labs keycard. The design's "unlock all maps?" reward is left out |
| A15 | Atlas | 5ive Se7en | Get 25 kills with the fiveseven |  |  | `6afeac88cb4d67ecd471d942` | Built | Built: 25 kills of any kind with either Five-seveN |
| A16 | Atlas | Griner! | Kill 4 Scav with grenades, kill 4 PMCs with grenades |  |  | `6afeac896f9bce1302340a86` | Built | Built: 4 Scav and 4 PMC kills with hand grenades (the base game's Grenadier list) |
| A17 | Atlas | Form Over Function | Kill enemies with anime girl sight (or placeholder, specific reflex) |  | Some assort unlock | `6afeac8ac71e4a2ce2ffcb03` | Built | Built: 10 PMC kills with a Holosun HS401G5 fitted, a stand-in for the anime sight. Assort unlock reward left out (no offer chosen) |
| A18 | Atlas | Eyes On The Prize | Kill enemies with other anime girl sight - slightly harder (or placeholder, specific reflex) |  | Some assort unlock | `6afeac8b3b75d5799d2a8891` | Built | Built: 15 PMC kills with a Trijicon SRS-02 fitted, a stand-in for the second anime sight. Assort unlock reward left out (no offer chosen) |
| A19 | Atlas | Oh, The Games People Play | Hand over 3 FIR Tetris |  |  | `6afeac8dfd988952514ff7dc` | Built | Built: hand in 3 FIR Tetriz |
| A20 | Atlas | Frequent Flier | Plant 30 USD then plant marker, on each UAV on Shoreline |  |  | `6afead0e1fb1863eb6a1b86e` | Needs check | Built: at each of the two crashed MQ-1 drones on Shoreline, leave 30 USD and then place an MS2000 marker (new zones `A20_1`, `A20_2`, one per drone, used by both steps) |
| A21 | Atlas | Awkward Assembly - Part 1 | Gun builder quest, but with absurd (not hard just funny) requirements |  | Some assort unlock |  | Flagged | Not built: needs your list of the absurd parts for the build (WeaponAssembly checks exact mods/stats). A24 starts after A20 until these exist |
| A22 | Atlas | Awkward Assembly - Part 2 | Gun builder quest, but with absurd (not hard just funny) requirements |  | Some assort unlock |  | Flagged | Not built: needs your list of the absurd parts for the build (WeaponAssembly checks exact mods/stats). A24 starts after A20 until these exist |
| A23 | Atlas | Awkward Assembly - Part 3 | Gun builder quest, but with absurd (not hard just funny) requirements |  | Some assort unlock |  | Flagged | Not built: needs your list of the absurd parts for the build (WeaponAssembly checks exact mods/stats). A24 starts after A20 until these exist |
| A24 | Atlas | Light Reading | Hand in 3 FIR books. Then, mark 3 good reading spots on Streets (zone TBD). |  |  | `6afead9c40832f9c22c4b3e9` | Needs check | Built: hand in any 3 FIR books, then visit 3 reading spots on Streets: new zones `A24_1` (Pinewood Hotel lobby sofas), `A24_2` (School No. 30), `A24_3` (Razvedchikov 7 apartment). Starts after A20 because A21-A23 are not built |
| A25 | Atlas | Packet Loss | 10 headshots with DMR from >100m |  |  | `6afeada403382817c436d262` | Built | Built: 10 headshot kills with a marksman rifle from 100 m or more. Registered under the Marksman category so modded DMRs count |
| A26 | Atlas | Hitscan - Part 1 | 5 kills with snipers >100m |  |  | `6afeada548b82fcfce03670d` | Built | Built: 5 kills with a bolt-action rifle from 100 m or more. Registered under the Sniper category so modded bolt guns count |
| A27 | Atlas | Hitscan - Part 2 | 5 kills with snipers >250m |  |  | `6afeada6119f6aae527fe2f7` | Built | Built: 5 kills with a bolt-action rifle from 250 m or more. Registered under the Sniper category so modded bolt guns count |
| A28 | Atlas | Meet Your Maker | Visit the 3 water treatment roofs on (First,Second,Third) Lighthouse, then transit to Shoreline, find a package in the Heli at resort, and extract via Vehicle extract |  |  | `6afeadae24543451782f7b1a` | Needs check | Built: visit the existing roof zones `A28_1`-`A28_3` on Lighthouse, transit from Lighthouse (any transit counts: the game can't require the Shoreline one), find the Case For Atlas at the resort helicopter (new forced spawn in `shoreline_forced.json`), extract via the Shoreline vehicle extract, hand in the case |
| A29 | Atlas | God's Child, Herself | Retrieve Misato Bodypillow in the Relax Lounge |  |  |  | Skipped | Skipped: the item (Misato body pillow / Lance of Longinus) doesn't exist yet; make it under Custom quest items and I can build the quest |
| A30 | Atlas | All Comes Tumbling Down | Retrieve Lance of Longinus from the Red labs room |  |  |  | Skipped | Skipped: the item (Misato body pillow / Lance of Longinus) doesn't exist yet; make it under Custom quest items and I can build the quest |

## Xiaoming (X)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| X1 | Xiaoming | Háo Jiǔ Bu Jiàn | Mark D2 power room on reserve, kill 3 raiders, extract via D2 (not all same raid) | Q12 |  |  | To build | Sheet: Trader level .16 each quest |
| X2 | Xiaoming | Silk Road | Mark some stuff on the shoreline road, and train |  |  |  | To build |  |
| X3 | Xiaoming | Silk Road - Part 2 | Plant drug packages (stims) (Injector Cases?) at 5 locations around Shoreline |  |  |  | To build |  |
| X4 | Xiaoming | Better Without | Kill quest; ends up being Atlas's guys |  |  |  | To build |  |
| X5 | Xiaoming | Better Without - Part 2 | Kill quest (similar but distinct) - certain map/faction |  |  |  | To build |  |
| X6 | Xiaoming | Delay, Deny, Defend | Break into some healthcare building and somehow get back at Atlas |  |  |  | To build |  |
| X7 | Xiaoming | Eastern Medicine | Find some med things |  |  |  | To build |  |
| X8 | Xiaoming | Jade Idol | Whatever the living high not a crime part 2 items are, turn in FIR |  |  |  | To build |  |
| X9 | Xiaoming | Concussion Tested | Get headshot while wearing a Killa helm, survive and extract same raid |  |  |  | To build |  |
| X10 | Xiaoming | Transfer Student | Reach lv5 attention, lv7 intellect |  |  |  | To build |  |
| X11 | Xiaoming | Chain of Custody - Part 1 | Kill 4 raiders in the Reserve command bunker. Find and turn in questpackage in control room. |  |  |  | To build |  |
| X12 | Xiaoming | Chain of Custody - Part 2 | Mark 6 AA tanks on Reserve(First,Second.Third, Fourth,Fitfth,Sixth), then kill 4 Scavs in the command bunker |  |  |  | To build |  |
| X13 | Xiaoming | The Sun Never Sets - Part 1 | Reach lv3 with Price, turn in 1500 USD |  |  |  | To build |  |
| X14 | Xiaoming | The Sun Never Sets - Part 2 | Kill 3 BEAR on Lighthouse from 1900-2400, and turn in 3 BEAR dogtags |  |  |  | To build |  |
| X15 | Xiaoming | Better Red Than Dead | Plant Bitcoin in Asian themed resturant on streets |  |  |  | To build |  |
| X16 | Xiaoming | Triple Gem - Part 1 | (Kill Sanitar OR Kill Killa OR Kill any of the goons) and survive and extract, same raid |  |  |  | To build |  |
| X17 | Xiaoming | Triple Gem - Part 2 | Kill 10PMC with deagle. Turn in 10 dogtags. |  |  |  | To build |  |
| X18 | Xiaoming | Glory to CCP - Part 1 | Locate the location of Xiaoming's friend on Streets, survive and extract |  |  |  | To build |  |
| X19 | Xiaoming | Glory to CCP - Part 2 | Locate the place of work of Xiaoming's friend on Streets, find the package, survive and extract, turn in |  |  |  | To build |  |
| X20 | Xiaoming | Chinatown | Visit all the restaurants on Streets of Tarkov, and mark their front doors |  |  |  | To build |  |
| X21 | Xiaoming | Gotcha, Gatcha | Plant 3 gas cans and 3 matches in the Game Dev room on streets, including one in the locked room. Survive and extract. |  |  |  | To build |  |
| X22 | Xiaoming | Shishi | Turn in 2 FIR Lion statues |  | Leads to Chimera unlock somehow |  | To build |  |
| X23 | Xiaoming | Tourist - Part 1 | Visit multiple locked rooms on Customs (touring good loot spots): trailer park cabin, new gas locked room, dorms 314, customs office key |  |  |  | To build |  |
| X24 | Xiaoming | Tourist - Part 2 | Visit multiple locked rooms on Shoreline: tape key, W222, E306, HEP Station  Key |  |  |  | To build |  |
| X25 | Xiaoming | Tourist - Part 3 | Mark inside all Reserve marked rooms RBPKPM, rbbkmr,RBVOMR |  |  |  | To build |  |

## Price (P)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| P1 | Price | Stocking Up | Find 1 FIR Vodka, 1 FIR Whisky |  |  | `6afeaf7915530ff37817d47a` | Built | Built: hand in 1 FIR vodka (either Tarkovskaya) and 1 FIR Dan Jackiel whiskey. Starts when Q8 (which unlocks Price) is done; Sheet: Tradr Level .2 each quest |
| P2 | Price | Bad For You, Good For Me | Find 4 each type cigarette FIR |  |  | `6afeaf7a33a7614fcee60d8a` | Built | Built: hand in 4 FIR packs of each of the 4 cigarette brands |
| P3 | Price | Fish and Croutons | Turn in 3 Spratz and 3 Croutons |  |  | `6afeaf7b5d9bf914aedf59e7` | Built | Built: hand in 3 cans of sprats and 3 packs of rye croutons (either kind), not FIR (the design says "turn in") |
| P4 | Price | Priced In | Plant USD in the financial buildings (both) and the housing building, survive and extract same raid |  |  | `6afeaf7e14cddbc37e5b808e` | Needs check | Built: plant a stack of dollars at new zones `P4_1` (Tarbank, Primorskiy 52), `P4_2` (financial office, Nikitskaya 10), `P4_3` (Cardinal), then survive and extract on Streets. "Same raid" isn't enforced: the game keeps plants across raids |
| P5 | Price | Priced Out | Mark 1,5,9,13 IDEA cash registers on Interchange then kill 5 scavs in same session |  |  | `6afeaf7f2f64c84788159743` | Built | Built: mark the 4 IDEA registers (existing zones `P5_1`-`P5_4`), then kill 5 Scavs on Interchange |
| P6 | Price | New Money | Plant bitcoin on A streets ATM, survive and extract same raid |  |  | `6afeaf811df12fad34fa7faa` | Needs check | Built: plant a Physical Bitcoin at new zone `P6` (street ATM outside the Pinewood Hotel), then survive and extract on Streets |
| P7 | Price | In Another Life | Kill 20 PMCs |  |  | `6afeaf82f98010fd7f8a2add` | Built | Built: kill 20 PMCs anywhere |
| P8 | Price | Check Please | Pick up 2 packages on Interchange tables Kiba Outer and Kiba Inner. Found 3 FIR Iskra, 3 some beverage, 1 other beverage. |  |  | `6afeaf8392e87e3a862e3c5a` | Built | Built: hand in the 2 Packages on Interchange (forced spawns at the Kiba tables were already in place), 3 FIR Iskra, 3 FIR Ice Green tea and 1 FIR Pevko beer (the two beverages are my pick) |
| P9 | Price | Table for Two | Plant iskra/wine/vodka on tables in certain maps |  |  | `6afeaf86b4ce126563a95994` | Needs check | Built: plant wine at new zone `P9_1` (Beluga VIP room, Streets), an Iskra at `P9_2` (IDEA cafe, Interchange), vodka at `P9_3` (kitchen by the garages, Customs; the dorms are all inside a Jaeger plant zone). Maps and tables my choice |
| P10 | Price | Vlone Vever | Plant rigs in certain interchange store Avokado, Dino Clothes |  | unlock rig/gear sell | `6afeaf8746258ee20b284c22` | Needs check | Built: plant any chest rig at the existing zones `P10_1` (Avokado) and `P10_2` (Dino Clothes, whose negative scale was made positive). The design's "unlock rig/gear sell" reward is left out: what a trader buys is in its base file, not quest-locked |
| P11 | Price | Louis and Clarks | Get kills near Adiik Shoe Store |  | unlock backpack sell | `6afeaf89baacdcc253b108de` | Built | Built: 8 kills of any kind inside the existing kill zone `P11` (Adik). The "unlock backpack sell" reward is left out, as in P10 |
| P12 | Price | King of Burgers | Visit All burger spot locations in the game (Interchange) |  |  | `6afeaf8a8816157535cee653` | Needs check | Built: visit the existing zone `P12_1` (Burger Spot) and new zone `P12_2` (the west wing burger houses), the only two I found on Interchange |
| P13 | Price | Courtesy Call - Part 1 | Going around streets looking for a bowling alley (gta4 callback) |  | XP, P14 | `6afeaf8d32d5bcdb98c8c596` | Needs check | Built: visit new zones `P13_1` (Cinema), `P13_2` (Sportmarket), `P13_3` (Klimov mall) on Streets |
| P14 | Price | Courtesy Call - Part 2 | Going to customs looking for a bowling alley (Fortress) |  | XP, P15 | `6afeaf8f7757bef5904f3c49` | Built | Built: visit the existing zone `P14` (Fortress, Customs) |
| P15 | Price | Courtesy Call - Part 3 | Looking on interchange for a bowling ball in the mall |  | XP, P16 | `6afeaf907133ee697372bbf9` | Built | Built: visit the existing zone `P15` (Interchange mall). No bowling ball item exists, so this is a search-only step |
| P16 | Price | Courtesy Call - Part 4 | One final other map (looking for bowling alley with some sort of twist) Find Bowling Ball? |  | Good XP and good item |  | To build |  |
| P17 | Price | Last Call | Plant 1 vodka, 1 Beer, 1 Whiskey in bar on streets |  |  | `6afeaf9133bb6de0ee92554e` | Needs check | Built: plant a vodka, a Pevko and a Dan Jackiel at new zone `P17` (bar of the Brodion restopub, Zmeiskiy 3). Starts after P15 because P16 isn't built |
| P18 | Price | The Pie? It's Far Too Hot | First: find and hand in FIR: 1x piece of plexiglass, 1x IEA Mil-Optics KH/F 34mm one-piece magmount, and mark inside Dorms Marked/314 |  |  | `6afeaf921cf748b4f280276b` | Built | Built: hand in 1 FIR plexiglass and 1 FIR KH/F 34mm magmount, then mark inside dorm 314 (existing zone `P18`) |
| P19 | Price | The Good Stuff | Find and Turn in 3 Moonshine |  |  | `6afeaf948ff3d3b964b1c9d8` | Built | Built: hand in 3 FIR Fierce Hatchling moonshine |
| P20 | Price | Superman | Find and Turn in 5 Super Water |  |  | `6afeaf951086f357132cb2f2` | Built | Built: hand in 5 FIR canisters of purified water |

## Needle (N)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| N1 | Needle | Soylent Green | Use any ETG | Q13 |  |  | To build | Sheet: Trd LV .24 |
| N2 | Needle | Soylent Orange | Use any L1 |  |  |  | To build |  |
| N3 | Needle | I Can't Aim | Find and Turn In 1 Ledx | Q13 | Xp, Graphics Card |  | To build |  |
| N4 | Needle | Poor Mans Propitol | Find and Turn in 4 Adrenaline |  |  |  | To build |  |
| N5 | Needle | Blue Bloods | Find and turn in 2 Perftorin |  |  |  | To build |  |
| N6 | Needle | Alchemical Magic | Find and turn in 4 meds and 1 Propitol |  |  |  | To build |  |
| N7 | Needle | Marathon Dose - Part 1 | Transit from Ground Zero to Interchange, survive and extract | Q13 |  |  | To build |  |
| N8 | Needle | Marathon Dose - Part 2 | Transit from Interchange to Woods, survive and extract |  |  |  | To build |  |
| N9 | Needle | Marathon Dose - Part 3 | Transit from Woods to Shoreline, survive and extract |  |  |  | To build |  |
| N10 | Needle | Inject Me Scotty | Find and Turn in 3 CALOK |  |  |  | To build |  |
| N11 | Needle | It's Wrapping Time | Find and Turn in 2 Military Bandages |  |  |  | To build |  |
| N12 | Needle | Poppin a Proppie | Find and Turn in 3 Propitol |  |  |  | To build |  |
| N13 | Needle | Much Needed Shipment | Find the box containing injectors cases |  |  |  | To build |  |
| N14 | Needle | Drug Buddies | Kill Reshala and 10 scavs in one raid |  |  |  | To build |  |
| N15 | Needle | Soundcloud Soliloquy | Look for 50 Cent bibliography on Interchange room Toy/book store |  |  |  | To build |  |
| N16 | Needle | This Cranker is Crazy | Kill 5 Scavs on the island near the washed up tanker on Shoreline |  |  |  | To build |  |
| N17 | Needle | The Gig is Up | Plant Vodka on the stage in the theatre on streets |  |  |  | To build |  |

## Voron (V)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| V1 | Voron | Welcome to the Family - Part 1 | Kill 20 PMCs between 2200-600 |  | XP, Cultist Knife Barter |  | To build | Sheet: trd lvl .2 |
| V2 | Voron | Welcome to the Family - Part 2 | Plant 2 GPUS Dorms Marked |  | XP, 10 Power Supplies,Lighthouse Encoder, Hideout Craft to encode DSP |  | To build | Unlock status: XP, DSP, Radio Frequency thing, and hideout craft |
| V3 | Voron | Welcome to the Family - Part 3 | Visit the Lighthouse and talk to lightkeeper |  | XP, 1 GPU, |  | To build | Unlock status: XP, |
| V4 | Voron | Welcome to the Family - Part 4 | plant 1 bitcoin on woods bunker circle |  | XP, Digital secure DSP radio transmitter TEST THIS |  | To build |  |
| V5 | Voron | Welcome to the Family - Part 5 | Plant 1 Yellow Card, 1 injectors case on lighthouse marked room |  | XP |  | To build |  |
| V6 | Voron | Welcome to the Family - Part 6 | Kill 1 PMC with cultist Knife |  | XP, M80A1 barter |  | To build |  |
| V7 | Voron | The Eye Requires Meat | Visit 3 meat-related places on different mapos |  |  |  | To build |  |
| V8 | Voron | The Eye Requires Bliss | find and turn in 10 painkillers |  |  |  | To build |  |
| V9 | Voron | The Eye Requires Munitions - Part 1 | Find and turn in 3 boxes of 5.45 |  | XP, 7n40 barter |  | To build |  |
| V10 | Voron | The Eye Requires Munitions - Part 2 | find and turn in 3 boxes 7.62 |  | XP, 5.45 and 7.62 BP barter |  | To build |  |
| V11 | Voron | The Eye Requires Munitions - Part 3 | Find and turn in 3 boxes of .338 |  | XP, .338 barters |  | To build |  |
| V12 | Voron | The Eye Never Forgets | Hunt down a rouge Priest and 2 Cultists |  | XP, Pyramid Head Funko |  | To build |  |
| V13 | Voron | The Eye Requires Pickup - Part 1 | Pickup Sacrifice at Check 13 Marked room |  |  |  | To build |  |
| V14 | Voron | The Eye Requires Pickup - Part 2 | Pickup Sacrifice at woods sunken circle |  |  |  | To build |  |
| V15 | Voron | The Eye Requires Pickup - Part 3 | Pickup Sacrifice at Lighthouse Marked room |  |  |  | To build |  |
| V16 | Voron | The Eye Requires Pickup - Part 4 | Pickup Sacrifice at Reserve Control room marked key |  |  |  | To build |  |
| V17 | Voron | Reap The Wicked | Kill 20 PMCs with headshots |  |  |  | To build |  |
| V18 | Voron | Reap The Unfortunate | Kill 50 Scavs with Headshots |  |  |  | To build |  |
| V19 | Voron | Reap the Cursed | Kill tagilla and killa with headshots |  |  |  | To build |  |
| V20 | Voron | One Final Delivery | Pickup the Box from ground zero dead scientist and plant on shoreline in same raid |  |  |  | To build |  |

## Weiss (S)

| ID | Trader | Quest | Tasks | Unlocked by | Reward | Quest id | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| S1 | Weiss | Real Life Wacka Mole | Eliminate 5 rouges (Braindead Scientists) | Q16 | XP 300k Roubles | `6a1346a78c34ba4a387ccf8f` | To build | Sheet: trd lvl .2 |
| S2 | Weiss | Please Place the Sharpie - Part 1 | Mark Radioactive Barrels in Labs | S1 | Xp, 2 Labs Cards | `6a13478c8c34ba4a387ccf97` | To build | Sheet: NO LOCALES |
| S3 | Weiss | Please Place the Sharpie - Part 2 | Mark Terragroup office Security Station by Security Armory | S2 | Xp, 100k roubles | `6a1348ae8c34ba4a387ccf9f` | To build | Sheet: NO LOCALES |
| S4 | Weiss | Please Place the Sharpie - Part 3 | Mark Listening Post on Lighthouse in Upper Chalet | S3 | XP, M754, 3x-20x rifle scope | `6a13491a8c34ba4a387ccfa7` | To build | Sheet: NO LOCALES |
| S5 | Weiss | The Boogie Bomb - Part 1 | Find and Turn in 1 MCC | S1 | Xp, Labs Card, Res Unit Card | `6a1349bd8c34ba4a387ccfb0` | To build | Sheet: NO LOCALES |
| S6 | Weiss | The Boogie Bomb - Part 2 | Find and Turn in 1 Moonshine | S5 | Xp, 1 GPU | `6a134bde8c34ba4a387ccfb7` | To build | Sheet: NO LOCALES |
| S7 | Weiss | Smooth Brains - Part 1 | 5 Scav Kills on ground zero with Torrey Pines Logic T12W 30Hz thermal reflex sight | S1 | xp, 2 bottles of Vodka | `6a134dda8c34ba4a387ccfce` | To build | Sheet: NO LOCALES |
| S8 | Weiss | Smooth Brains - Part 2 | 15 Scav Kills on Ground Zero with Torrey Pines Logic T12W 30Hz thermal reflex sight | S7 | Xp,REAPIR Assort | `6a134cf28c34ba4a387ccfc4` | To build | Sheet: NO LOCALES |
| S9 | Weiss | The Humane Society's After Us! | Start ground zero transit to streets then extract | Lvl 30 | Hidden Reward (Bottle of Water) | `6a134ffc8c34ba4a387ccfdd` | To build | Sheet: NO LOCALES |
| S10 | Weiss | It Must Be The Illuminati! | plant 2 cameras, Bridge overlooking main street on streets, Office overlooking courtyard at terragroup | S9 | Xp, Bag of croutons | `6a1351028c34ba4a387ccfec` | To build | Sheet: NO LOCALES |
| S11 | Weiss | Super Trooper | Find and Turn in Laundry Detergent and Painkillers x3 | S10 | xp, 1 trimidol, 3 etg, 2 zagustin | `6a1351948c34ba4a387ccff3` | To build | Sheet: NO LOCALES |
| S12 | Weiss | Discombobulated - Part 1 | Find and turn in gyroscope 1 Labs By Robotic Arm | S11 | Xp, Roubles | `6a1352dc8c34ba4a387cd005` | To build | Sheet: NO LOCALES |
| S13 | Weiss | Discombobulated - Part 2 | Find and turn in gyroscope 2 Labs Res Unit (Weiss Room) | S12 | Xp, Roubles | `6a13536a8c34ba4a387cd00c` | To build | Sheet: NO LOCALES |
| S14 | Weiss | A Tasty Treat | Find Chemical on lighthouse Operating Room Key then transit to shoreline survive/extract with 1 pmc kill on shoreline | S10 | Xp, SIG Sauer ECHO1 1-2x30mm 30Hz thermal reflex scope assort | `6a1353b18c34ba4a387cd013` | To build | Sheet: NO LOCALES |
| S15 | Weiss | Side Effects | Kill 10 PMCS dialogue with JAR JAR BINKS MODE | S14 |  | `6a1355ac8c34ba4a387cd01f` | To build | Sheet: NO LOCALES |
| S16 | Weiss | Take the fight to the Humane Society | Kill 2 rouges on Labs | S10 | XP, LIMP | `6a1355ee8c34ba4a387cd025` | To build | Sheet: NO LOCALES |
| S17 | Weiss | Illuminate the Illuminati | Kill Goons | S10 | Xp, LIMP | `6a1356e48c34ba4a387cd02d` | To build | Sheet: NO LOCALES |
| S18 | Weiss | Brains Over Brawn | Go to labs and find documents Labs Manager Room | S13 | XP, 2 Labs Cards | `6a1357468c34ba4a387cd035` | To build | Sheet: NO LOCALES |
| S19 | Weiss | Brawn Over Brains | Kill 1 enemy will baton melee weapon | S18 | XP, Taiga melee(Hidden Reward) | `6a1359dd8c34ba4a387cd03e` | To build | Sheet: NO LOCALES |
| S20 | Weiss | My Masterpiece | Get 10 kills with REAPIR scope | S19 | Xp, Thermal Goggles with assort unlock (Flea Ban?) | `6a135a8c8c34ba4a387cd048` | To build | Sheet: NO LOCALES |
| S21 | Weiss | Ultimate Body | Turn in damaged Cult Plates | S20 | Xp, 2 Custom Armor Plates(Assort Unlock with Flea Ban) | `6a135b598c34ba4a387cd050` | To build | Sheet: NO LOCALES |

## In the repo but not in the sheet

| Trader | Quest | Quest id | Status | Notes |
|---|---|---|---|---|

## Custom quest items

| Item | Item id | Quest | In repo |
|---|---|---|---|
| R&D Files | `69b4d0c58cef59c5c553c4be` | Q6 | yes |
| Angel Stim |  |  | no |
| Labs Personel Files | `69b4d10f4891aa1c80b12b78` | Q15 | yes |
| Demon Stim |  |  | no |
| Signal Booster | `69b4d88a6b6e47c7c6093cc1` | Q16 | yes |
| Package | `69d2dbe0fd3c451b13480f2a` | X11 | yes |
| RedLedx | `69b4d15ea9ee50f56157c0cd` | Q18 | yes |
| Box of "legal" Chinese Peptides | `69b4f0e63266da01f06b0749` | Q19 | yes |
| The Briefcase | `69b4d251b8dba3688eda785f` | Q22 | yes |
| Secure Folder 0052 | `5938878586f7741b797c562f` | Q24 | no |
| Labrynth Photo Album Labrynth | `69b4d3bf669a409073138bb1` | Q26 | yes |
| Hidden Item | `69d2caf8c956d3a46db2e20e` | A8 | yes |
| 3 Folders | `69d2e75da92020043e7c085a` | A9_2 | yes |
|  | `69b4cb785480e8f6a36b20bc` | A9_1 | yes |
| Item In Heli | `69b4d5c725998b5696dcaf77` | A28 | yes |
| Spear of Longinus |  | A30 | no |
| Misato Bodypillow Relax |  | A29 | no |
| QuestPackage Control Room | `69b4cdc223d83be3907d58d5` | X10 | yes |
| Questpackage Streets | `69afb77d9bd526e56c0c34d7` | X20 | yes |
| Drive At Heli Lighthouse | `69b4cd55c28d7079a2e4372e` | C3 | yes |
| Package on Interchange | `69b4ccf02212c2e699d6652d` | P8 | yes |
| Gyroscope 1 Labs | `69b4eeaf8e3cf3d70d820d11` | S11 | yes |
| GyroScope 2 Labs | `69b4eef739f0077489484909` | S12 | yes |
| Chemical Lighthouse | `69b4efd4696fcee5c85250a4` | S14 | yes |
| Documents Labs | `69b4f058d7f63d42ceed6c9b` | S18 | yes |
| Custom Plates(Reward) | `69d44b9ec379dcfd2bf8de40` | S20 | yes |
| Diary on reserver heli | `69bb4430d567f0f75c4c02f6` | C3 | no |
| Sacrifice | `69d1f5c5d8786ae5cfe6c66d` | V13-V16 | yes |
| Final Sacrifice | `69d2cd74c9543f516911c29d` | V20 | yes |
| Injectors Case Shipment | `69bb46282a87c0f36004a252` | N13 | no |
| Find Rap Sheet | `69d2ca6e6c1d42de861b9745` | N15 | yes |
