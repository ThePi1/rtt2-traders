# Trader assorts

The stock of every RTT2 trader. This file is the source: `tools/build_assorts.py` turns it into `data/*-assort.json`, the quest assorts in `db/CustomQuests/*/QuestAssort` and the quests' `AssortmentUnlock` rewards. To change a trader's stock, edit a row here and run the script again:

```
python tools/build_assorts.py
```

Add `--check` to see what would change without writing anything.
- **What the script reads from each row:** LL, Cost, Limit and Unlock. A Cost written as an amount (`1,234 ₽`, `0.80 $`, `1,866 €`) is used as it is. A barter Cost is copied from the vanilla offer.
- **Parts:** each gun's and armour's parts come from its vanilla offer (the Offer column).
- **Unlocks:** an Unlock starting with a quest row (A5, Q16 ...) locks the item behind that quest.
- **Current stock:** rows marked "current RTT2 stock" are left as they are.
- **Re-running:** everything the script writes has an id starting with `a55027`, and each run replaces the last run's output.

**How the draft was made.** Each item is taken from vanilla SPT 4.1.6's traders (Prapor, Therapist, Skier, Peacekeeper, Mechanic, Ragman and Jaeger), at its lowest vanilla loyalty level. It keeps vanilla's price and buy limit. A set of rules then gives it one home trader (below). Ref's Arena stock is left out. Guns the Storyteller unlocks through the L lines, and items an RTT2 trader already sells, aren't repeated.

**Columns.**
- **Unlock:** a quest the item needs, as well as the LL. *Proposed* means from the plan. *Suggested* means vanilla locked the item behind a quest, so I picked one of the trader's own quests from the matching act. Change these freely.
- **From:** the vanilla trader and LL it was taken from.
- **Offer:** the vanilla assort id, used to copy the gun's attachments.

**Prices** are vanilla's. Atlas's are converted to dollars and Weiss's to euros at the handbook rates ($1 = 121 ₽, €1 = 134 ₽).

## Changes that ship with this batch

- [x] **Assorts:** built into the mod with `tools/build_assorts.py`.
- [x] **Rep and loyalty:** done. Quest standing, the LL template (level 15/25/35, standing 1/2/3), Atlas in dollars, Weiss in euros, and Xiaoming selling both currencies are all in the mod. See [Trader loyalty](QUESTS.md#trader-loyalty) in QUESTS.md for when each trader reaches each LL.
- [ ] **Voron's quest ammo:** V6 gives M80A1 (pen 60) at LL2. Vanilla never sells it. Move it to LL3 or LL4.

**When each LL arrives** (story quests only): LL2 comes at the end of Act I for Chimera and Price, and in Act II for the rest. LL3 comes in Act II or III. LL4 comes in Act III or IV, held back by the level-35 requirement. Weiss opens in Act II and Voron in Act III, so their LL1–3 come close together. Each draft item keeps its vanilla LL, so it arrives at about the same point in the story as it does in vanilla. *Suggested* quest unlocks are picked from the trader's own story quests that a player does while at that LL.

## Summary

| Trader | Theme | Currency | Opens | LL1 | LL2 | LL3 | LL4 | Quest-locked | Total |
|---|---|---|---|---|---|---|---|---|---|
| Chimera | Ex-Soviet military and hideout supplies | RUB | Act I (Q3) | 64 | 37 | 35 | 19 | 16 | 155 |
| Xiaoming | Export and grey-market guns, bulk ammo, currency | RUB (sells USD and EUR) | Act I (Q12) | 16 | 13 | 15 | 8 | 11 | 52 |
| Atlas | Gun parts and Western rifles | USD | Act I (Q11) | 35 | 28 | 24 | 22 | 40 | 109 |
| Price | Consumables, simple armour, hunting gear | RUB | Act I (Q8) | 88 | 59 | 58 | 45 | 37 | 250 |
| Needle | Stims, painkillers, pistol and SMG ammo, cheap guns | RUB | Act I (Q13) | 33 | 27 | 14 | 13 | 13 | 87 |
| Weiss | Medicine, Labs and experimental gear | EUR | Act II (after Q16) | 12 | 14 | 16 | 30 | 21 | 72 |
| Voron | Cult, stealth and high-penetration Russian ammo | RUB, mostly barters | Act III (after Q20) | 3 | 5 | 7 | 13 | 16 | 28 |

Storyteller keeps his 61 L-line gun unlocks and gets nothing new. The Laptop and Fence don't change.

**Routing rules** (first match wins):
- **Guns:** 9x39 → Voron. Export and civilian models (ADAR, VPO, AK-101/102, AK-545, MCX .300, Vector, RFB, TX-15, RD-704, Mk47, OP-SKS) → Xiaoming. Western service rifles (M4A1, 416, SCAR, G36, AUG, MDR, SA58, SPEAR, FN40GL) → Atlas. Kalashnikov family, ASh-12, RPD, RPK, SKS, SVT/AVT, Mosin and RShG-2 → Chimera. MP shotguns, Mossberg, TOZ-106, MP-18, Vepr-Hunter and signal pistols → Price. The rest of the pistols and SMGs → Needle.
- **Ammo:** 5.45, 7.62x39, 7.62x54R and 12.7x55 → Chimera, or Voron at 40+ penetration. 9x39 → Voron. 5.56, 7.62x51, .300 BLK, 6.8, .338 and 40x46 → Atlas. Pistol and SMG calibers → Needle. 12ga, 20ga, 23x75, .366 and flares → Price. Ammo boxes → Xiaoming.
- **Armour:** class 1–4 armour, plates, armoured helmets and helmet parts → Price. Class 5–6 → Weiss. Unarmoured headwear, glasses, headsets and face covers → Chimera. Rigs and backpacks → Price.
- **Medical:** stims and painkillers → Needle. Basic LL1 meds → Price. All other meds → Weiss. Food and drink → Price.
- **Night vision and thermals** → Weiss. **Grenades** → Chimera. **Knives** → Voron. **Dollars and euros** → Xiaoming.
- **Mods:** they go to the trader that took over their vanilla seller. Prapor → Chimera, Skier → Xiaoming, Jaeger → Price, Mechanic and Peacekeeper → Atlas. Everything else follows its vanilla seller the same way, with Therapist → Weiss and Ragman → Price.
- **Which mods stay:** every scope, sight, night-vision device and thermal stays. So does the cheapest mount for each scope that only fits on a mount. Of the other gun parts, each trader keeps **2 per LL**. Those are the best-fitting part from the first two of these categories the trader has at that LL: magazine, suppressor, tactical device, foregrip, stock, muzzle device, flashlight, pistol grip, bipod. "Best-fitting" means the part that fits the most items. The rest of vanilla's gun parts (barrels, handguards, receivers, gas blocks, rails and so on) are left out, so players find those in raid or on the flea.

## Chimera: Ex-Soviet military and hideout supplies

RUB. Opens in Act I (Q3). Takes over Prapor's guns, ammo and AK parts, and Ragman's headwear and apparel.

| LL | Item | Type | Cost | Limit | Unlock | From | tpl | Offer |
|---|---|---|---|---|---|---|---|---|
| 1 | KBP 9A-91 9x39 compact assault rifle | Gun | 41,300 ₽ | 2 |  | Prapor LL1 | `644674a13d52156624001fbc` | `686e346d6c2a18ed6b0eb1f9` |
| 1 | Kalashnikov AK-74M 5.45x39 assault rifle | Gun | 5× Apollo Soyuz cigarettes | 2 | Q16 Routed (proposed) | Prapor (moved) | `5ac4cd105acfc40016339859` | `686e346b6c2a18ed6b0eb0f4` |
| 1 | Kalashnikov AKM 7.62x39 assault rifle | Gun | 3× Can of beef stew (Small) | 1 |  | Prapor LL1 | `59d6088586f774275f37482f` | `686e34676c2a18ed6b0eaede` |
| 1 | Kalashnikov AKS-74U 5.45x39 assault rifle | Gun | 24,600 ₽ | 5 |  | Prapor LL1 | `57dc2fa62459775949412633` | `686e34636c2a18ed6b0eacd8` |
| 1 | Kalashnikov AKS-74UB 5.45x39 assault rifle | Gun | 70,800 ₽ | 5 | Q6 Terrorgroup? (suggested); vanilla: Debut | Prapor LL1 | `5839a40f24597726f856b511` | `686e34636c2a18ed6b0ead05` |
| 1 | Kalashnikov AKS-74UN 5.45x39 assault rifle | Gun | 35,500 ₽ | 2 |  | Prapor LL1 | `583990e32459771419544dd2` | `686e34646c2a18ed6b0ead7d` |
| 1 | Mosin 7.62x54R bolt-action rifle (Infantry) | Gun | 35,000 ₽ | 5 |  | Prapor LL1 | `5bfd297f0db834001a669119` | `686e34666c2a18ed6b0eae6e` |
| 1 | Mosin 7.62x54R bolt-action rifle (Sniper) | Gun | 5× D Size battery + 8× AA Battery | 1 |  | Prapor LL1 | `5ae08f0a5acfc408fb1398a1` | `686e34666c2a18ed6b0eae38` |
| 1 | TOZ Simonov SKS 7.62x39 carbine | Gun | 29,900 ₽ | 5 |  | Prapor LL1 | `574d967124597745970e7c94` | `686e34686c2a18ed6b0eaf94` |
| 1 | 40mm VOG-25 grenade | Ammo (pen 0) | 9,000 ₽ | 5 | Q4 Welcome Back (suggested); vanilla: Failed Setup | Mechanic LL1 | `5656eb674bdc2d35148b457c` | `64a2e6f09b9ad2b93b0cab9d` |
| 1 | 5.45x39mm PRS gs | Ammo (pen 13) | 65 ₽ | 1000 |  | Prapor LL1 | `56dff338d2720bbd668b4569` | `686e34636c2a18ed6b0ead03` |
| 1 | 5.45x39mm SP | Ammo (pen 15) | 80 ₽ | 400 |  | Skier LL1 | `56dff421d2720b5f5a8b4567` | `686e340f6c2a18ed6b0e8cf5` |
| 1 | 7.62x39mm HP | Ammo (pen 15) | 74 ₽ | 1000 |  | Jaeger LL1 | `59e4d3d286f774176a36250a` | `686e34266c2a18ed6b0e9567` |
| 1 | 5.45x39mm US gs | Ammo (pen 17) | 96 ₽ | 1000 |  | Prapor LL1 | `56dff4ecd2720b5f5a8b4568` | `686e34636c2a18ed6b0eacd6` |
| 1 | 9x39mm FMJ | Ammo (pen 17) | 147 ₽ | 300 |  | Jaeger LL1 | `6576f96220d53a5b8f3e395e` | `686e342a6c2a18ed6b0e9711` |
| 1 | 7.62x39mm SP | Ammo (pen 20) | 117 ₽ | 1000 |  | Skier LL1 | `64b7af734b75259c590fa895` | `686e34186c2a18ed6b0e9046` |
| 1 | 7.62x54mm R HP BT | Ammo (pen 26) | 200 ₽ | 1000 |  | Jaeger LL1 | `64b8f7c241772715af0f9c3d` | `686e342b6c2a18ed6b0e9751` |
| 1 | 7.62x54mm R SP BT | Ammo (pen 31) | 280 ₽ | 1000 | Q5 Getting Ahead (suggested); vanilla: Supplier | Skier LL1 | `64b8f7b5389d7ffd620ccba2` | `686e34146c2a18ed6b0e8e99` |
| 1 | 5.45x39mm HP | Ammo (pen 9) | 53 ₽ | 1000 |  | Jaeger LL1 | `56dff216d2720bbd668b4568` | `686e34206c2a18ed6b0e92d0` |
| 1 | PACA Soft Armor | Armour | 25,000 ₽ | 2 |  | current RTT2 stock | `5648a7494bdc2d9d488b4583` | `69fe2983d041b334be637ec7` |
| 1 | Transformer Bag | Backpack | 20,000 ₽ |  |  | current RTT2 stock | `56e33680d2720be2748b4576` | `6a05e58075949dd5a9bd76db` |
| 1 | F-1 hand grenade | Grenade | 1× Energy-saving lamp | 2 |  | Prapor LL1 | `5710c24ad2720bc3458b45a3` | `686e34626c2a18ed6b0eacb9` |
| 1 | M18 smoke grenade (Green) | Grenade | 3,675 ₽ | 5 |  | Jaeger LL1 | `617aa4dd8166f034d57de9c5` | `686e342d6c2a18ed6b0e97f1` |
| 1 | RDG-2B smoke grenade | Grenade | 4,745 ₽ | 4 |  | Prapor LL1 | `5a2a57cfc4a2826c6e06d44a` | `686e34666c2a18ed6b0eae36` |
| 1 | BEAR 5-Panel | Headwear | 3,500 ₽ |  |  | current RTT2 stock | `6765d79148caecc924f38301` | `6a05e61075949dd5a9bd76df` |
| 1 | BEAR Beanie | Headwear | 3,500 ₽ |  |  | current RTT2 stock | `67e343112c5ed0143e3c74eb` | `6a05e65275949dd5a9bd76e1` |
| 1 | BEAR baseball cap (Black) | Headwear | 2,028 ₽ | 10 |  | Ragman LL1 | `5b40e5e25acfc4001a599bea` | `686e34086c2a18ed6b0e892e` |
| 1 | BEAR baseball cap (Olive Drab) | Headwear | 1,916 ₽ | 10 |  | Ragman LL1 | `5aa2b87de5b5b00016327c25` | `686e34086c2a18ed6b0e88e8` |
| 1 | Bandana | Headwear | 2,215 ₽ | 10 |  | Ragman LL1 | `5b43271c5acfc432ff4dce65` | `686e34086c2a18ed6b0e8928` |
| 1 | MIL-TEC boonie hat | Headwear | 2,409 ₽ | 10 |  | Ragman LL1 | `5b4327aa5acfc400175496e0` | `686e34086c2a18ed6b0e890b` |
| 1 | UNTAR helmet | Headwear | 35,000 ₽ | 2 |  | current RTT2 stock | `5aa7d03ae5b5b00016327db5` | `6a05e69075949dd5a9bd76e2` |
| 1 | USEC 5-Panel | Headwear | 3,500 ₽ |  |  | current RTT2 stock | `679de71c3b47fe7f7537f7ff` | `6a05e60375949dd5a9bd76de` |
| 1 | USEC Beanie | Headwear | 3,500 ₽ |  |  | current RTT2 stock | `679d31ae779c471efb063dba` | `6a05e64975949dd5a9bd76e0` |
| 1 | USEC baseball cap (Black) | Headwear | 1,923 ₽ | 10 |  | Ragman LL1 | `5b40e61f5acfc4001a599bec` | `686e34086c2a18ed6b0e8914` |
| 1 | USEC baseball cap (Coyote) | Headwear | 1,823 ₽ | 10 |  | Ragman LL1 | `5aa2a7e8e5b5b00016327c16` | `686e34076c2a18ed6b0e8858` |
| 1 | Factory emergency exit key | Key | 75,000 ₽ | 1 |  | current RTT2 stock | `5448ba0b4bdc2d02308b456c` | `6a05e55775949dd5a9bd76da` |
| 1 | Tarcone Director's office key | Key | 2× Diary |  |  | current RTT2 stock | `5780d0532459777a5108b9a2` | `6a05e51375949dd5a9bd76d8` |
| 1 | TerraGroup Labs access keycard | Key | 600,000 ₽ |  |  | current RTT2 stock | `5c94bbff86f7747ee735c08f` | `69fd6144ae4cb6c08e1d9782` |
| 1 | Underground parking utility room key | Key | 4× Can of beef stew (Small) |  |  | current RTT2 stock | `658199972dc4e60f6d556a2f` | `6a05e85475949dd5a9bd76e7` |
| 1 | AI-2 medkit | Meds | 6,000 ₽ | 3 |  | current RTT2 stock | `5755356824597772cb798962` | `6a05e4cc75949dd5a9bd76d5` |
| 1 | Aseptic bandage | Meds | 2,000 ₽ | 5 |  | current RTT2 stock | `544fb25a4bdc2dfb738b4567` | `6a05e41f75949dd5a9bd76d2` |
| 1 | Aseptic bandage | Meds | 2,000 ₽ | 5 |  | current RTT2 stock | `544fb25a4bdc2dfb738b4567` | `6a05e44075949dd5a9bd76d3` |
| 1 | Esmarch tourniquet | Meds | 2,000 ₽ | 3 |  | current RTT2 stock | `5e831507ea0a7c419c2f9bd9` | `6a05e4ba75949dd5a9bd76d4` |
| 1 | Axion Kobra EKP-1S-03 reflex sight (Dovetail) | Mod: Collimator | 10,700 ₽ | 5 |  | Prapor LL1 | `6544d4187c5457729210d277` | `686e346b6c2a18ed6b0eb0e9` |
| 1 | Axion Kobra EKP-8-02 reflex sight (Dovetail) | Mod: Collimator | 10,200 ₽ | 5 |  | Prapor LL1 | `5947db3f86f77447880cf76f` | `686e34616c2a18ed6b0eac38` |
| 1 | NPZ PK1 Obzor dovetail reflex sight | Mod: Collimator | 7,600 ₽ | 5 |  | Prapor LL1 | `618a5d5852ecee1505530b2a` | `686e346a6c2a18ed6b0eb08d` |
| 1 | AK-74 5.45x39 6L23 30-round magazine | Mod: Magazine | 2,179 ₽ | 10 |  | Prapor LL1 | `55d480c04bdc2d1d4e8b456a` | `686e34626c2a18ed6b0eac50` |
| 1 | PU 3.5x ring scope mount | Mod: Mount | 1,205 ₽ | 5 |  | Prapor LL1 | `5b3f7c005acfc4704b4a1de8` | `686e34656c2a18ed6b0eadfd` |
| 1 | BelOMO PSO-1 4x24 scope | Mod: OpticScope | 19,400 ₽ | 4 |  | Prapor LL1 | `5c82342f2e221644f31c060e` | `686e34696c2a18ed6b0eafe1` |
| 1 | BelOMO PSO-1M2-1 4x24 scope | Mod: OpticScope | 2× Spark plug | 5 |  | Prapor LL1 | `576fd4ec2459777f0b518431` | `686e34666c2a18ed6b0eae55` |
| 1 | NPZ USP-1 Tyulpan 4x scope | Mod: OpticScope | 15,800 ₽ | 5 |  | Prapor LL1 | `5cf638cbd7f00c06595bc936` | `686e34686c2a18ed6b0eaf8f` |
| 1 | PU 3.5x riflescope | Mod: OpticScope | 13,400 ₽ | 5 |  | Prapor LL1 | `5b3f7c1c5acfc40dc5296b1d` | `686e34656c2a18ed6b0eadfa` |
| 1 | AK-74 wooden stock | Mod: Stock | 2,014 ₽ | 3 |  | Prapor LL1 | `5649b1c04bdc2d16268b457c` | `686e34616c2a18ed6b0eac4d` |
| 1 | 6B34 anti-fragmentation glasses | Other | 3,003 ₽ | 5 |  | Prapor LL1 | `5b432be65acfc433000ed01f` | `686e34666c2a18ed6b0eaebc` |
| 1 | Balaclava | Other | 2,874 ₽ | 10 |  | Ragman LL1 | `572b7f1624597762ae139822` | `686e34076c2a18ed6b0e8876` |
| 1 | Balaclava (White) | Other | 3,081 ₽ | 10 |  | Ragman LL1 | `675ac888803644528007b3f6` | `686e340c6c2a18ed6b0e8bf9` |
| 1 | Dundukk sport sunglasses | Other | 2,252 ₽ | 5 |  | Ragman LL1 | `5aa2b986e5b5b00014028f4c` | `686e34086c2a18ed6b0e8934` |
| 1 | GSSh-01 active headset | Other | 17,500 ₽ | 7 |  | Prapor LL1 | `5b432b965acfc47a8774094e` | `686e34666c2a18ed6b0eae2f` |
| 1 | Khorovod armband | Other | 1× Golden egg | 1 | Q7 Getting Connected (suggested); vanilla: Khorovod | Prapor LL1 | `67614b3ab8c060ebb204b106` | `677e990ea03da7967902c88f` |
| 1 | Lucky Scav Junk box | Other | 1,250,000 ₽ |  |  | current RTT2 stock | `5b7c710788a4506dec015957` | `69d2aa615292804e7db37250` |
| 1 | OPSMEN Earmor M32 headset | Other | 28,300 ₽ | 5 |  | Skier LL1 | `6033fa48ffd42c541047f728` | `686e34146c2a18ed6b0e8ebe` |
| 1 | Peltor ComTac II headset (OD Green) | Other | 50,000 ₽ | 2 |  | current RTT2 stock | `5645bcc04bdc2d363b8b4572` | `6a05e7e075949dd5a9bd76e6` |
| 1 | Signal Booster | Other | 1,000 ₽ |  | Q15 Big Brained (current) | current RTT2 stock | `69b4d88a6b6e47c7c6093cc1` | `69d4b6b85cd6d80bbface2be` |
| 1 | Tactical glasses | Other | 1,853 ₽ | 5 |  | Ragman LL1 | `557ff21e4bdc2d89578b4586` | `686e34076c2a18ed6b0e8835` |
| 2 | KBP VSK-94 9x39 rifle | Gun | 54,200 ₽ | 2 |  | Prapor LL2 | `645e0c6b3b381ede770e1cc9` | `686e346d6c2a18ed6b0eb22c` |
| 2 | Kalashnikov AK-74 5.45x39 assault rifle | Gun | 34,300 ₽ | 5 |  | Prapor LL2 | `5bf3e03b0db834001d2c4a9c` | `686e34666c2a18ed6b0eae57` |
| 2 | Kalashnikov AK-74N 5.45x39 assault rifle | Gun | 35,900 ₽ | 5 |  | Prapor LL2 | `5644bd2b4bdc2d3b4c8b4572` | `686e34646c2a18ed6b0ead64` |
| 2 | Kalashnikov AKMS 7.62x39 assault rifle | Gun | 41,900 ₽ | 5 |  | Prapor LL2 | `59ff346386f77477562ff5e2` | `686e34616c2a18ed6b0eac18` |
| 2 | Kalashnikov AKS-74N 5.45x39 assault rifle | Gun | 38,100 ₽ | 5 |  | Prapor LL2 | `5ab8e9fcd8ce870019439434` | `686e34656c2a18ed6b0eadb4` |
| 2 | RPK-16 5.45x39 light machine gun | Gun | 2× Bottle of Tarkovskaya vodka + 3× Can of beef stew (Small) | 1 | Q20 Offering to the Eye (suggested); vanilla: The Huntsman Path - Sellout | Prapor LL2 | `5beed0f50db834001c062b12` | `686e346c6c2a18ed6b0eb18b` |
| 2 | 12.7x55mm PS12A | Ammo (pen 10) | 240 ₽ | 200 |  | Prapor LL2 | `5cadf6e5ae921500113bb973` | `686e34666c2a18ed6b0eae43` |
| 2 | 5.45x39mm T gs | Ammo (pen 20) | 99 ₽ | 1000 |  | Prapor LL2 | `56dff4a2d2720bbd668b456a` | `686e34646c2a18ed6b0ead5c` |
| 2 | 5.45x39mm FMJ | Ammo (pen 24) | 108 ₽ | 1000 | Q20 Offering to the Eye (suggested); vanilla: Delivery From the Past | Prapor LL2 | `56dff0bed2720bb0668b4567` | `686e34646c2a18ed6b0ead75` |
| 2 | 7.62x39mm FMJ | Ammo (pen 26) | 153 ₽ | 400 |  | Prapor LL2 | `64b7af5a8532cf95ee0a0dbd` | `686e34696c2a18ed6b0eafff` |
| 2 | 12.7x55mm PS12 | Ammo (pen 28) | 393 ₽ | 120 |  | Prapor LL2 | `5cadf6ddae9215051e1c23b2` | `686e34666c2a18ed6b0eae46` |
| 2 | 9x39mm SP-5 gs | Ammo (pen 28) | 240 ₽ | 1000 |  | Prapor LL2 | `57a0dfb82459774d3078b56c` | `686e34636c2a18ed6b0eacd0` |
| 2 | 7.62x54mm R FMJ | Ammo (pen 36) | 295 ₽ | 120 |  | Prapor LL2 | `64b8f7968532cf95ee0a0dbf` | `686e346a6c2a18ed6b0eb06c` |
| 2 | LBT-1476A 3Day Pack (Woodland) | Backpack | 35,000 ₽ | 2 |  | current RTT2 stock | `618cfae774bb2d036a049e7c` | `6a05e5a475949dd5a9bd76dc` |
| 2 | M67 hand grenade | Grenade | 1× Zibbo lighter | 8 |  | Peacekeeper LL2 | `58d3db5386f77426186285a0` | `686e344f6c2a18ed6b0ea488` |
| 2 | RGD-5 hand grenade | Grenade | 1× Energy-saving lamp | 3 |  | Prapor LL2 | `5448be9a4bdc2dfd2f8b456a` | `686e34626c2a18ed6b0eac9f` |
| 2 | VOG-17 Khattabka improvised hand grenade | Grenade | 1× UZRGM grenade fuze | 5 |  | Mechanic LL2 | `5e32f56fcb6d5863cc5e5ee4` | `686e343e6c2a18ed6b0e9e63` |
| 2 | Zarya stun grenade | Grenade | 7,300 ₽ | 10 |  | Prapor LL2 | `5a0c27731526d80618476ac4` | `686e34676c2a18ed6b0eaec4` |
| 2 | 6B47 Ratnik-BSh helmet (EMR cover) | Headwear | 29,000 ₽ | 2 |  | current RTT2 stock | `5aa7cfc0e5b5b00015693143` | `6a05e75275949dd5a9bd76e5` |
| 2 | Beret (Olive Drab) | Headwear | 13,500 ₽ | 5 |  | Ragman LL2 | `5f60e784f2bcbb675b00dac7` | `686e340b6c2a18ed6b0e8af9` |
| 2 | MTEK FLUX Ballistic helmet (Olive Drab) | Headwear | 100,000 ₽ | 1 |  | current RTT2 stock | `6759655674aa5e0825040d62` | `6a05e6fd75949dd5a9bd76e4` |
| 2 | Stich Profi Chimera boonie hat | Headwear | 3,519 ₽ | 10 |  | Ragman LL2 | `60b52e5bc7d8103275739d67` | `686e340a6c2a18ed6b0e8a8b` |
| 2 | Tactical fleece beanie (Tan) | Headwear | 5,000 ₽ | 10 |  | Ragman LL2 | `5aa2ba19e5b5b00014028f4e` | `686e34086c2a18ed6b0e88b9` |
| 2 | UX PRO beanie | Headwear | 2,268 ₽ | 4 |  | Ragman LL2 | `5aa2ba46e5b5b000137b758d` | `686e34076c2a18ed6b0e8888` |
| 2 | Wilcox Skull Lock head mount | Headwear | 127,300 ₽ | 5 |  | Peacekeeper LL2 | `5a16bb52fcdbcb001a3b00dc` | `686e344d6c2a18ed6b0ea38a` |
| 2 | SR-2M KP-SR2 reflex sight | Mod: Collimator | 13,600 ₽ | 5 |  | Prapor LL2 | `62ff9920fe938a24c90c10d2` | `686e346d6c2a18ed6b0eb23d` |
| 2 | Valday Krechet reflex sight | Mod: Collimator | 14,400 ₽ | 5 |  | Prapor LL2 | `609a63b6e2ff132951242d09` | `686e346a6c2a18ed6b0eb075` |
| 2 | AK-74 5.45x39 6L23 30-round magazine (Plum) | Mod: Magazine | 2,289 ₽ | 10 |  | Prapor LL2 | `5cbdaf89ae9215000e5b9c94` | `686e34696c2a18ed6b0eafe4` |
| 2 | KMZ 1P59 dovetail mount | Mod: Mount | 1,908 ₽ | 5 |  | Prapor LL2 | `5d0a29ead7ad1a0026013f27` | `686e34686c2a18ed6b0eaf74` |
| 2 | NPZ 1P78-1 dovetail mount | Mod: Mount | 2,180 ₽ | 3 |  | Prapor LL2 | `618a75c9a3884f56c957ca1b` | `686e34696c2a18ed6b0eb04a` |
| 2 | NPZ 1P78-1 2.8x scope | Mod: OpticScope | 22,300 ₽ | 5 |  | Prapor LL2 | `618a75f0bd321d49084cd399` | `686e346a6c2a18ed6b0eb06f` |
| 2 | AK GP-25 accessory kit recoil pad | Mod: Stock | 4,051 ₽ | 4 | Q20 Offering to the Eye (suggested); vanilla: Gunsmith - Part 6 | Prapor LL2 | `5a0c59791526d8dba737bba7` | `686e34616c2a18ed6b0eac13` |
| 2 | Cold Fear infrared balaclava | Other | 4,793 ₽ | 4 |  | Ragman LL2 | `5ab8f39486f7745cd93a1cca` | `686e34076c2a18ed6b0e886a` |
| 2 | ESS Crossbow tactical glasses | Other | 3,885 ₽ | 5 |  | Ragman LL2 | `5d5fca1ea4b93635fd598c07` | `686e340a6c2a18ed6b0e89fb` |
| 2 | Key case | Other | 1× Physical Bitcoin | 1 |  | current RTT2 stock | `67d3ed3271c17ff82e0a5b0b` | `6a05e4fb75949dd5a9bd76d7` |
| 2 | MSA Sordin Supreme PRO-X/L headset | Other | 1× Veritas guitar pick | 2 |  | Ragman LL2 | `5aa2ba71e5b5b000137b758f` | `686e340b6c2a18ed6b0e8b54` |
| 2 | Shemagh (Tan) | Other | 4,485 ₽ | 7 |  | Ragman LL2 | `5b4325355acfc40019478126` | `686e34096c2a18ed6b0e89cb` |
| 3 | Degtyarev RPD 7.62x39 machine gun | Gun | 90,100 ₽ | 2 |  | Prapor LL3 | `6513ef33e06849f06c0957ca` | `686e346a6c2a18ed6b0eb0b3` |
| 3 | Degtyarev RPDN 7.62x39 machine gun | Gun | 1× Military circuit board + 1× Cyclon rechargeable battery | 5 |  | Mechanic LL3 | `65268d8ecb944ff1e90ea385` | `686e34476c2a18ed6b0ea142` |
| 3 | Kalashnikov AK-103 7.62x39 assault rifle | Gun | 47,800 ₽ | 5 |  | Prapor LL3 | `5ac66d2e5acfc43b321d4b53` | `686e34656c2a18ed6b0eae1c` |
| 3 | Kalashnikov AK-104 7.62x39 assault rifle | Gun | 53,900 ₽ | 5 |  | Prapor LL3 | `5ac66d725acfc43b321d4b60` | `686e34666c2a18ed6b0eae64` |
| 3 | Kalashnikov AK-105 5.45x39 assault rifle | Gun | 44,100 ₽ | 5 |  | Prapor LL3 | `5ac66d9b5acfc4001633997a` | `686e34646c2a18ed6b0ead98` |
| 3 | Kalashnikov AK-12 5.45x39 assault rifle | Gun | 3× Gunpowder "Eagle" + 4× Metal spare parts | 5 |  | Prapor LL3 | `6499849fc93611967b034949` | `686e346d6c2a18ed6b0eb204` |
| 3 | Kalashnikov AKMN 7.62x39 assault rifle | Gun | 48,200 ₽ | 5 |  | Prapor LL3 | `5a0ec13bfcdbcb00165aa685` | `686e34626c2a18ed6b0eac94` |
| 3 | Kalashnikov AKMSN 7.62x39 assault rifle | Gun | 43,100 ₽ | 5 |  | Prapor LL3 | `5abcbc27d8ce8700182eceeb` | `686e34666c2a18ed6b0eaeb1` |
| 3 | Tokarev AVT-40 7.62x54R automatic rifle | Gun | 2× Antique teapot | 1 | Q26 Into The Maze (suggested); vanilla: Glory to CPSU - Part 2 | Prapor LL3 | `6410733d5dd49d77bd07847e` | `686e346d6c2a18ed6b0eb1e6` |
| 3 | Tokarev SVT-40 7.62x54R rifle | Gun | 62,700 ₽ | 2 |  | Prapor LL3 | `643ea5b23db6f9f57107d9fd` | `686e34696c2a18ed6b0eafef` |
| 3 | 5.45x39mm PS gs | Ammo (pen 28) | 153 ₽ | 400 |  | Prapor LL3 | `56dff3afd2720bba668b4567` | `686e34626c2a18ed6b0eaca2` |
| 3 | 7.62x39mm US gzh | Ammo (pen 29) | 175 ₽ | 1000 |  | Prapor LL3 | `59e4d24686f7741776641ac7` | `686e34616c2a18ed6b0eac2c` |
| 3 | 7.62x39mm T-45M1 gzh | Ammo (pen 30) | 218 ₽ | 1000 |  | Prapor LL3 | `59e4cf5286f7741778269d8a` | `686e34636c2a18ed6b0ead2c` |
| 3 | 7.62x39mm PS gzh | Ammo (pen 35) | 262 ₽ | 300 | C10 Loot Lord - Part 4 (suggested); vanilla: The Punisher - Part 1 | Prapor LL3 | `5656d7c34bdc2d9d198b4587` | `686e34646c2a18ed6b0ead3f` |
| 3 | 5.56x45mm SSA AP | Ammo (pen 57) | 3,500 ₽ |  | C17 Bi-Lingual - Part 4 (current) | current RTT2 stock | `601949593ae8f707c4608daa` | `6afea93d54ebd5501d6dc2f9` |
| 3 | Model 7290 Flash Bang grenade | Grenade | 9,600 ₽ | 4 |  | Peacekeeper LL3 | `619256e5f8af2c1a4e1f5d92` | `686e34556c2a18ed6b0ea717` |
| 3 | Armasight NVG head strap | Headwear | 20,700 ₽ | 3 |  | Peacekeeper LL3 | `5c066ef40db834001966a595` | `686e344e6c2a18ed6b0ea43e` |
| 3 | Beret (Black) | Headwear | 18,300 ₽ | 5 |  | Ragman LL3 | `5f60e6403b85f6263c14558c` | `686e340a6c2a18ed6b0e8a52` |
| 3 | Beret (Blue) | Headwear | 26,400 ₽ | 3 |  | Ragman LL3 | `5f60e7788adaa7100c3adb49` | `686e340b6c2a18ed6b0e8aa9` |
| 3 | Kinda cowboy hat | Headwear | 1× KEKTAPE duct tape | 3 |  | Ragman LL3 | `5aa2b9ede5b5b000137b758b` | `686e34096c2a18ed6b0e89bf` |
| 3 | Valday PK-120 (1P87) reflex sight | Mod: Collimator | 21,000 ₽ | 7 |  | Prapor LL3 | `5c0505e00db834001b735073` | `686e34656c2a18ed6b0eadc2` |
| 3 | AK-12 5.45x39 30-round magazine | Mod: Magazine | 3,747 ₽ | 10 |  | Prapor LL3 | `5bed61680db834001d2c45ab` | `686e34656c2a18ed6b0eadce` |
| 3 | BelOMO PSO-1M2 4x24 scope | Mod: OpticScope | 20,500 ₽ | 5 |  | Prapor LL3 | `5c82343a2e221644f31c0611` | `686e34676c2a18ed6b0eaf1b` |
| 3 | KMZ 1P59 3-10x riflescope | Mod: OpticScope | 24,200 ₽ | 2 |  | Prapor LL3 | `5d0a3a58d7ad1a669c15ca14` | `686e34686c2a18ed6b0eaf35` |
| 3 | KMZ 1P69 3-10x riflescope | Mod: OpticScope | 27,500 ₽ | 2 |  | Prapor LL3 | `5d0a3e8cd7ad1a6f6a3d35bd` | `686e34676c2a18ed6b0eaecd` |
| 3 | AK-12 stock | Mod: Stock | 5,600 ₽ | 3 |  | Prapor LL3 | `5beec8c20db834001d2c465c` | `686e34676c2a18ed6b0eaf18` |
| 3 | Ghost half-mask | Other | 7,200 ₽ | 5 |  | Ragman LL3 | `6571bde39837cc51b800c212` | `686e340c6c2a18ed6b0e8b7a` |
| 3 | LShZ-2DTM cover (Black) | Other | 1,665 ₽ | 5 |  | Ragman LL3 | `5d6d3943a4b9360dbc46d0cc` | `686e340a6c2a18ed6b0e89fe` |
| 3 | Momex balaclava | Other | 3,565 ₽ | 10 |  | Ragman LL3 | `5b432f3d5acfc4704b4a1dfb` | `686e34086c2a18ed6b0e88a4` |
| 3 | NPP KlASS Condor glasses | Other | 1× Slim diary | 4 |  | Prapor LL3 | `603409c80ca681766b6a0fb2` | `686e346a6c2a18ed6b0eb07b` |
| 3 | Oakley SI Gascan glasses | Other | 6,200 ₽ | 5 |  | Ragman LL3 | `5d6d2e22a4b9361bd5780d05` | `686e34096c2a18ed6b0e89ea` |
| 3 | Ops-Core FAST RAC Headset | Other | 49,300 ₽ | 5 |  | Peacekeeper LL3 | `5a16b9fffcdbcb0176308b34` | `686e344d6c2a18ed6b0ea3d2` |
| 3 | Pyramex Proximity safety glasses | Other | 3,552 ₽ | 5 |  | Ragman LL3 | `5c0d32fcd174af02a1659c75` | `686e34076c2a18ed6b0e8879` |
| 3 | Safariland Liberator HP 2.0 Hearing Protection Headset (FDE) | Other | 47,000 ₽ | 5 |  | Ragman LL3 | `66b5f68de98be930d701c00e` | `686e340c6c2a18ed6b0e8c03` |
| 3 | Shemagh (Green) | Other | 4,727 ₽ | 10 |  | Ragman LL3 | `5ab8f85d86f7745cd93a1cf5` | `686e34076c2a18ed6b0e886d` |
| 4 | ASh-12 12.7x55 assault rifle | Gun | 2× Bottle of Tarkovskaya vodka | 2 | C10 Loot Lord - Part 4 (suggested); vanilla: Regulated Materials | Prapor LL4 | `5cadfbf7ae92152ac412eeef` | `686e34676c2a18ed6b0eaf26` |
| 4 | Kalashnikov PKM 7.62x54R machine gun | Gun | 1× TerraGroup "Blue Folders" materials | 1 | C10 Loot Lord - Part 4 (suggested); vanilla: Gunsmith - Part 25 | Mechanic LL4 | `64637076203536ad5600c990` | `686e34476c2a18ed6b0ea167` |
| 4 | RShG-2 72.5mm rocket launcher | Gun | 215,600 ₽ | 1 | Q26 Into The Maze (suggested); vanilla: The Art of Explosion | Prapor LL4 | `676bf44c5539167c3603e869` | `686e346e6c2a18ed6b0eb2a0` |
| 4 | 9x39mm SPP gs | Ammo (pen 35) | 480 ₽ | 220 |  | Prapor LL4 | `5c0d668f86f7747ccb7f13b2` | `686e34686c2a18ed6b0eaf77` |
| 4 | 5.45x39mm BT gs | Ammo (pen 37) | 589 ₽ | 120 |  | Prapor LL4 | `56dff061d2720bb5668b4567` | `686e34616c2a18ed6b0eac41` |
| 4 | Valday PS-320 1/6x scope | Mod: AssaultScope | 2× Bottle of Tarkovskaya vodka | 1 |  | Prapor LL4 | `5c0517910db83400232ffee5` | `686e34686c2a18ed6b0eaf8c` |
| 4 | ASh-12 vertical foregrip | Mod: Foregrip | 2,344 ₽ | 4 |  | Prapor LL4 | `5cda9bcfd7f00c0c0b53e900` | `686e34676c2a18ed6b0eaf15` |
| 4 | AK-12 5.45x39 early model 30-round magazine | Mod: Magazine | 4,702 ₽ | 5 |  | Prapor LL4 | `649ec30cb013f04a700e60fb` | `686e346b6c2a18ed6b0eb0ef` |
| 4 | Atomic Defense CQCM up armored ballistic mask (Black) | Other | 83,000 ₽ | 3 | Q26 Into The Maze (suggested); vanilla: Snatch | Ragman LL4 | `657089638db3adca1009f4ca` | `686e340b6c2a18ed6b0e8b47` |
| 4 | Deadly Skull mask | Other | 7,600 ₽ | 10 |  | Ragman LL4 | `5b432b6c5acfc4001a599bf0` | `686e34096c2a18ed6b0e89d7` |
| 4 | Death Shadow lightweight armored mask | Other | 57,900 ₽ | 3 |  | Ragman LL4 | `6570aead4d84f81fd002a033` | `686e340b6c2a18ed6b0e8b51` |
| 4 | Ghost balaclava | Other | 7,500 ₽ | 5 |  | Ragman LL4 | `5ab8f4ff86f77431c60d91ba` | `686e34096c2a18ed6b0e89d1` |
| 4 | Oakley SI Batwolf glasses | Other | 19,000 ₽ | 3 |  | Peacekeeper LL4 | `62a61c988ec41a51b34758d5` | `686e345a6c2a18ed6b0ea9ad` |
| 4 | Oakley SI M Frame safety glasses | Other | 5,200 ₽ | 5 |  | Ragman LL4 | `5c1a1cc52e221602b3136e3d` | `686e340a6c2a18ed6b0e8a35` |
| 4 | Peltor Tactical Sport headset | Other | 49,400 ₽ | 5 |  | Ragman LL4 | `5c165d832e2216398b5a7e36` | `686e34086c2a18ed6b0e8925` |
| 4 | RayBench Aviator glasses | Other | 7,400 ₽ | 10 |  | Ragman LL4 | `5d6d2ef3a4b93618084f58bd` | `686e340a6c2a18ed6b0e8a2c` |
| 4 | Shattered lightweight armored mask | Other | 8,300 ₽ | 7 |  | Ragman LL4 | `5b432b2f5acfc4771e1c6622` | `686e34086c2a18ed6b0e88e5` |
| 4 | TW EXFIL Peltor ComTac V headset (OD Green) | Other | 66,300 ₽ | 5 |  | Peacekeeper LL4 | `66b5f69ea7f72d197e70bcdb` | `686e345c6c2a18ed6b0eaa5e` |
| 4 | TW EXFIL Peltor ComTac VI headset (Coyote Brown) | Other | 74,600 ₽ | 5 |  | Peacekeeper LL4 | `66b5f6a28ca68c6461709ed8` | `686e345e6c2a18ed6b0eab11` |

## Xiaoming: Export and grey-market guns, bulk ammo, currency

RUB (sells USD and EUR). Opens in Act I (Q12). Takes over Skier's guns and parts, plus the bulk ammo boxes.

| LL | Item | Type | Cost | Limit | Unlock | From | tpl | Offer |
|---|---|---|---|---|---|---|---|---|
| 1 | ADAR 2-15 5.56x45 carbine | Gun | 45,300 ₽ | 4 |  | Skier LL1 | `5c07c60e0db834002330051f` | `686e34106c2a18ed6b0e8d40` |
| 1 | Molot Arms Simonov OP-SKS 7.62x39 carbine | Gun | 36,700 ₽ | 5 |  | Jaeger LL1 | `587e02ff24597743df3deaeb` | `686e34206c2a18ed6b0e92e7` |
| 1 | Molot Arms VPO-136 Vepr-KM 7.62x39 carbine | Gun | 31,200 ₽ | 5 |  | Skier LL1 | `59e6152586f77473dc057aa1` | `686e34106c2a18ed6b0e8d0f` |
| 1 | Molot Arms VPO-209 .366 TKM carbine | Gun | 28,400 ₽ | 5 |  | Skier LL1 | `59e6687d86f77411d949b251` | `686e340f6c2a18ed6b0e8cbb` |
| 1 | SIG Sauer ROMEO7 1x30 reflex sight (Prototype) | Mod: Collimator | 18,800 ₽ | 5 |  | Skier LL1 | `6477772ea8a38bb2050ed4db` | `686e34156c2a18ed6b0e8eea` |
| 1 | VOMZ Pilad P1x42 Weaver reflex sight | Mod: Collimator | 13,900 ₽ | 5 | X3 Silk Road - Part 2 (suggested); vanilla: Golden Swag | Skier LL1 | `584984812459776a704a82a6` | `686e340f6c2a18ed6b0e8cb6` |
| 1 | AK-74 "Saiga 545" 5.45x39 10-round magazine | Mod: Magazine | 1,575 ₽ | 20 |  | Skier LL1 | `55d4837c4bdc2d1d4e8b456c` | `686e34186c2a18ed6b0e9014` |
| 1 | M700 30mm integral ring scope mount | Mod: Mount | 3,570 ₽ | 3 |  | Jaeger LL1 | `5bfebc5e0db834001a6694e5` | `686e34216c2a18ed6b0e9343` |
| 1 | SIG Sauer ALPHA4 30mm ring scope mount | Mod: Mount | 6,100 ₽ | 5 |  | Peacekeeper LL1 | `6567e751a715f85433025998` | `686e345a6c2a18ed6b0ea9b3` |
| 1 | Burris FullField TAC30 1-4x24 30mm riflescope | Mod: OpticScope | 45,000 ₽ | 10 | X1 Háo Jiǔ Bu Jiàn (suggested); vanilla: Cocktail Tasting | Skier LL1 | `5b2388675acfc4771e1be0be` | `64a8578f0e9876295f0f83ed` |
| 1 | EOTech Vudu 1-6x24 30mm riflescope | Mod: OpticScope | 80,000 ₽ | 2 | X2 Silk Road (suggested); vanilla: Cocktail Tasting | Skier LL1 | `5b3b99475acfc432ff4dcbee` | `64a8578f0e9876295f0f83ef` |
| 1 | Vortex Razor HD Gen.2 1-6x24 30mm riflescope | Mod: OpticScope | 115,000 ₽ | 2 | X4 Better Without (suggested); vanilla: Cocktail Tasting | Skier LL1 | `618ba27d9008e4636a67f61d` | `64a8578f0e9876295f0f83ee` |
| 1 | Rotor 43 .366 TKM sound suppressor | Mod: Silencer | 28,800 ₽ | 3 |  | Skier LL1 | `5a9fbb74a2750c0032157181` | `686e34106c2a18ed6b0e8d32` |
| 1 | Arena poster | Other | 80,500 ₽ | 1 |  | Skier LL1 | `675a0288c3102563bd01c9c3` | `686e341b6c2a18ed6b0e9152` |
| 1 | Dollars | Other | 136 ₽ |  |  | current RTT2 stock | `5696686a4bdc2da3298b456a` | `6b1e5c0a0b0c4d5e6f708192` |
| 1 | Euros | Other | 158 ₽ |  |  | current RTT2 stock | `569668774bdc2da2298b4568` | `6b1e5c0a0b0c4d5e6f708193` |
| 2 | Kel-Tec RFB 7.62x51 rifle | Gun | 2× Gas analyzer | 1 |  | Skier LL2 | `5f2a9575926fd9352339381f` | `686e34196c2a18ed6b0e9063` |
| 2 | SAG AK-545 5.45x39 carbine | Gun | 72,100 ₽ | 3 |  | Skier LL2 | `628b5638ad252a16da6dd245` | `686e34186c2a18ed6b0e901f` |
| 2 | SAG AK-545 Short 5.45x39 carbine | Gun | 81,800 ₽ | 3 |  | Skier LL2 | `628b9c37a733087d0d7fe84b` | `686e341a6c2a18ed6b0e90f5` |
| 2 | SIG MCX .300 Blackout assault rifle | Gun | 1× Broken GPhone X smartphone + 1× Golden 1GPhone smartphone + 2× Broken GPhone smartphone | 2 |  | Skier LL2 | `5fbcc1d9016cce60e8341ab3` | `686e34136c2a18ed6b0e8e6c` |
| 2 | Soyuz-TM STM-9 Gen.2 9x19 carbine | Gun | 45,200 ₽ | 4 |  | Skier LL2 | `60339954d62c9b14ed777c06` | `686e34176c2a18ed6b0e8fc4` |
| 2 | 12/70 RIP ammo pack (5 pcs) | Ammo box | 1× T-Shaped plug | 12 | X8 Jade Idol (suggested); vanilla: Bullshit | Skier LL2 | `5c1127d0d174af29be75cf68` | `686e34116c2a18ed6b0e8d75` |
| 2 | 20/70 Dangerous Game Slug ammo pack (25 pcs) | Ammo box | 1× Pack of sodium bicarbonate | 4 |  | Jaeger LL2 | `67657773b83469e4f102dc27` | `686e342d6c2a18ed6b0e97fa` |
| 2 | 5.45x39mm BT gs ammo pack (30 pcs) | Ammo box | 2× Can of beef stew (Large) | 2 |  | Prapor LL2 | `57372c89245977685d4159b1` | `686e34666c2a18ed6b0eae94` |
| 2 | Kiba Arms Short Prism 2.5x scope | Mod: AssaultScope | 20,100 ₽ | 2 |  | Skier LL2 | `5c1cdd512e22161b267d91ae` | `686e34136c2a18ed6b0e8e67` |
| 2 | Leapers UTG reflex sight | Mod: Collimator | 14,000 ₽ | 5 |  | Skier LL2 | `6165ac8c290d254f5e6b2f6c` | `686e34166c2a18ed6b0e8f79` |
| 2 | OKP-7 reflex sight | Mod: Collimator | 16,900 ₽ | 4 |  | Skier LL2 | `570fd79bd2720bc7458b4583` | `686e340f6c2a18ed6b0e8cb0` |
| 2 | AK 7.62x39 Molot Arms 6P2.Sb-11 40-round magazine | Mod: Magazine | 2,862 ₽ | 10 |  | Skier LL2 | `59e5f5a486f7746c530b3ce2` | `686e340e6c2a18ed6b0e8c86` |
| 2 | AK-74 Hexagon 5.45x39 sound suppressor | Mod: Silencer | 45,300 ₽ | 5 | X9 Concussion Tested (suggested); vanilla: Humanitarian Supplies | Skier LL2 | `593d493f86f7745e6b2ceb22` | `686e34106c2a18ed6b0e8d58` |
| 3 | Kalashnikov AK-101 5.56x45 assault rifle | Gun | 38,300 ₽ | 5 |  | Mechanic LL3 | `5ac66cb05acfc40198510a10` | `686e34376c2a18ed6b0e9bd1` |
| 3 | Kalashnikov AK-102 5.56x45 assault rifle | Gun | 51,900 ₽ | 5 |  | Mechanic LL3 | `5ac66d015acfc400180ae6e4` | `686e34366c2a18ed6b0e9b69` |
| 3 | Lone Star TX-15 DML 5.56x45 carbine | Gun | 209,900 ₽ | 3 | X13 The Sun Never Sets - Part 1 (suggested); vanilla: Gunsmith - Part 16 | Skier LL3 | `5d43021ca4b9362eab4b5e25` | `686e34126c2a18ed6b0e8dda` |
| 3 | TDI KRISS Vector Gen.2 .45 ACP submachine gun | Gun | 89,400 ₽ | 3 | X14 The Sun Never Sets - Part 2 (suggested); vanilla: Friend From the West - Part 2 | Skier LL3 | `5fb64bc92b1b027b1f50bcf2` | `686e34146c2a18ed6b0e8ec3` |
| 3 | TDI KRISS Vector Gen.2 9x19 submachine gun | Gun | 96,700 ₽ | 3 | X15 Better Red Than Dead (suggested); vanilla: Vitamins - Part 2 | Skier LL3 | `5fc3f2d5900b1d5091531e57` | `686e34156c2a18ed6b0e8eec` |
| 3 | 20/70 Flechette ammo pack (25 pcs) | Ammo box | 1× Can of white salt | 2 |  | Jaeger LL3 | `676577166d874f6502106a21` | `686e342c6c2a18ed6b0e977f` |
| 3 | 20/70 TSS Armor Piercing Slug ammo pack (25 pcs) | Ammo box | 1× Repellent | 3 |  | Jaeger LL3 | `67657764c832f8c59c016d45` | `686e342d6c2a18ed6b0e980a` |
| 3 | 9x39mm SPP gs ammo pack (8 pcs) | Ammo box | 2× Insulating tape | 50 |  | Prapor LL3 | `5c12619186f7743f871c8a32` | `686e34656c2a18ed6b0eaddf` |
| 3 | SwampFox Trihawk Prism Scope 3x30 | Mod: AssaultScope | 34,300 ₽ | 2 |  | Skier LL3 | `626bb8532c923541184624b4` | `686e34196c2a18ed6b0e904c` |
| 3 | OKP-7 reflex sight (Dovetail) | Mod: Collimator | 19,500 ₽ | 4 |  | Skier LL3 | `57486e672459770abd687134` | `686e34106c2a18ed6b0e8d0a` |
| 3 | SIG Sauer ROMEO8T reflex sight | Mod: Collimator | 33,200 ₽ | 3 |  | Skier LL3 | `60a23797a37c940de7062d02` | `686e34156c2a18ed6b0e8f33` |
| 3 | AK 7.62x39 FAB Defense Ultimag 30R 30-round magazine | Mod: Magazine | 2,645 ₽ | 12 |  | Skier LL3 | `6272874a6c47bd74f92e2087` | `686e34186c2a18ed6b0e900b` |
| 3 | Nightforce Magmount 34mm ring scope mount with Ruggedized Accessory Platform | Mod: Mount | 6,600 ₽ | 5 |  | Jaeger LL3 | `5aa66c72e5b5b00016327c93` | `686e34226c2a18ed6b0e9372` |
| 3 | Hensoldt FF 4-16x56 34mm riflescope | Mod: OpticScope | 5× Dogtag USEC | 1 |  | Skier LL3 | `56ea70acd2720b844b8b4594` | `686e340f6c2a18ed6b0e8cf8` |
| 3 | AKM Hexagon 7.62x39 sound suppressor | Mod: Silencer | 49,100 ₽ | 4 |  | Skier LL3 | `593d489686f7745c6255d58a` | `686e340e6c2a18ed6b0e8c83` |
| 4 | Aklys Defense Velociraptor .300 Blackout assault rifle | Gun | 119,600 ₽ | 3 | X20 Chinatown (suggested); vanilla: Protect the Sky | Mechanic LL4 | `674d6121c09f69dfb201a888` | `686e34466c2a18ed6b0ea0e8` |
| 4 | CMMG Mk47 Mutant 7.62x39 assault rifle | Gun | 140,300 ₽ | 2 | X21 Gotcha, Gatcha (suggested); vanilla: Bullshit | Skier LL4 | `606587252535c57a13424cfd` | `686e34176c2a18ed6b0e8f99` |
| 4 | Rifle Dynamics RD-704 7.62x39 assault rifle | Gun | 102,300 ₽ | 3 |  | Mechanic LL4 | `628a60ae6b1d481ff772e9c8` | `686e34416c2a18ed6b0e9f86` |
| 4 | .338 Lapua Magnum FMJ ammo pack (20 pcs) | Ammo box | 3× Golden neck chain | 1 |  | Skier LL4 | `657023ccbfc87b3a3409320a` | `686e341d6c2a18ed6b0e91da` |
| 4 | EOTech XPS3-0 holographic sight | Mod: Collimator | 31,700 ₽ | 3 |  | Skier LL4 | `58491f3324597764bc48fa02` | `686e340e6c2a18ed6b0e8c50` |
| 4 | Vortex Razor AMG UH-1 holographic sight | Mod: Collimator | 29,700 ₽ | 5 |  | Skier LL4 | `59f9d81586f7744c7506ee62` | `686e340e6c2a18ed6b0e8c90` |
| 4 | AA-12 12ga 8-round magazine | Mod: Magazine | 6,500 ₽ | 10 |  | Skier LL4 | `66ffaab91f7492c901027bb8` | `686e341c6c2a18ed6b0e91a1` |
| 4 | AK Hexagon DTKP MK.2 7.62x39 sound suppressor | Mod: Silencer | 59,500 ₽ | 3 |  | Skier LL4 | `5e208b9842457a4a7a33d074` | `686e34156c2a18ed6b0e8f2a` |

## Atlas: Gun parts and Western rifles

USD. Opens in Act I (Q11). Takes over Mechanic and Peacekeeper: mods, NATO rifles and ammo.

| LL | Item | Type | Cost | Limit | Unlock | From | tpl | Offer |
|---|---|---|---|---|---|---|---|---|
| 1 | 20x1mm toy gun | Gun | 1× Tetriz portable game console | 3 |  | Mechanic LL1 | `66015072e9f84d5680039678` | `686e34426c2a18ed6b0e9ffa` |
| 1 | Colt M4A1 5.56x45 assault rifle | Gun | 3× PC CPU + 1× CPU fan | 1 | A5 Operation Benchmark (proposed) | Peacekeeper (moved) | `5447a9cd4bdc2dbd208b4567` | `686e34496c2a18ed6b0ea1e0` |
| 1 | Steyr AUG A1 5.56x45 assault rifle | Gun | 605 $ | 5 |  | Peacekeeper LL1 | `62e7c4fba689e8c9c50dfc38` | `686e34566c2a18ed6b0ea7bc` |
| 1 | 40x46mm M386 (HE) grenade | Ammo (pen 1) | 104 $ | 10 | A1 Screwed Up (suggested); vanilla: Failed Setup | Mechanic LL1 | `5ede475b549eed7c6d5c18fb` | `64a2e6f09b9ad2b93b0cab9f` |
| 1 | 5.56x45mm MK 255 Mod 0 (RRLP) | Ammo (pen 11) | 0.80 $ | 1000 |  | Peacekeeper LL1 | `59e6918f86f7746c9f75e849` | `686e344a6c2a18ed6b0ea28e` |
| 1 | .300 Whisper | Ammo (pen 14) | 1.07 $ | 1000 |  | Jaeger LL1 | `6196365d58ef8c428c287da1` | `686e34226c2a18ed6b0e93b1` |
| 1 | 7.62x51mm Ultra Nosler | Ammo (pen 15) | 1.20 $ | 1000 |  | Jaeger LL1 | `5e023e88277cce2b522ff2b1` | `686e34246c2a18ed6b0e9494` |
| 1 | 5.56x45mm HP | Ammo (pen 7) | 0.44 $ | 1000 |  | Jaeger LL1 | `59e6927d86f77411da468256` | `686e341f6c2a18ed6b0e9251` |
| 1 | Steyr AUG A1 STG77 1.5x optic sight | Mod: AssaultScope | 58.13 $ | 5 |  | Peacekeeper LL1 | `62ea7c793043d74a0306e19f` | `686e34566c2a18ed6b0ea7c5` |
| 1 | Holosun HS401G5 reflex sight | Mod: Collimator | 41 $ |  | A17 Form Over Function (current) | current RTT2 stock | `5b30b0dc5acfc400153b7124` | `6b0260f60c8879a85f4f056f` |
| 1 | Trijicon SRS-02 reflex sight | Mod: Collimator | 41 $ |  | A18 Eyes On The Prize (current) | current RTT2 stock | `5d2da1e948f035477b1ce2ba` | `6b0260f7d97439c255af88da` |
| 1 | Walther MRS reflex sight | Mod: Collimator | 41 $ |  | A17 Form Over Function (current) | current RTT2 stock | `570fd721d2720bc5458b4596` | `6b0260f60c8879a85f4f0573` |
| 1 | Aimpoint ACRO P-1 reflex sight | Mod: CompactCollimator | 145 $ | 4 |  | Peacekeeper LL1 | `616442e4faa1272e43152193` | `686e34556c2a18ed6b0ea729` |
| 1 | Aimpoint Micro H-2 reflex sight | Mod: CompactCollimator | 168 $ | 5 |  | Peacekeeper LL1 | `61657230d92c473c770213d7` | `686e34546c2a18ed6b0ea6c7` |
| 1 | Burris FastFire 3 reflex sight | Mod: CompactCollimator | 148 $ | 4 |  | Peacekeeper LL1 | `577d141e24597739c5255e01` | `686e344a6c2a18ed6b0ea285` |
| 1 | Trijicon RMR reflex sight | Mod: CompactCollimator | 41 $ |  | A18 Eyes On The Prize (current) | current RTT2 stock | `5a32aa8bc4a2826c6e06d737` | `6b0260f7d97439c255af88de` |
| 1 | AR-15 5.56x45 Magpul PMAG 20 GEN M3 STANAG 20-round magazine | Mod: Magazine | 26.88 $ | 10 |  | Peacekeeper LL1 | `5448c1d04bdc2dff2f8b4569` | `686e344d6c2a18ed6b0ea3c0` |
| 1 | Glock 9x19 SGM Tactical 50-round drum magazine | Mod: Magazine | 74 $ |  | A21 Awkward Assembly - Part 1 (current) | current RTT2 stock | `5a718f958dc32e00094b97e7` | `6b0262b2749cb622193b3004` |
| 1 | RPK-16 5.45x39 95-round drum magazine | Mod: Magazine | 298 $ |  | A23 Awkward Assembly - Part 3 (current) | current RTT2 stock | `5bed625c0db834001c062946` | `6b0262b57ea2ad1950912ed5` |
| 1 | SilencerCo Omega 45k .45 ACP sound suppressor | Mod: Silencer | 312 $ | 4 |  | Mechanic LL1 | `5fc4b9b17283c4046c5814d7` | `686e343f6c2a18ed6b0e9ee0` |
| 1 | Mosin Rifle ProMag Archangel OPFOR PRS chassis | Mod: Stock | 174 $ |  | A22 Awkward Assembly - Part 2 (current) | current RTT2 stock | `5bae13bad4351e00320204af` | `6b0262b35a80baad6c24abb8` |
| 1 | Ammunition case | Other | 2× Can of thermite + 2× Gunpowder "Eagle" | 1 | A2 Deregulated Material (suggested); vanilla: Gunsmith - Part 5 | Mechanic LL1 | `5aafbde786f774389d0cbc0f` | `686e34356c2a18ed6b0e9ae8` |
| 1 | Customs plan map | Other | 116 $ |  | A14 Atlas of Worlds (current) | current RTT2 stock | `5798a2832459774b53341029` | `6b0260e834d4ae9cb33d6b38` |
| 1 | Factory plan map | Other | 140 $ |  | A14 Atlas of Worlds (current) | current RTT2 stock | `574eb85c245977648157eec3` | `6b0260e834d4ae9cb33d6b34` |
| 1 | Gas analyzer | Other | 1× CPU fan | 1 |  | Mechanic LL1 | `590a3efd86f77437d351a25b` | `686e343f6c2a18ed6b0e9efc` |
| 1 | Interchange plan map | Other | 83 $ |  | A14 Atlas of Worlds (current) | current RTT2 stock | `5be4038986f774527d3fae60` | `6b0260e834d4ae9cb33d6b48` |
| 1 | Leatherman Multitool | Other | 96.50 $ | 3 |  | Mechanic LL1 | `544fb5454bdc2df8738b456a` | `686e342e6c2a18ed6b0e983a` |
| 1 | Pliers Elite | Other | 1× Pliers + 1× Nippers + 1× Round pliers | 2 |  | Mechanic LL1 | `5af04b6486f774195a3ebb49` | `686e34406c2a18ed6b0e9f2e` |
| 1 | Programmer's diary (Copy) | Other | 82.64 $ | 10 | A3 500 Cigarettes (suggested); vanilla: Friend from Norvinsk - Part 5 | Mechanic LL1 | `6866665cdf54e1190902df55` | `68a5c0144fffa5bd7a078e5c` |
| 1 | Shoreline Health Resort plan map | Other | 83 $ |  | A14 Atlas of Worlds (current) | current RTT2 stock | `5a80a29286f7742b25692012` | `6b0260e834d4ae9cb33d6b44` |
| 1 | Shoreline plan map | Other | 165 $ |  | A14 Atlas of Worlds (current) | current RTT2 stock | `5a8036fb86f77407252ddc02` | `6b0260e834d4ae9cb33d6b40` |
| 1 | Signal Jammer | Other | 144 $ | 10 | A4 Close Contact (suggested); vanilla: Signal - Part 3 | Mechanic LL1 | `5ac78a9b86f7741cca0bbd8d` | `686e34336c2a18ed6b0e9a33` |
| 1 | Toolset | Other | 1× Pliers + 1× Screwdriver + 1× Wrench + 1× Insulating tape + 1× Construction measuring tape | 2 |  | Mechanic LL1 | `590c2e1186f77425357b6124` | `686e34386c2a18ed6b0e9c3c` |
| 1 | WI-FI Camera | Other | 284 $ | 5 | A5 Operation Benchmark (suggested); vanilla: Informed Means Armed | Mechanic LL1 | `5b4391a586f7745321235ab2` | `686e34376c2a18ed6b0e9bdc` |
| 1 | Woods plan map | Other | 107 $ |  | A14 Atlas of Worlds (current) | current RTT2 stock | `5900b89686f7744e704a8747` | `6b0260e834d4ae9cb33d6b3c` |
| 2 | DS Arms SA58 7.62x51 assault rifle | Gun | 3× Damaged hard drive + 2× RAM stick | 1 | A12 Training Arc (suggested); vanilla: Overpopulation | Peacekeeper LL2 | `5b0bbe4e5acfc40dc528a72d` | `686e344e6c2a18ed6b0ea406` |
| 2 | FN SCAR-L 5.56x45 assault rifle (FDE) | Gun | 975 $ | 2 | A13 Filler Episode (suggested); vanilla: Revision - Streets of Tarkov | Peacekeeper LL2 | `618428466ef05c2ce828f218` | `686e34566c2a18ed6b0ea79d` |
| 2 | HK G36 5.56x45 assault rifle | Gun | 510 $ | 4 |  | Peacekeeper LL2 | `623063e994fc3f7b302a9696` | `686e34586c2a18ed6b0ea8b5` |
| 2 | .338 Lapua Magnum TAC-X | Ammo (pen 18) | 5.90 $ | 80 |  | Jaeger LL2 | `5fc382b6d6fa9c00c571bbc3` | `686e34236c2a18ed6b0e9435` |
| 2 | 5.56x45mm M856 | Ammo (pen 18) | 0.98 $ | 1000 |  | Peacekeeper LL2 | `59e68f6f86f7746c9f75e846` | `686e344a6c2a18ed6b0ea28b` |
| 2 | .300 Blackout V-Max | Ammo (pen 20) | 1.52 $ | 210 |  | Skier LL2 | `6196364158ef8c428c287d9f` | `686e34156c2a18ed6b0e8f12` |
| 2 | 5.56x45mm FMJ | Ammo (pen 23) | 1.16 $ | 300 | A9 English Opening - Part 2 (suggested); vanilla: Tigr Safari | Peacekeeper LL2 | `59e6920f86f77411d82aa167` | `686e34576c2a18ed6b0ea829` |
| 2 | 5.56x45mm Warmageddon | Ammo (pen 3) | 1.16 $ | 150 | A10 English Opening - Part 3 (suggested); vanilla: Humanitarian Supplies | Peacekeeper LL2 | `5c0d5ae286f7741e46554302` | `686e34556c2a18ed6b0ea6d7` |
| 2 | 7.62x51mm TCW SP | Ammo (pen 30) | 1.62 $ | 1000 |  | Skier LL2 | `5e023e6e34d52a55c3304f71` | `686e34136c2a18ed6b0e8e7b` |
| 2 | ELCAN SpecterDR 1x/4x scope (FDE) | Mod: AssaultScope | 2× SSD drive | 1 |  | Mechanic LL2 | `57aca93d2459771f2c7e26db` | `686e34406c2a18ed6b0e9f19` |
| 2 | HK G36 Hensoldt HKV 3x carry handle | Mod: AssaultScope | 84.96 $ | 5 |  | Peacekeeper LL2 | `622b4d7df9cfc87d675d2ded` | `686e345b6c2a18ed6b0ea9d4` |
| 2 | HK G36 Hensoldt HKV ZF 1.5x carry handle | Mod: AssaultScope | 76.02 $ | 5 |  | Peacekeeper LL2 | `622b4f54dc8dcc0ba8742f85` | `686e34586c2a18ed6b0ea89b` |
| 2 | SIG Sauer BRAVO4 4x30 scope | Mod: AssaultScope | 1× Bottle of Dan Jackiel whiskey | 2 |  | Peacekeeper LL2 | `57adff4f24597737f373b6e6` | `686e34516c2a18ed6b0ea547` |
| 2 | Trijicon ACOG TA11D 3.5x35 scope | Mod: AssaultScope | 210 $ | 5 |  | Peacekeeper LL2 | `59db7e1086f77448be30ddf3` | `686e344a6c2a18ed6b0ea297` |
| 2 | Aimpoint CompM4 reflex sight | Mod: Collimator | 225 $ | 4 |  | Peacekeeper LL2 | `5c7d55de2e221644f31bff68` | `686e344f6c2a18ed6b0ea485` |
| 2 | Aimpoint PRO reflex sight | Mod: Collimator | 190 $ | 4 |  | Peacekeeper LL2 | `61659f79d92c473c770213ee` | `686e34556c2a18ed6b0ea72f` |
| 2 | Hensoldt RV red dot sight | Mod: Collimator | 71.54 $ | 5 |  | Peacekeeper LL2 | `622efbcb99f4ea1a4d6c9a15` | `686e345b6c2a18ed6b0ea9c8` |
| 2 | Aimpoint Micro T-1 reflex sight | Mod: CompactCollimator | 215 $ | 5 |  | Peacekeeper LL2 | `58d399e486f77442e0016fe7` | `686e34486c2a18ed6b0ea1bc` |
| 2 | Leupold DeltaPoint Reflex Sight | Mod: CompactCollimator | 162 $ | 4 |  | Peacekeeper LL2 | `58d268fc86f774111273f8c2` | `686e344d6c2a18ed6b0ea3bd` |
| 2 | SIG Sauer ROMEO4 reflex sight | Mod: CompactCollimator | 191 $ | 3 | A15 5ive Se7en (suggested); vanilla: Fishing Gear | Peacekeeper LL2 | `5b3116595acfc40019476364` | `686e344e6c2a18ed6b0ea3fa` |
| 2 | AK-74 5.45x39 Magpul PMAG 30 GEN M3 30-round magazine | Mod: Magazine | 23.77 $ | 10 |  | Peacekeeper LL2 | `5aaa4194e5b5b055d06310a5` | `686e344e6c2a18ed6b0ea42a` |
| 2 | SIG Sauer SRD9 9x19 sound suppressor | Mod: Silencer | 256 $ | 3 |  | Peacekeeper LL2 | `5c6165902e22160010261b28` | `686e34526c2a18ed6b0ea590` |
| 2 | Ballistic plate case | Other | 6,198 $ | 1 | A11 Paramilitary Pasta (suggested); vanilla: Gunsmith - Old Friend's Request | Mechanic LL2 | `67600929bd0a0549d70993f6` | `686e34476c2a18ed6b0ea183` |
| 2 | Physical Bitcoin | Other | 2× Tetriz portable game console + 2× GreenBat lithium battery | 1 |  | Mechanic LL2 | `59faff1d86f7746c51718c9c` | `686e34356c2a18ed6b0e9aeb` |
| 2 | Secure container Alpha | Other | 7,566 $ | 1 |  | Peacekeeper LL2 | `544a11ac4bdc2d470e8b456a` | `686e34496c2a18ed6b0ea22c` |
| 2 | Secure container Beta | Other | 1× 6-STEN-140-M military battery + 3× Iridium military thermal vision module + 3× Virtex programmable processor + 5× Military cable | 1 |  | Peacekeeper LL2 | `5857a8b324597729ab0a0e7d` | `686e344d6c2a18ed6b0ea3cc` |
| 2 | Weapon case | Other | 5× Physical Bitcoin | 1 |  | Mechanic LL2 | `59fb023c86f7746d0d4b423c` | `686e34386c2a18ed6b0e9c36` |
| 2 | Working LCD | Other | 2× Broken LCD | 10 |  | Mechanic LL2 | `5d1b304286f774253763a528` | `686e343a6c2a18ed6b0e9cf6` |
| 3 | Desert Tech MDR 5.56x45 assault rifle | Gun | 962 $ | 2 |  | Peacekeeper LL3 | `5c488a752e221602b412af63` | `686e34516c2a18ed6b0ea572` |
| 3 | FN SCAR-H 7.62x51 assault rifle (FDE) | Gun | 2× Secure magnetic tape cassette + 1× Flat screwdriver (Long) | 1 |  | Mechanic LL3 | `6165ac306ef05c2ce828ef74` | `686e343e6c2a18ed6b0e9e9d` |
| 3 | FN SCAR-L 5.56x45 assault rifle | Gun | 833 $ | 3 |  | Peacekeeper LL3 | `6184055050224f204c1da540` | `686e34556c2a18ed6b0ea700` |
| 3 | HK 416A5 5.56x45 assault rifle | Gun | 828 $ | 2 | A17 Form Over Function (suggested); vanilla: Wet Job - Part 3 | Peacekeeper LL3 | `5bb2475ed4351e00853264e3` | `686e344e6c2a18ed6b0ea41c` |
| 3 | Steyr AUG A3 5.56x45 assault rifle | Gun | 620 $ | 3 |  | Peacekeeper LL3 | `63171672192e68c5460cebc5` | `686e345e6c2a18ed6b0eab3b` |
| 3 | Steyr AUG A3 5.56x45 assault rifle (Black) | Gun | 710 $ | 3 |  | Peacekeeper LL3 | `6718817435e3cfd9550d2c27` | `686e345c6c2a18ed6b0eaa51` |
| 3 | .300 Blackout BCP FMJ | Ammo (pen 30) | 2.74 $ | 150 |  | Skier LL3 | `5fbe3ffdf8b6a877a729ea82` | `686e34126c2a18ed6b0e8dfc` |
| 3 | 5.56x45mm M855 | Ammo (pen 31) | 1.61 $ | 1000 |  | Peacekeeper LL3 | `54527a984bdc2d4e668b4567` | `686e344a6c2a18ed6b0ea257` |
| 3 | .338 Lapua Magnum UCW | Ammo (pen 32) | 7.21 $ | 60 |  | Jaeger LL3 | `5fc382c1016cce60e8341b20` | `686e34246c2a18ed6b0e949c` |
| 3 | 6.8x51mm SIG FMJ | Ammo (pen 36) | 4.73 $ | 150 |  | Peacekeeper LL3 | `6529302b8c26af6326029fb7` | `686e34586c2a18ed6b0ea871` |
| 3 | 7.62x51mm BCP FMJ | Ammo (pen 37) | 2.08 $ | 100 |  | Jaeger LL3 | `5e023e53d4353e3302577c4c` | `686e342c6c2a18ed6b0e97b8` |
| 3 | ELCAN SpecterDR 1x/4x scope | Mod: AssaultScope | 295 $ | 4 |  | Peacekeeper LL3 | `57ac965c24597706be5f975c` | `686e344c6c2a18ed6b0ea368` |
| 3 | Leupold Mark 4 HAMR 4x24 DeltaPoint hybrid assault scope | Mod: AssaultScope | 384 $ | 4 |  | Peacekeeper LL3 | `544a3a774bdc2d3a388b4567` | `686e344a6c2a18ed6b0ea269` |
| 3 | Steyr AUG A3 M1 1.5x optic sight | Mod: AssaultScope | 80.49 $ | 5 |  | Peacekeeper LL3 | `62ebd290c427473eff0baafb` | `686e345a6c2a18ed6b0ea992` |
| 3 | Trijicon ACOG TA01NSN 4x32 scope (Black) | Mod: AssaultScope | 247 $ | 5 |  | Peacekeeper LL3 | `5c05293e0db83400232fff80` | `686e344f6c2a18ed6b0ea476` |
| 3 | Trijicon ACOG TA01NSN 4x32 scope (Tan) | Mod: AssaultScope | 240 $ | 4 |  | Peacekeeper LL3 | `5c052a900db834001a66acbd` | `686e34526c2a18ed6b0ea5d1` |
| 3 | EOTech 553 holographic sight | Mod: Collimator | 312 $ | 3 |  | Peacekeeper LL3 | `570fd6c2d2720bc6458b457f` | `686e344c6c2a18ed6b0ea340` |
| 3 | EOTech HHS-1 hybrid sight (Tan) | Mod: Collimator | 454 $ | 5 | A16 Griner! (suggested); vanilla: The Guide | Peacekeeper LL3 | `5c0a2cec0db834001b7ce47d` | `686e344e6c2a18ed6b0ea456` |
| 3 | FN P90 Ring Sight reflex sight | Mod: Collimator | 128 $ | 5 |  | Mechanic LL3 | `5cebec38d7f00c00110a652a` | `686e343d6c2a18ed6b0e9e1a` |
| 3 | AR-15 5.56x45 Magpul PMAG 30 GEN M3 STANAG 30-round magazine (FDE) | Mod: Magazine | 27.84 $ | 10 |  | Peacekeeper LL3 | `5d1340b3d7ad1a0b52682ed7` | `686e34526c2a18ed6b0ea5c5` |
| 3 | SIG Sauer SRD762Ti 7.62x51 sound suppressor | Mod: Silencer | 465 $ | 2 |  | Peacekeeper LL3 | `5fbe7618d6fa9c00c571bb6c` | `686e34546c2a18ed6b0ea6a8` |
| 3 | Graphics card | Other | 7× Car battery | 3 | A19 Oh, The Games People Play (suggested); vanilla: The Price of Independence | Mechanic LL3 | `57347ca924597744596b4e71` | `686e34466c2a18ed6b0ea0c8` |
| 3 | Intelligence folder | Other | 4× Diary + 4× Slim diary + 1× Topographic survey maps | 1 |  | Peacekeeper LL3 | `5c12613b86f7743bbe2c3f76` | `686e34526c2a18ed6b0ea59c` |
| 3 | Magazine case | Other | 2,136 $ | 1 | A18 Eyes On The Prize (suggested); vanilla: A Shooter Born in Heaven | Mechanic LL3 | `5c127c4486f7745625356c13` | `686e34346c2a18ed6b0e9a93` |
| 4 | Desert Tech MDR 7.62x51 assault rifle | Gun | 1,356 $ | 2 | A27 Hitscan - Part 2 (suggested); vanilla: Wet Job - Part 4 | Peacekeeper LL4 | `5dcbd56fdbd3d91b3e5468d5` | `686e34546c2a18ed6b0ea6aa` |
| 4 | FN SCAR-H 7.62x51 assault rifle | Gun | 1,266 $ | 1 |  | Peacekeeper LL4 | `6183afd850224f204c1da514` | `686e34576c2a18ed6b0ea838` |
| 4 | FN SCAR-H X-17 7.62x51 assault rifle | Gun | 243 $ | 3 |  | Mechanic LL4 | `676176d362e0497044079f4c` | `686e34466c2a18ed6b0ea0fb` |
| 4 | FN40GL Mk2 40mm grenade launcher | Gun | 1× VPX Flash Storage Module + 5× Military circuit board + 5× Military cable | 1 | A28 Meet Your Maker (suggested); vanilla: Wet Job - Part 6 | Peacekeeper LL4 | `5e81ebcd8e146c7080625e15` | `686e34546c2a18ed6b0ea694` |
| 4 | SIG MCX-SPEAR 6.8x51 assault rifle | Gun | 1,965 $ | 3 | A28 Meet Your Maker (proposed) | Peacekeeper (moved) | `65290f395ae2ae97b80fdf2d` | `686e345a6c2a18ed6b0ea981` |
| 4 | 5.56x45mm M856A1 | Ammo (pen 38) | 3.81 $ | 120 |  | Peacekeeper LL4 | `59e6906286f7746c9f75e847` | `686e34496c2a18ed6b0ea1de` |
| 4 | .300 Blackout CBJ | Ammo (pen 43) | 4.92 $ | 90 |  | Peacekeeper LL4 | `64b8725c4b75259c590fa899` | `686e34576c2a18ed6b0ea815` |
| 4 | 7.62x51mm M80 | Ammo (pen 43) | 3.93 $ | 100 | A24 Light Reading (suggested); vanilla: Revision - Lighthouse | Peacekeeper LL4 | `58dd3ad986f77403051cba8f` | `686e345d6c2a18ed6b0eaaf6` |
| 4 | 6.8x51mm SIG Hybrid | Ammo (pen 47) | 13.07 $ | 100 | A20 Frequent Flier (suggested); vanilla: Trouble in the Big City | Peacekeeper LL4 | `6529243824cbe3c74a05e5c1` | `686e345e6c2a18ed6b0eaaff` |
| 4 | 7.62x51mm M993 | Ammo (pen 65) | 20.00 $ | 20 | A25 Packet Loss (suggested); vanilla: The Punisher. Harvest | Peacekeeper LL4 | `5efb0c1bd79ff02a1f5e68d9` | `656629d07cac3c3b160e63fe` |
| 4 | TerraGroup Labs keycard (Black) | Key | 5× 6-STEN-140-M military battery + 8× Cyclon rechargeable battery + 2× UHF RFID Reader + 1× Secure magnetic tape cassette | 1 | A24 Light Reading (suggested); vanilla: Gunsmith - Part 25 | Mechanic LL4 | `5c1d0f4986f7744bb01837fa` | `686e343d6c2a18ed6b0e9e60` |
| 4 | ELCAN Specter HCO holographic sight | Mod: Collimator | 225 $ | 3 |  | Peacekeeper LL4 | `64785e7c19d732620e045e15` | `686e34556c2a18ed6b0ea746` |
| 4 | EOTech EXPS3-0 holographic sight (Tan) | Mod: Collimator | 304 $ | 4 |  | Mechanic LL4 | `558022b54bdc2dac148b458d` | `686e34336c2a18ed6b0e9a2d` |
| 4 | EOTech HHS-1 hybrid sight | Mod: Collimator | 389 $ | 5 |  | Peacekeeper LL4 | `5c07dd120db834001c39092d` | `686e344f6c2a18ed6b0ea46a` |
| 4 | Milkor M2A1 grenade launcher reflex sight | Mod: Collimator | 188 $ | 5 |  | Peacekeeper LL4 | `6284bd5f95250a29bc628a30` | `686e345b6c2a18ed6b0ea9ce` |
| 4 | Wilcox BOSS Xe reflex sight | Mod: Collimator | 507 $ | 4 |  | Peacekeeper LL4 | `655f13e0a246670fb0373245` | `686e345a6c2a18ed6b0ea99b` |
| 4 | AR-15 5.56x45 TROY BattleMag STANAG 30-round magazine | Mod: Magazine | 38.68 $ | 12 |  | Mechanic LL4 | `5c6d46132e221601da357d56` | `686e343c6c2a18ed6b0e9d9f` |
| 4 | AAC 762-SDN-6 multi-caliber sound suppressor | Mod: Silencer | 602 $ | 3 |  | Peacekeeper LL4 | `5a34fe59c4a282000b1521a2` | `686e344a6c2a18ed6b0ea288` |
| 4 | Advanced current converter | Other | 30× Electronic components + 10× Phased array element + 10× Virtex programmable processor + 10× VPX Flash Storage Module | 1 | A26 Hitscan - Part 1 (suggested); vanilla: Trouble in the Big City | Mechanic LL4 | `6389c85357baa773a825b356` | `686e34426c2a18ed6b0ea043` |
| 4 | Far-forward GPS Signal Amplifier Unit | Other | 5× Military gyrotachometer + 10× Military cable + 5× UHF RFID Reader + 8× Military COFDM Wireless Signal Transmitter | 1 | A29 God's Child, Herself (suggested); vanilla: Following the Bread Crumbs | Mechanic LL4 | `6389c7f115805221fb410466` | `686e34416c2a18ed6b0e9fd7` |
| 4 | Microcontroller board | Other | 3× Virtex programmable processor + 1× Graphics card + 5× Broken GPhone X smartphone + 5× VPX Flash Storage Module | 1 | A30 All Comes Tumbling Down (suggested); vanilla: Missing Informant | Mechanic LL4 | `6389c7750ef44505c87f5996` | `686e34426c2a18ed6b0e9ff8` |
| 4 | T H I C C Weapon case | Other | 10× Physical Bitcoin + 10× Gold skull ring | 1 | A20 Frequent Flier (suggested); vanilla: Chemistry Closet | Mechanic LL4 | `5b6d9ce188a4501afc1b2b25` | `686e34336c2a18ed6b0e9a52` |

## Price: Consumables, simple armour, hunting gear

RUB. Opens in Act I (Q8). Takes over Jaeger's shotguns, hunting ammo, mods and food, and Ragman's class 2–4 armour, rigs and backpacks.

| LL | Item | Type | Cost | Limit | Unlock | From | tpl | Offer |
|---|---|---|---|---|---|---|---|---|
| 1 | MP-133 12ga pump-action shotgun | Gun | 23,900 ₽ | 5 |  | Jaeger LL1 | `54491c4f4bdc2db1078b4568` | `686e34206c2a18ed6b0e92da` |
| 1 | MP-153 12ga semi-automatic shotgun | Gun | 1× Yotota car key + 1× Folding car key + 1× VAZ car key | 2 |  | Skier LL1 | `56dee2bdd2720bc8328b4567` | `686e34156c2a18ed6b0e8f1d` |
| 1 | MP-18 7.62x54R single-shot rifle | Gun | 16,100 ₽ | 2 |  | Jaeger LL1 | `61f7c9e189e6fb1a5e3ea78d` | `686e342a6c2a18ed6b0e96b1` |
| 1 | MP-43-1C 12ga double-barrel shotgun | Gun | 8,800 ₽ | 5 |  | Jaeger LL1 | `5580223e4bdc2d1c128b457f` | `686e34276c2a18ed6b0e95c7` |
| 1 | MTs-255-12 12ga shotgun | Gun | 21,300 ₽ | 5 |  | Jaeger LL1 | `60db29ce99594040e04c4a27` | `686e34286c2a18ed6b0e9632` |
| 1 | Mossberg 590A1 12ga pump-action shotgun | Gun | 32,600 ₽ | 10 |  | Peacekeeper LL1 | `5e870397991fd70db46995c8` | `686e34576c2a18ed6b0ea81d` |
| 1 | RSP-30 reactive signal cartridge (Green) | Gun | 6,000 ₽ | 2 |  | Jaeger LL1 | `6217726288ed9f0845317459` | `686e34296c2a18ed6b0e968e` |
| 1 | RSP-30 reactive signal cartridge (Yellow) | Gun | 2,346 ₽ | 5 |  | Prapor LL1 | `624c0b3340357b5f566e8766` | `686e346d6c2a18ed6b0eb237` |
| 1 | TOZ-106 20ga bolt-action shotgun | Gun | 8,900 ₽ | 5 |  | Skier LL1 | `5a38e6bac4a2826c6e06d79b` | `686e34116c2a18ed6b0e8da5` |
| 1 | 20x1mm disk | Ammo (pen 0) | 1 ₽ | 400 |  | Mechanic LL1 | `6601546f86889319850bd566` | `686e34446c2a18ed6b0ea04f` |
| 1 | 26x75mm flare cartridge (Acid Green) | Ammo (pen 0) | 10× Bottle of hydrogen peroxide + 5× Bottle of OLOLO Multivitamins + 1× Portable defibrillator | 1 | P1 Stocking Up (suggested); vanilla: A Key to Salvation | Therapist LL1 | `635267f063651329f75a4ee8` | `667eac90d135442276096594` |
| 1 | 26x75mm flare cartridge (Yellow) | Ammo (pen 0) | 3,376 ₽ | 5 |  | Jaeger LL1 | `62389be94d5d474bf712e709` | `686e34296c2a18ed6b0e969c` |
| 1 | 12/70 5.25mm buckshot | Ammo (pen 1) | 37 ₽ | 200 |  | Jaeger LL1 | `5d6e6772a4b936088465b17c` | `686e34236c2a18ed6b0e93fd` |
| 1 | 20/70 5.6mm buckshot | Ammo (pen 1) | 21 ₽ | 200 |  | Jaeger LL1 | `5d6e695fa4b936359b35d852` | `686e34226c2a18ed6b0e93b5` |
| 1 | 12/70 Grizzly 40 slug | Ammo (pen 12) | 70 ₽ | 200 |  | Jaeger LL1 | `5d6e6869a4b9361c140bcfde` | `686e34246c2a18ed6b0e9481` |
| 1 | .366 TKM Geksa | Ammo (pen 14) | 79 ₽ | 200 |  | Jaeger LL1 | `59e6658b86f77411d949b250` | `686e34216c2a18ed6b0e9317` |
| 1 | 20/70 Poleva-3 slug | Ammo (pen 14) | 51 ₽ | 200 |  | Jaeger LL1 | `5d6e6a53a4b9361bd473feec` | `686e34246c2a18ed6b0e9447` |
| 1 | 12/70 lead slug | Ammo (pen 15) | 65 ₽ | 200 |  | Skier LL1 | `58820d1224597753c90aeb13` | `686e34106c2a18ed6b0e8d01` |
| 1 | 12/70 Dual Sabot slug | Ammo (pen 17) | 72 ₽ | 200 |  | Jaeger LL1 | `5d6e68dea4b9361bcc29e659` | `686e34256c2a18ed6b0e94df` |
| 1 | 12/70 Poleva-3 slug | Ammo (pen 17) | 54 ₽ | 500 |  | Jaeger LL1 | `5d6e6891a4b9361bd473feea` | `686e34246c2a18ed6b0e9490` |
| 1 | 20/70 Poleva-6u slug | Ammo (pen 17) | 69 ₽ | 200 |  | Jaeger LL1 | `5d6e6a42a4b9364f07165f52` | `686e34246c2a18ed6b0e948c` |
| 1 | .366 TKM FMJ | Ammo (pen 23) | 84 ₽ | 1000 |  | Jaeger LL1 | `59e6542b86f77411dc52a77a` | `686e341f6c2a18ed6b0e9274` |
| 1 | 12/70 6.5mm Express buckshot | Ammo (pen 3) | 41 ₽ | 200 |  | Jaeger LL1 | `5d6e67fba4b9361bc73bc779` | `686e34246c2a18ed6b0e9455` |
| 1 | 12/70 7mm buckshot | Ammo (pen 3) | 35 ₽ | 400 |  | Skier LL1 | `560d5e524bdc2d25448b4571` | `686e340d6c2a18ed6b0e8c32` |
| 1 | 20/70 7.5mm buckshot | Ammo (pen 3) | 28 ₽ | 400 |  | Skier LL1 | `5a38ebd9c4a282000d722a5b` | `686e34126c2a18ed6b0e8e14` |
| 1 | 6B2 body armor (Flora) | Armour (class 2) | 19,600 ₽ | 5 |  | Prapor LL1 | `5df8a2ca86f7740bfe6df777` | `686e34686c2a18ed6b0eafaa` |
| 1 | BNTI Module-3M body armor | Armour (class 2) | 24,700 ₽ | 5 |  | Skier LL1 | `59e7635f86f7742cbf2c1095` | `686e34176c2a18ed6b0e8fbe` |
| 1 | 6B23-1 body armor (EMR) | Armour (class 3) | 1× Propane tank (5L) | 1 |  | Prapor LL1 | `5c0e5bab86f77461f55ed1f3` | `686e34696c2a18ed6b0eb010` |
| 1 | BNTI Zhuk body armor (Press) | Armour (class 3) | 1× Horse figurine + 1× Pompon hat | 1 |  | Skier LL1 | `5c0e5edb86f77461f55ed1f7` | `686e34156c2a18ed6b0e8f02` |
| 1 | MF-UNTAR body armor | Armour (class 3) | 2× Can of Max Energy energy drink | 1 |  | Ragman LL1 | `5ab8e4ed86f7742d8e50c7fa` | `686e34096c2a18ed6b0e89b5` |
| 1 | NPP KlASS Kora-Kulon body armor (Black) | Armour (class 3) | 1× Raven figurine | 1 |  | Ragman LL1 | `64be79c487d1510151095552` | `686e340b6c2a18ed6b0e8b59` |
| 1 | NPP KlASS Kora-Kulon body armor (EMR) | Armour (class 3) | 47,100 ₽ | 3 | P3 Fish and Croutons (suggested); vanilla: Search Mission | Prapor LL1 | `64be79e2bf8412471d0d9bcc` | `686e34696c2a18ed6b0eb036` |
| 1 | Flyye MBSS backpack (UCP) | Backpack | 19,000 ₽ |  | P11 Louis and Clarks (current) | current RTT2 stock | `544a5cde4bdc2d39388b456b` | `6b0260f9e297dd7d15b9ef7e` |
| 1 | LolKek 3F Transfer tourist backpack | Backpack | 59,000 ₽ |  | P11 Louis and Clarks (current) | current RTT2 stock | `5f5e45cc5021ce62144be7aa` | `6b0260f9e297dd7d15b9ef86` |
| 1 | Oakley Mechanism heavy duty backpack (Black) | Backpack | 56,000 ₽ |  | P11 Louis and Clarks (current) | current RTT2 stock | `5d5d940f86f7742797262046` | `6b0260f9e297dd7d15b9ef82` |
| 1 | Tactical sling bag (Khaki) | Backpack | 6,700 ₽ | 10 |  | Ragman LL1 | `5ab8f04f86f774585f4237d8` | `686e34086c2a18ed6b0e8908` |
| 1 | VKBO army bag | Backpack | 8,700 ₽ | 3 |  | Prapor LL1 | `5ab8ee7786f7742d8f33f0b9` | `686e34676c2a18ed6b0eaec0` |
| 1 | Army crackers | Food | 14,700 ₽ | 3 |  | Therapist LL1 | `5448ff904bdc2d6f028b456e` | `686e34716c2a18ed6b0eb478` |
| 1 | Bottle of water (0.6L) | Food | 12,400 ₽ | 5 |  | Therapist LL1 | `5448fee04bdc2dbc018b4567` | `686e34706c2a18ed6b0eb409` |
| 1 | Can of humpback salmon | Food | 2× Toothpaste | 3 |  | Therapist LL1 | `57347d5f245977448b40fa81` | `686e34726c2a18ed6b0eb4bd` |
| 1 | Can of pacific saury | Food | 1× Classic matches + 1× Crickent lighter | 5 |  | Therapist LL1 | `5673de654bdc2d180f8b456d` | `686e34706c2a18ed6b0eb40f` |
| 1 | Iskra ration pack | Food | 1× Disposable syringe | 2 |  | Therapist LL1 | `590c5d4b86f774784e1b9c45` | `686e34706c2a18ed6b0eb40c` |
| 1 | Slickers chocolate bar | Food | 1× Pack of Vita juice | 5 |  | Therapist LL1 | `544fb6cc4bdc2d34748b456e` | `686e34716c2a18ed6b0eb48a` |
| 1 | TSh-4M-L soft tank crew helmet | Headwear (class 1) | 6,700 ₽ | 5 |  | Ragman LL1 | `5df8a58286f77412631087ed` | `686e340c6c2a18ed6b0e8bc2` |
| 1 | Kolpak-1S riot helmet | Headwear (class 2) | 8,900 ₽ | 5 |  | Ragman LL1 | `59e7711e86f7746cae05fbe1` | `686e34076c2a18ed6b0e882c` |
| 1 | PSh-97 DJETA riot helmet | Headwear (class 2) | 11,800 ₽ | 5 |  | Skier LL1 | `5c0d2727d174af02a012cf58` | `686e34146c2a18ed6b0e8eb7` |
| 1 | FORT Kiver-M bulletproof helmet | Headwear (class 3) | 34,500 ₽ | 10 |  | Ragman LL1 | `5645bc214bdc2d363b8b4571` | `686e34066c2a18ed6b0e87fb` |
| 1 | SSSh-94 SFERA-S helmet | Headwear (class 3) | 34,900 ₽ | 2 | P4 Priced In (suggested); vanilla: Bad Rep Evidence | Prapor LL1 | `5aa7d193e5b5b000171d063f` | `686e34676c2a18ed6b0eaeff` |
| 1 | SSh-68 steel helmet (Olive Drab) | Headwear (class 3) | 29,100 ₽ | 10 |  | Ragman LL1 | `5c06c6a80db834001b735491` | `686e34096c2a18ed6b0e8962` |
| 1 | CALOK-B hemostatic applicator | Meds | 2× Pack of screws | 2 |  | Therapist LL1 | `5e8488fa988a8701445df1e4` | `686e34726c2a18ed6b0eb4a8` |
| 1 | CAT hemostatic tourniquet | Meds | 6,900 ₽ | 20 |  | Peacekeeper LL1 | `60098af40accd37ef2175f27` | `686e345d6c2a18ed6b0eaae3` |
| 1 | CMS surgical kit | Meds | 3× Nippers | 2 |  | Jaeger LL1 | `5d02778e86f774203e7dedbe` | `686e34246c2a18ed6b0e9489` |
| 1 | Car first aid kit | Meds | 11,800 ₽ | 10 | P2 Bad For You, Good For Me (suggested); vanilla: Sanitary Standards - Part 1 | Therapist LL1 | `590c661e86f7741e566b646a` | `686e34706c2a18ed6b0eb400` |
| 1 | Immobilizing splint | Meds | 4,283 ₽ | 20 |  | Therapist LL1 | `544fb3364bdc2d34748b456a` | `686e34706c2a18ed6b0eb3f1` |
| 1 | Salewa first aid kit | Meds | 1× Emergency Water Ration | 2 |  | Therapist LL1 | `544fb45d4bdc2dee738b4568` | `686e34716c2a18ed6b0eb472` |
| 1 | Axion Kobra EKP-8-18 reflex sight | Mod: Collimator | 14,700 ₽ | 5 |  | Jaeger LL1 | `591c4efa86f7741030027726` | `686e34216c2a18ed6b0e930c` |
| 1 | BelOMO PK-AA dovetail reflex sight | Mod: Collimator | 5,400 ₽ | 3 |  | Jaeger LL1 | `6113d6c3290d254f5e6b27db` | `686e34266c2a18ed6b0e953f` |
| 1 | KOMZ Rusak reflex sight | Mod: Collimator | 3,693 ₽ | 5 |  | Jaeger LL1 | `65f05b9d39dab9e9ec049cfd` | `686e342c6c2a18ed6b0e97b1` |
| 1 | VOMZ Pilad TargetRing reflex sight | Mod: Collimator | 9,200 ₽ | 4 |  | Jaeger LL1 | `609b9e31506cf869cf3eaf41` | `686e34266c2a18ed6b0e9557` |
| 1 | BelOMO PK-06 reflex sight | Mod: CompactCollimator | 8,400 ₽ | 3 |  | Jaeger LL1 | `57ae0171245977343c27bfcf` | `686e341f6c2a18ed6b0e923e` |
| 1 | MP-153 12ga 5-shell magazine | Mod: Magazine | 948 ₽ | 10 |  | Jaeger LL1 | `5882163e24597758206fee8c` | `686e34206c2a18ed6b0e92c3` |
| 1 | Leapers UTG 25mm ring scope mount | Mod: Mount | 1,733 ₽ | 5 |  | Jaeger LL1 | `5dff77c759400025ea5150cf` | `686e34246c2a18ed6b0e94a3` |
| 1 | VOMZ Pilad 4x32 25.4mm riflescope | Mod: OpticScope | 15,200 ₽ | 5 |  | Jaeger LL1 | `5dff772da3651922b360bf91` | `686e34246c2a18ed6b0e944b` |
| 1 | VPO-209 wooden stock | Mod: Stock | 1,911 ₽ | 3 |  | Jaeger LL1 | `59e89d0986f77427600d226e` | `686e34256c2a18ed6b0e94c1` |
| 1 | Armband (Blue) | Other | 637 ₽ | 1 |  | Ragman LL1 | `5b3f3af486f774679e752c1f` | `686e34086c2a18ed6b0e8911` |
| 1 | Armband (Green) | Other | 585 ₽ | 1 |  | Ragman LL1 | `5b3f3b0186f774021a2afef7` | `686e34076c2a18ed6b0e889e` |
| 1 | Armband (Red) | Other | 993 ₽ | 1 |  | Ragman LL1 | `5b3f3ade86f7746b6b790d8e` | `686e34076c2a18ed6b0e8873` |
| 1 | Armband (White) | Other | 810 ₽ | 1 |  | Ragman LL1 | `5b3f16c486f7747c327f55f7` | `686e34096c2a18ed6b0e89bc` |
| 1 | Armband (Yellow) | Other | 593 ₽ | 1 |  | Ragman LL1 | `5b3f3b0e86f7746752107cda` | `686e34096c2a18ed6b0e89ce` |
| 1 | EYE MK.2 professional hand-held compass | Other | 203,500 ₽ | 1 |  | Jaeger LL1 | `5f4f9eb969cdc30ff33f09db` | `686e34266c2a18ed6b0e952f` |
| 1 | Kolpak-1S face shield | Other | 5,400 ₽ | 3 |  | Ragman LL1 | `5ac4c50d5acfc40019262e87` | `686e34076c2a18ed6b0e8870` |
| 1 | Metal fuel tank | Other | 12× Classic matches + 5× Hunting matches | 1 |  | Jaeger LL1 | `5d1b36a186f7742523398433` | `686e34236c2a18ed6b0e93e5` |
| 1 | Soap | Other | 1× Awl | 1 |  | Ragman LL1 | `5c13cd2486f774072c757944` | `686e340c6c2a18ed6b0e8b71` |
| 1 | Tripwire installation kit | Other | 24,600 ₽ | 4 | P5 Priced Out (suggested); vanilla: Every Hunter Knows This | Jaeger LL1 | `666b11055a706400b717cfa5` | `686e342a6c2a18ed6b0e9715` |
| 1 | Vortex Ranger 1500 rangefinder | Other | 9,400 ₽ | 10 |  | Jaeger LL1 | `61605e13ffa6e502ac5e7eef` | `686e34276c2a18ed6b0e9586` |
| 1 | Zhuk-3 ballistic plate (Front) | Plate (class 3) | 1× Pack of Grand juice | 3 |  | Prapor LL1 | `656f57dc27aed95beb08f628` | `686e346b6c2a18ed6b0eb143` |
| 1 | 6B5-15 Zh-86 Uley armored rig (Flora) | Rig | 59,000 ₽ |  | P10 Vlone Vever (current) | current RTT2 stock | `5c0e446786f7742013381639` | `6b0260f843837a263b96e860` |
| 1 | CSA chest rig (Black) | Rig | 11,400 ₽ | 3 |  | Ragman LL1 | `6034d0230ca681766b6a0fb5` | `686e340b6c2a18ed6b0e8b34` |
| 1 | Direct Action Thunderbolt compact chest rig (Shadow Grey) | Rig | 26,000 ₽ |  | P10 Vlone Vever (current) | current RTT2 stock | `5f5f41f56760b4138443b352` | `6b0260f843837a263b96e842` |
| 1 | Scav Vest | Rig | 1× Slickers chocolate bar | 10 |  | Jaeger LL1 | `572b7adb24597762ae139821` | `686e341f6c2a18ed6b0e9267` |
| 1 | Shellback Tactical Banshee plate carrier (A-TACS AU) | Rig | 72,000 ₽ |  | P10 Vlone Vever (current) | current RTT2 stock | `639343fce101f4caa40a4ef3` | `6b0260f843837a263b96e84c` |
| 1 | Spiritus Systems Bank Robber chest rig (MultiCam Alpine) | Rig | 8,600 ₽ | 3 |  | Ragman LL1 | `674589d98dd67746010329e6` | `686e340c6c2a18ed6b0e8bec` |
| 1 | Spiritus Systems Bank Robber chest rig (MultiCam Black) | Rig | 8,200 ₽ | 3 |  | Ragman LL1 | `5e4abc1f86f774069619fbaa` | `686e340c6c2a18ed6b0e8ba4` |
| 1 | Type 56 Chicom chest harness | Rig | 12,400 ₽ | 5 |  | Ragman LL1 | `64be7110bf597ba84a0a41ea` | `686e340b6c2a18ed6b0e8b67` |
| 1 | UMTBS 6Sh112 Scout-Sniper chest rig (EMR) | Rig | 1× Pack of milk + 1× Pack of oat flakes | 2 |  | Prapor LL1 | `5929a2a086f7744f4b234d43` | `686e346a6c2a18ed6b0eb093` |
| 1 | Umka M33-SET1 hunter vest (Olive Drab) | Rig | 27,000 ₽ | 3 |  | Jaeger LL1 | `6034cf5fffd42c541047f72e` | `686e34286c2a18ed6b0e9613` |
| 1 | WARTECH TV-109 + TV-106 chest rig (A-TACS FG) | Rig | 15,800 ₽ | 4 |  | Ragman LL1 | `59e7643b86f7742cbf2c109a` | `686e34066c2a18ed6b0e8801` |
| 1 | Zulu Nylon Gear M4 Reduced Signature Chest Rig (Ranger Green) | Rig | 9,000 ₽ | 4 |  | Ragman LL1 | `64be7095047e826eae02b0c1` | `686e340c6c2a18ed6b0e8bdc` |
| 2 | MP-155 12ga semi-automatic shotgun | Gun | 34,900 ₽ | 5 |  | Jaeger LL2 | `606dae0ab0e443224b421bb7` | `686e34276c2a18ed6b0e95ab` |
| 2 | MP-43 12ga sawed-off double-barrel shotgun | Gun | 10,200 ₽ | 1 |  | Jaeger LL2 | `64748cb8de82c85eaf0a273a` | `686e342b6c2a18ed6b0e976d` |
| 2 | Molot Arms VPO-101 Vepr-Hunter 7.62x51 carbine | Gun | 48,300 ₽ | 3 |  | Jaeger LL2 | `5c501a4d2e221602b412b540` | `686e34246c2a18ed6b0e945c` |
| 2 | RSP-30 reactive signal cartridge (Blue) | Gun | 1× Pipe grip wrench + 1× Inseq gas pipe wrench | 3 | P10 Vlone Vever (suggested); vanilla: The Price of Independence | Mechanic LL2 | `66d98233302686954b0c6f81` | `686e34466c2a18ed6b0ea0cb` |
| 2 | 26x75mm flare cartridge (Green) | Ammo (pen 0) | 1× Aquapeps water purification tablets | 1 |  | Jaeger LL2 | `62389aaba63f32501b1b444f` | `686e34296c2a18ed6b0e9692` |
| 2 | 23x75mm Shrapnel-10 buckshot | Ammo (pen 11) | 120 ₽ | 25 |  | Prapor LL2 | `5e85a9a6eacf8c039e4e2ac1` | `686e34676c2a18ed6b0eaef9` |
| 2 | 12/70 Copper Sabot Premier HP slug | Ammo (pen 14) | 87 ₽ | 150 |  | Jaeger LL2 | `5d6e68b3a4b9361bca7e50b5` | `686e34246c2a18ed6b0e9443` |
| 2 | 20/70 6.2mm buckshot | Ammo (pen 2) | 32 ₽ | 200 |  | Jaeger LL2 | `5d6e69b9a4b9361bc8618958` | `686e34246c2a18ed6b0e9479` |
| 2 | 12/70 FTX Custom Lite slug | Ammo (pen 20) | 75 ₽ | 200 |  | Jaeger LL2 | `5d6e68e6a4b9361c140bcfe0` | `686e34256c2a18ed6b0e94ad` |
| 2 | 12/70 Poleva-6u slug | Ammo (pen 20) | 72 ₽ | 500 |  | Jaeger LL2 | `5d6e689ca4b9361bc8618956` | `686e34236c2a18ed6b0e93e8` |
| 2 | 12/70 Piranha | Ammo (pen 24) | 231 ₽ | 70 |  | Jaeger LL2 | `64b8ee384b75259c590fa89b` | `686e34266c2a18ed6b0e9553` |
| 2 | 20/70 7.3mm buckshot | Ammo (pen 3) | 40 ₽ | 200 |  | Jaeger LL2 | `5d6e69c7a4b9360b6c0d54e4` | `686e34246c2a18ed6b0e9459` |
| 2 | .366 TKM EKO | Ammo (pen 30) | 116 ₽ | 1000 |  | Jaeger LL2 | `59e655cb86f77411dc52a77b` | `686e341f6c2a18ed6b0e9282` |
| 2 | 12/70 SuperFormance HP slug | Ammo (pen 5) | 202 ₽ | 60 |  | Jaeger LL2 | `5d6e68d1a4b93622fe60e845` | `686e34236c2a18ed6b0e9431` |
| 2 | BNTI Kirasa-N body armor | Armour (class 3) | 50,900 ₽ | 3 |  | Ragman LL2 | `5b44d22286f774172b0c9de8` | `686e34096c2a18ed6b0e8976` |
| 2 | 6B13 assault armor (Flora) | Armour (class 4) | 64,300 ₽ | 2 | P16 Courtesy Call - Part 4 (proposed) | Ragman (moved) | `5c0e51be86f774598e797894` | `686e34076c2a18ed6b0e8893` |
| 2 | Interceptor OTV body armor (UCP) | Armour (class 4) | 1× Golden rooster figurine | 2 | P6 New Money (suggested); vanilla: Minibus | Ragman LL2 | `64abd93857958b4249003418` | `686e340b6c2a18ed6b0e8af0` |
| 2 | NFM THOR Concealable Reinforced Vest body armor | Armour (class 4) | 2× Slim diary | 2 | P9 Table for Two (suggested); vanilla: Database - Part 1 | Ragman LL2 | `609e8540d5c319764c2bc2e9` | `686e340a6c2a18ed6b0e8a6c` |
| 2 | Hazard 4 Pillbox backpack (Black) | Backpack | 1× Horse figurine | 1 |  | Ragman LL2 | `60a2828e8689911a226117f9` | `686e340a6c2a18ed6b0e8a44` |
| 2 | Hazard 4 Takedown sling backpack (MultiCam) | Backpack | 30,100 ₽ | 5 | P10 Vlone Vever (suggested); vanilla: The Blood of War - Part 1 | Ragman LL2 | `6038d614d10cbf667352dd44` | `686e340b6c2a18ed6b0e8afc` |
| 2 | LBT-1476A 3Day Pack (MultiCam Alpine) | Backpack | 1× Cordura polyamide fabric | 2 |  | Ragman LL2 | `67458794e21e5d724e066976` | `686e340c6c2a18ed6b0e8bef` |
| 2 | LBT-8005A Day Pack backpack (MultiCam Black) | Backpack | 24,500 ₽ | 2 |  | Peacekeeper LL2 | `5e9dcf5986f7746c417435b3` | `686e34526c2a18ed6b0ea5da` |
| 2 | Tehinkom RK-PT-25 patrol backpack (EMR) | Backpack | 30,400 ₽ | 3 |  | Ragman LL2 | `656ddcf0f02d7bcea90bf395` | `686e340c6c2a18ed6b0e8b77` |
| 2 | WARTECH Berkut BB-102 backpack (A-TACS FG) | Backpack | 24,500 ₽ | 8 |  | Ragman LL2 | `5ca20d5986f774331e7c9602` | `686e34086c2a18ed6b0e88df` |
| 2 | Emelya rye croutons | Food | 16,500 ₽ | 4 |  | Therapist LL2 | `5751487e245977207e26a315` | `686e34706c2a18ed6b0eb41e` |
| 2 | Pack of sugar | Food | 5× Emelya rye croutons | 1 |  | Jaeger LL2 | `59e3577886f774176a362503` | `686e34276c2a18ed6b0e958d` |
| 2 | Rye croutons | Food | 1× Emelya rye croutons | 3 |  | Therapist LL2 | `57347d3d245977448f7b7f61` | `686e34726c2a18ed6b0eb4a2` |
| 2 | 6B47 Ratnik-BSh helmet (EMR Arctic cover) | Headwear (class 3) | 2× Ox bleach | 2 |  | Ragman LL2 | `6745895717824b1ec20570a6` | `686e340c6c2a18ed6b0e8c09` |
| 2 | 6B47 Ratnik-BSh helmet (Olive Drab) | Headwear (class 3) | 39,100 ₽ | 8 |  | Prapor LL2 | `5a7c4850e899ef00150be885` | `686e34636c2a18ed6b0ead12` |
| 2 | DevTac Ronin ballistic helmet | Headwear (class 3) | 77,800 ₽ | 2 | P8 Check Please (suggested); vanilla: Corporate Secrets | Mechanic LL2 | `66bdc28a0b603c26902b2011` | `686e34476c2a18ed6b0ea154` |
| 2 | Galvion Caiman Hybrid helmet (Grey) | Headwear (class 3) | 55,500 ₽ | 1 | P9 Table for Two (suggested); vanilla: Revision - Streets of Tarkov | Peacekeeper LL2 | `5f60b34a41e30a4ab12a6947` | `686e34576c2a18ed6b0ea834` |
| 2 | LShZ lightweight helmet (Olive Drab) | Headwear (class 3) | 35,700 ₽ | 4 |  | Ragman LL2 | `5b432d215acfc4771e1c6624` | `686e34096c2a18ed6b0e8990` |
| 2 | MSA ACH TC-2001 MICH Series helmet (Olive Drab) | Headwear (class 4) | 56,400 ₽ | 5 | P7 In Another Life (suggested); vanilla: Wet Job - Part 2 | Peacekeeper LL2 | `5d5e7d28a4b936645d161203` | `686e34506c2a18ed6b0ea50e` |
| 2 | MSA Gallet TC 800 High Cut combat helmet (Black) | Headwear (class 4) | 1× Topographic survey maps + 1× Damaged hard drive | 3 |  | Peacekeeper LL2 | `5e4bfc1586f774264f7582d3` | `686e34586c2a18ed6b0ea8cf` |
| 2 | ZSh-1-2M helmet (Olive Drab) | Headwear (class 4) | 54,300 ₽ | 4 |  | Ragman LL2 | `5aa7e454e5b5b0214e506fa2` | `686e34076c2a18ed6b0e8849` |
| 2 | Military checkpoint key | Key | 2× Tech manual + 4× Bottle of Tarkovskaya vodka + 2× Can of beef stew (Small) | 1 |  | Jaeger LL2 | `5913915886f774123603c392` | `686e34266c2a18ed6b0e952c` |
| 2 | Monstrum Tactical Compact Prism Scope 2x32 | Mod: AssaultScope | 38,800 ₽ | 2 |  | Jaeger LL2 | `5d2dc3e548f035404a1a4798` | `686e34236c2a18ed6b0e93ec` |
| 2 | MP-153 12ga 7-shell magazine | Mod: Magazine | 1,747 ₽ | 10 |  | Jaeger LL2 | `5882163224597757561aa920` | `686e34206c2a18ed6b0e92a7` |
| 2 | Nightforce Magmount 34mm ring scope mount with Ruggedized Accessory Platform | Mod: Mount | 6,600 ₽ | 5 |  | Jaeger LL2 | `5aa66c72e5b5b00016327c93` | `686e34226c2a18ed6b0e9372` |
| 2 | Nightforce ATACR 7-35x56 34mm riflescope | Mod: OpticScope | 1× Portable Powerbank + 2× Magnet + 1× Ultraviolet lamp | 1 |  | Jaeger LL2 | `5aa66be6e5b5b0214e506e97` | `686e34226c2a18ed6b0e9397` |
| 2 | Mosin Rifle AIM Sports Recoil Pad | Mod: Stock | 4,084 ₽ | 5 | P8 Check Please (suggested); vanilla: The Tarkov Shooter - Part 3 | Jaeger LL2 | `5bbde409d4351e003562b036` | `686e34226c2a18ed6b0e938e` |
| 2 | Kiver-M face shield | Other | 27,800 ₽ | 4 |  | Ragman LL2 | `5b46238386f7741a693bcf9c` | `686e34096c2a18ed6b0e89e4` |
| 2 | Mr. Holodilnick thermal bag | Other | 10× Can of Hot Rod energy drink + 5× Can of TarCola soda + 5× Can of herring + 5× Can of squash spread | 1 |  | Jaeger LL2 | `5c093db286f7740a1b2617e3` | `686e34216c2a18ed6b0e935e` |
| 2 | Ops-Core FAST Visor | Other | 14,900 ₽ | 3 |  | Ragman LL2 | `5a16b672fcdbcb001912fa83` | `686e34086c2a18ed6b0e8917` |
| 2 | ZSh-1-2M face shield | Other | 2× Piece of plexiglass | 3 |  | Ragman LL2 | `5aa7e3abe5b5b000171d064d` | `686e34086c2a18ed6b0e8937` |
| 2 | 6B12 ballistic plates (Front) | Plate (class 3) | 13,500 ₽ | 5 |  | Prapor LL2 | `654a4dea7c17dec2f50cc86a` | `686e346d6c2a18ed6b0eb1f0` |
| 2 | AR500 Legacy Plate ballistic plate | Plate (class 3) | 14,500 ₽ | 2 |  | Skier LL2 | `656f9d5900d62bcd2e02407c` | `686e341a6c2a18ed6b0e90bd` |
| 2 | 6B23-2 ballistic plate (Back) | Plate (class 4) | 12,200 ₽ | 5 |  | Prapor LL2 | `657b22485f444d6dff0c6c2f` | `686e346b6c2a18ed6b0eb10b` |
| 2 | ANA Tactical Alpha chest rig (Olive Drab) | Rig | 5× Duct tape + 1× Alkaline cleaner for heat exchangers | 1 |  | Ragman LL2 | `592c2d1a86f7746dbe2af32a` | `686e34086c2a18ed6b0e890e` |
| 2 | Azimut SS Zhuk chest harness (Black) | Rig | 33,500 ₽ | 8 |  | Ragman LL2 | `603648ff5a45383c122086ac` | `686e340b6c2a18ed6b0e8abe` |
| 2 | BlackHawk! Commando chest harness (Desert Tan) | Rig | 31,800 ₽ | 5 |  | Ragman LL2 | `5b44c8ea86f7742d1627baf1` | `686e34076c2a18ed6b0e887c` |
| 2 | Dynaforce Triton M43-A chest harness (Black) | Rig | 26,400 ₽ | 3 |  | Ragman LL2 | `5ca20abf86f77418567a43f2` | `686e340a6c2a18ed6b0e8a32` |
| 2 | Gear Craft GC-BSS-MK1 chest rig (A-TACS FG) | Rig | 26,700 ₽ | 8 |  | Ragman LL2 | `5fd4c60f875c30179f5d04c2` | `686e340b6c2a18ed6b0e8b13` |
| 2 | Haley Strategic D3CRX Chest Harness (Ranger Green) | Rig | 35,100 ₽ | 8 |  | Ragman LL2 | `5d5d85c586f774279a21cbdb` | `686e340a6c2a18ed6b0e8a1d` |
| 2 | SOE Micro Rig (MultiCam) | Rig | 10,400 ₽ | 5 |  | Peacekeeper LL2 | `5d5d8ca986f7742798716522` | `686e34526c2a18ed6b0ea586` |
| 2 | Splav Tarzan M22 chest rig (Smog) | Rig | 1× Hunting matches | 2 |  | Jaeger LL2 | `5e4abfed86f77406a2713cf7` | `686e34286c2a18ed6b0e9608` |
| 2 | Stich Profi Chest Rig MK2 (Recon, A-TACS FG) | Rig | 36,000 ₽ | 6 |  | Ragman LL2 | `60a6220e953894617404b00a` | `686e340b6c2a18ed6b0e8aff` |
| 2 | 6B5-16 Zh-86 Uley armored rig (Khaki) | Rig (class 3) | 55,600 ₽ | 1 | P7 In Another Life (suggested); vanilla: Shootout Picnic | Prapor LL2 | `5c0e3eb886f7742015526062` | `686e34656c2a18ed6b0eae04` |
| 2 | 6B3TM-01 armored rig (Khaki) | Rig (class 4) | 2× 6B3TM-01 armored rig (Khaki) | 2 | P6 New Money (suggested); vanilla: Database - Part 2 | Ragman LL2 | `5d5d646386f7742797261fd9` | `686e340a6c2a18ed6b0e8a4b` |
| 3 | ZiD SP-81 26x75 signal pistol | Gun | 3× Makarov PM (t) 9x18PM pistol + 2× TT-33 7.62x25 TT pistol + 1× Gunpowder "Eagle" | 1 |  | Jaeger LL3 | `620109578d82e67e7911abf2` | `686e342b6c2a18ed6b0e9724` |
| 3 | 23x75mm Zvezda flashbang round | Ammo (pen 0) | 2,618 ₽ | 10 | P12 King of Burgers (suggested); vanilla: Our Own Land | Prapor LL3 | `5e85a9f4add9fe03027d9bf1` | `6877c7788a126f9efb0cc09d` |
| 3 | 23x75mm Shrapnel-25 buckshot | Ammo (pen 10) | 138 ₽ | 40 |  | Prapor LL3 | `5f647f31b6238e5dd066e196` | `686e346a6c2a18ed6b0eb081` |
| 3 | 20/70 Star slug | Ammo (pen 16) | 86 ₽ | 200 |  | Jaeger LL3 | `5d6e6a05a4b93618084f58d0` | `686e34246c2a18ed6b0e947d` |
| 3 | 12/70 8.5mm Magnum buckshot | Ammo (pen 2) | 200 ₽ | 80 |  | Jaeger LL3 | `5d6e6806a4b936088465b17e` | `686e34236c2a18ed6b0e93f9` |
| 3 | 12/70 makeshift .50 BMG slug | Ammo (pen 26) | 420 ₽ | 50 |  | Jaeger LL3 | `5d6e68c4a4b9361b93413f79` | `686e34226c2a18ed6b0e93a1` |
| 3 | 12/70 flechette | Ammo (pen 31) | 439 ₽ | 70 |  | Jaeger LL3 | `5d6e6911a4b9361bd5780d52` | `686e342a6c2a18ed6b0e96ca` |
| 3 | 23x75mm Barrikada slug | Ammo (pen 39) | 280 ₽ | 20 |  | Prapor LL3 | `5e85aa1a988a8701445df1f5` | `686e34686c2a18ed6b0eaf92` |
| 3 | 20/70 Devastator slug | Ammo (pen 5) | 189 ₽ | 120 |  | Jaeger LL3 | `5d6e6a5fa4b93614ec501745` | `686e34236c2a18ed6b0e93e1` |
| 3 | BNTI Gzhel-K body armor | Armour (class 3) | 1× Golden neck chain + 2× Can of Majaica coffee beans | 3 |  | Ragman LL3 | `5ab8e79e86f7742d8b372e78` | `686e340c6c2a18ed6b0e8bc7` |
| 3 | ANA Tactical Beta 2 Battle backpack (Olive Drab) | Backpack | 76,000 ₽ | 2 |  | Ragman LL3 | `5b44c6ae86f7742d1627baea` | `686e34076c2a18ed6b0e885b` |
| 3 | Camelbak Tri-Zip assault backpack (Foliage) | Backpack | 57,900 ₽ | 3 | P14 Courtesy Call - Part 2 (suggested); vanilla: Inventory Check | Ragman LL3 | `545cdae64bdc2d39198b4568` | `686e34066c2a18ed6b0e8819` |
| 3 | Camelbak Tri-Zip assault backpack (MultiCam) | Backpack | 61,300 ₽ | 3 | P15 Courtesy Call - Part 3 (suggested); vanilla: Inventory Check | Ragman LL3 | `66b5f22b78bbc0200425f904` | `686e340c6c2a18ed6b0e8bd9` |
| 3 | Direct Action Dragon Egg Mark II backpack (Black) | Backpack | 33,800 ₽ | 3 |  | Ragman LL3 | `656f198fb27298d6fd005466` | `686e340b6c2a18ed6b0e8b44` |
| 3 | Gruppa 99 T20 backpack (MultiCam) | Backpack | 32,600 ₽ | 5 |  | Ragman LL3 | `619cf0335771dd3c390269ae` | `686e340b6c2a18ed6b0e8abb` |
| 3 | Gruppa 99 T20 backpack (Umber Brown) | Backpack | 32,600 ₽ | 5 |  | Ragman LL3 | `618bb76513f5097c8d5aa2d5` | `686e34096c2a18ed6b0e89ed` |
| 3 | Gruppa 99 T30 backpack (MultiCam) | Backpack | 10× Dogtag USEC | 2 |  | Ragman LL3 | `62a1b7fbc30cfa1d366af586` | `686e340a6c2a18ed6b0e8a55` |
| 3 | Hazard 4 Takedown sling backpack (Black) | Backpack | 30,100 ₽ | 4 |  | Ragman LL3 | `6034d103ca006d2dca39b3f0` | `686e34096c2a18ed6b0e89e7` |
| 3 | LBT-2670 Slim Field Med Pack (Black) | Backpack | 2× Augmentin antibiotic pills + 2× Vaseline balm + 2× Surv12 field surgical kit + 3× Pile of meds | 1 |  | Therapist LL3 | `5e4abc6786f77406812bd572` | `686e34716c2a18ed6b0eb490` |
| 3 | NPP KlASS Tor-2 helmet (Olive Drab) | Headwear (class 3) | 58,500 ₽ | 4 |  | Ragman LL3 | `65719f0775149d62ce0a670b` | `686e340b6c2a18ed6b0e8b61` |
| 3 | Diamond Age Bastion helmet (Black) | Headwear (class 4) | 66,100 ₽ | 2 |  | Ragman LL3 | `5ea17ca01412a1425304d1c0` | `686e340b6c2a18ed6b0e8b39` |
| 3 | Diamond Age NeoSteel High Cut helmet (Black) | Headwear (class 4) | 90,300 ₽ | 4 |  | Ragman LL3 | `65709d2d21b9f815e208ff95` | `686e340b6c2a18ed6b0e8b6c` |
| 3 | HighCom Striker ACHHC IIIA helmet (Black) | Headwear (class 4) | 57,900 ₽ | 2 |  | Ragman LL3 | `5b40e3f35acfc40016388218` | `686e34096c2a18ed6b0e89df` |
| 3 | HighCom Striker ACHHC IIIA helmet (Olive Drab) | Headwear (class 4) | 58,900 ₽ | 3 |  | Ragman LL3 | `5b40e4035acfc47a87740943` | `686e34096c2a18ed6b0e896a` |
| 3 | Maska-1SCh bulletproof helmet (Olive Drab) | Headwear (class 4) | 67,700 ₽ | 2 |  | Prapor LL3 | `5c091a4e0db834001d5addc8` | `686e34666c2a18ed6b0eae79` |
| 3 | ZSh-1-2M helmet (Black cover) | Headwear (class 4) | 49,500 ₽ | 1 |  | Ragman LL3 | `5aa7e4a4e5b5b000137b76f2` | `686e34066c2a18ed6b0e880a` |
| 3 | Dorm room 314 marked key | Key | 1× RB-VO marked key + 1× RB-PKPM marked key + 1× RB-BK marked key | 1 |  | Jaeger LL3 | `5780cf7f2459777de4559322` | `686e34276c2a18ed6b0e958a` |
| 3 | Goshan cash register key | Key | 6× Toilet paper + 5× Repellent + 2× SurvL Survivor Lighter + 2× Pack of chlorine | 1 |  | Jaeger LL3 | `5ad7247386f7747487619dc3` | `686e34266c2a18ed6b0e9550` |
| 3 | OLI logistics department office key | Key | 4× Hunting matches + 2× SurvL Survivor Lighter + 1× Dry fuel | 1 |  | Jaeger LL3 | `5ad5cfbd86f7742c825d6104` | `686e34276c2a18ed6b0e9593` |
| 3 | MP-153 12ga 8-shell magazine | Mod: Magazine | 2,229 ₽ | 4 |  | Jaeger LL3 | `56deeefcd2720bc8328b4568` | `686e34216c2a18ed6b0e931b` |
| 3 | M700 30mm integral ring scope mount | Mod: Mount | 3,570 ₽ | 3 |  | Jaeger LL3 | `5bfebc5e0db834001a6694e5` | `686e34216c2a18ed6b0e9343` |
| 3 | Schmidt & Bender PM II 5-25x56 34mm riflescope | Mod: OpticScope | 99,800 ₽ | 1 |  | Jaeger LL3 | `62850c28da09541f43158cca` | `686e34296c2a18ed6b0e9653` |
| 3 | Wilcox RAPTAR ES Tactical Rangefinder | Mod: TacticalCombo | 23,100 ₽ | 2 |  | Jaeger LL3 | `61605d88ffa6e502ac5e7eeb` | `686e34266c2a18ed6b0e954c` |
| 3 | Galvion Caiman Fixed Arm Visor | Other | 24,300 ₽ | 4 |  | Peacekeeper LL3 | `5f60bf4558eff926626a60f2` | `686e34576c2a18ed6b0ea7ed` |
| 3 | Galvion Caiman Hybrid Ballistic Mandible Guard | Other | 26,500 ₽ | 4 |  | Peacekeeper LL3 | `5f60c076f2bcbb675b00dac2` | `686e34576c2a18ed6b0ea849` |
| 3 | Grenade case | Other | 5× SurvL Survivor Lighter + 15× Hunting matches + 8× Repellent | 1 |  | Jaeger LL3 | `5e2af55f86f7746d4159f07c` | `686e34276c2a18ed6b0e9599` |
| 3 | LShZ-2DTM face shield | Other | 3× Piece of plexiglass | 3 |  | Ragman LL3 | `5d6d3829a4b9361bc8618943` | `686e340a6c2a18ed6b0e8a0a` |
| 3 | NPP KlASS Tor-2 helmet face shield | Other | 35,600 ₽ | 4 |  | Ragman LL3 | `65719f9ef392ad76c50a2ec8` | `686e340b6c2a18ed6b0e8b3e` |
| 3 | Ops-Core FAST Gunsight Mandible | Other | 23,100 ₽ | 3 |  | Peacekeeper LL3 | `5a16ba61fcdbcb098008728a` | `686e344b6c2a18ed6b0ea2f4` |
| 3 | Ops-Core FAST Side Armor | Other | 31,700 ₽ | 3 |  | Peacekeeper LL3 | `5a16badafcdbcb001865f72d` | `686e344c6c2a18ed6b0ea365` |
| 3 | 6B33 ballistic plate (Front) | Plate (class 4) | 16,600 ₽ | 5 |  | Prapor LL3 | `656f603f94b480b8a500c0d6` | `686e346c6c2a18ed6b0eb1b3` |
| 3 | Global Armor’s Steel ballistic plate | Plate (class 4) | 18,500 ₽ | 4 |  | Skier LL3 | `656fa0fb498d1b7e3e071d9c` | `686e34186c2a18ed6b0e9049` |
| 3 | Kiba Arms Titan ballistic plate | Plate (class 4) | 2× Strike Cigarettes | 2 | P11 Louis and Clarks (suggested); vanilla: Bullshit | Skier LL3 | `656fa25e94b480b8a500c0e0` | `686e341b6c2a18ed6b0e9110` |
| 3 | Monoclete level III PE ballistic plate | Plate (class 4) | 1× Press pass (issued for NoiceGuy) | 2 |  | Peacekeeper LL3 | `656fad8c498d1b7e3e071da0` | `686e345b6c2a18ed6b0ea9e6` |
| 3 | NewSphereTech level III ballistic plate | Plate (class 4) | 21,000 ₽ | 4 |  | Peacekeeper LL3 | `656fb21fa0dce000a2020f7c` | `686e345a6c2a18ed6b0ea9c5` |
| 3 | SPRTN Elaphros ballistic plate | Plate (class 4) | 22,000 ₽ | 4 |  | Peacekeeper LL3 | `656fb0bd7c2d57afe200c0dc` | `686e345a6c2a18ed6b0ea99e` |
| 3 | SPRTN Omega ballistic plate | Plate (class 4) | 21,000 ₽ | 4 |  | Skier LL3 | `656f9fa0498d1b7e3e071d98` | `686e34186c2a18ed6b0e901a` |
| 3 | BlackRock chest rig (Gray) | Rig | 45,200 ₽ | 6 |  | Ragman LL3 | `5648a69d4bdc2ded0b8b457b` | `686e34076c2a18ed6b0e8832` |
| 3 | Poyas-A + Poyas-B gear rig | Rig | 1× Antique teapot | 3 |  | Ragman LL3 | `5c0e6a1586f77404597b4965` | `686e34086c2a18ed6b0e893a` |
| 3 | Stich Profi Chest Rig MK2 (Assault, A-TACS FG) | Rig | 37,500 ₽ | 3 |  | Ragman LL3 | `60a621c49c197e4e8c4455e6` | `686e340a6c2a18ed6b0e8a58` |
| 3 | Velocity Systems MPPV Multi-Purpose Patrol Vest (Wolf Grey) | Rig | 3× Can of condensed milk | 3 |  | Ragman LL3 | `5df8a42886f77412640e2e75` | `686e340a6c2a18ed6b0e8a07` |
| 3 | WARTECH MK3 TV-104 chest rig (MultiCam) | Rig | 41,000 ₽ | 3 |  | Ragman LL3 | `5ab8dab586f77441cd04f2a2` | `686e34086c2a18ed6b0e892b` |
| 3 | ANA Tactical M1 plate carrier (Olive Drab) | Rig (class 4) | 2× Bottle of Norvinsky Yadreniy premium kvass (0.6L) + 1× Aquamari water bottle with filter | 3 |  | Ragman LL3 | `5c0e722886f7740458316a57` | `686e34096c2a18ed6b0e8956` |
| 3 | CQC Osprey MK4A plate carrier (Assault, MTP) | Rig (class 4) | 92,000 ₽ | 2 | P13 Courtesy Call - Part 1 (suggested); vanilla: Audiophile | Ragman LL3 | `60a3c70cde5f453f634816a3` | `686e340b6c2a18ed6b0e8ade` |
| 3 | ECLiPSE RBAV-AF plate carrier (Ranger Green) | Rig (class 4) | 86,000 ₽ | 2 |  | Ragman LL3 | `628dc750b910320f4c27a732` | `686e340b6c2a18ed6b0e8b09` |
| 3 | Eagle Industries MMAC plate carrier (Ranger Green) | Rig (class 4) | 73,900 ₽ | 3 |  | Peacekeeper LL3 | `61bc85697113f767765c7fe7` | `686e34546c2a18ed6b0ea685` |
| 3 | First Spear Strandhogg plate carrier (Ranger Green) | Rig (class 4) | 1× Sewing kit + 2× Cordura polyamide fabric + 1× Bottle of Tarkovskaya vodka | 2 |  | Ragman LL3 | `61bcc89aef0f505f0c6cd0fc` | `686e340b6c2a18ed6b0e8acb` |
| 3 | Stich Profi Plate Carrier V2 (Black) | Rig (class 4) | 2× Viibiin sneaker | 3 |  | Ragman LL3 | `66b6296d7994640992013b17` | `686e340c6c2a18ed6b0e8bb5` |
| 4 | 12/70 RIP | Ammo (pen 2) | 735 ₽ | 50 |  | Jaeger LL4 | `5c0d591486f7744c505b416f` | `686e34256c2a18ed6b0e9516` |
| 4 | 6B43 Zabralo-Sh body armor (EMR) | Armour (class 3) | 4× Topographic survey maps + 2× Phase control relay | 3 |  | Prapor LL4 | `545cdb794bdc2d3a198b456a` | `686e346e6c2a18ed6b0eb2ae` |
| 4 | HighCom Trooper TFO body armor (MultiCam) | Armour (class 4) | 3× Axel parrot figurine | 2 | P20 Superman (suggested); vanilla: The Blood of War - Part 3 | Ragman LL4 | `5c0e655586f774045612eeb2` | `686e340a6c2a18ed6b0e8a5f` |
| 4 | 3V Gear Paratus 3-Day Operator's Tactical backpack (Foliage Grey) | Backpack | 63,700 ₽ | 3 |  | Peacekeeper LL4 | `5c0e805e86f774683f3dd637` | `686e344f6c2a18ed6b0ea466` |
| 4 | 6Sh118 raid backpack (EMR) | Backpack | 1× Cyclon rechargeable battery + 2× Military gyrotachometer | 1 | P16 Courtesy Call - Part 4 (suggested); vanilla: Sew it Good - Part 3 | Prapor LL4 | `5df8a4d786f77412672a1e3b` | `686e34676c2a18ed6b0eaf1e` |
| 4 | Eberlestock F4 Terminator load bearing backpack (Tiger Stripe) | Backpack | 90,400 ₽ | 3 |  | Ragman LL4 | `5f5e46b96bdad616ad46d613` | `686e340a6c2a18ed6b0e8a2f` |
| 4 | Eberlestock G2 Gunslinger II backpack (Dry Earth) | Backpack | 60,900 ₽ | 3 |  | Ragman LL4 | `6034d2d697633951dc245ea6` | `686e340b6c2a18ed6b0e8ac1` |
| 4 | Mystery Ranch Blackjack 50 backpack (MultiCam) | Backpack | 1× VPX Flash Storage Module | 1 | P17 Last Call (suggested); vanilla: Hot Delivery | Ragman LL4 | `5c0e774286f77468413cc5b2` | `686e34086c2a18ed6b0e88a1` |
| 4 | Mystery Ranch SATL Bridger Assault Pack (Foliage) | Backpack | 100,000 ₽ | 2 |  | Ragman LL4 | `656e0436d44a1bb4220303a0` | `686e340c6c2a18ed6b0e8b74` |
| 4 | SSO Attack 2 raid backpack (Khaki) | Backpack | 1× Chain with Prokill medallion | 1 |  | Ragman LL4 | `5ab8ebf186f7742d8b372e80` | `686e34076c2a18ed6b0e8838` |
| 4 | Tasmanian Tiger Trooper 35 backpack (Khaki) | Backpack | 2× Can of condensed milk + 1× Pack of milk | 2 |  | Ragman LL4 | `639346cc1c8f182ad90c8972` | `686e340a6c2a18ed6b0e8a8e` |
| 4 | BNTI LShZ-2DTM helmet (Black) | Headwear (class 4) | 86,800 ₽ | 1 |  | Ragman LL4 | `5d6d3716a4b9361bc8618872` | `686e340a6c2a18ed6b0e8a26` |
| 4 | Crye Precision AirFrame helmet (Tan) | Headwear (class 4) | 94,600 ₽ | 2 | P17 Last Call (suggested); vanilla: Spa Tour - Part 7 | Peacekeeper LL4 | `5c17a7ed2e2216152142459c` | `686e34516c2a18ed6b0ea524` |
| 4 | DevTac Ronin Respirator | Headwear (class 4) | 111,800 ₽ | 1 | P18 The Pie? It's Far Too Hot (suggested); vanilla: Payback | Ragman LL4 | `5b4329f05acfc47a86086aa1` | `686e340c6c2a18ed6b0e8be4` |
| 4 | HighCom Striker ULACH IIIA helmet (Desert Tan) | Headwear (class 4) | 97,000 ₽ | 4 | P19 The Good Stuff (suggested); vanilla: Sales Night | Ragman LL4 | `5b40e2bc5acfc40016388216` | `686e34096c2a18ed6b0e89c5` |
| 4 | MTEK FLUX Ballistic helmet (MultiCam Alpine) | Headwear (class 4) | 119,300 ₽ | 3 |  | Ragman LL4 | `675956062f6ddfe8ff0e2806` | `686e340c6c2a18ed6b0e8b9f` |
| 4 | MTEK STRIKE Ballistic helmet (Coyote) | Headwear (class 4) | 113,600 ₽ | 3 |  | Ragman LL4 | `67597ceea35600b4c10cea86` | `686e340c6c2a18ed6b0e8bfe` |
| 4 | MTEK STRIKE Ballistic helmet (Coyote/MultiCam Arid) | Headwear (class 4) | 114,600 ₽ | 3 |  | Ragman LL4 | `67597d241d5a44f2f605df06` | `686e340c6c2a18ed6b0e8ba9` |
| 4 | Ops-Core FAST MT Super High Cut helmet (Black) | Headwear (class 4) | 1× Military COFDM Wireless Signal Transmitter + 1× Military gyrotachometer | 2 |  | Peacekeeper LL4 | `5a154d5cfcdbcb001a3b00da` | `686e345e6c2a18ed6b0eab26` |
| 4 | Ops-Core FAST MT Super High Cut helmet (Urban Tan) | Headwear (class 4) | 102,900 ₽ | 2 | P18 The Pie? It's Far Too Hot (suggested); vanilla: Cargo X - Part 4 | Peacekeeper LL4 | `5ac8d6885acfc400180ae7b0` | `686e34496c2a18ed6b0ea1d6` |
| 4 | Team Wendy EXFIL Ballistic Helmet (Black) | Headwear (class 4) | 122,500 ₽ | 2 | P20 Superman (suggested); vanilla: Samples | Peacekeeper LL4 | `5e00c1ad86f774747333222c` | `686e34516c2a18ed6b0ea568` |
| 4 | Team Wendy EXFIL Ballistic Helmet (Coyote Brown) | Headwear (class 4) | 109,700 ₽ | 2 |  | Peacekeeper LL4 | `5e01ef6886f77445f643baa4` | `686e34506c2a18ed6b0ea507` |
| 4 | RB-PP key | Key | 4× Can of RatCola soda + 8× Pompon hat + 4× Ushanka ear flap hat | 1 |  | Jaeger LL4 | `5d80cb8786f774405611c7d9` | `686e34296c2a18ed6b0e96a9` |
| 4 | RB-PSP2 key | Key | 7× Cyclon rechargeable battery + 5× Flat screwdriver (Long) | 1 |  | Jaeger LL4 | `5d95d6fa86f77424484aa5e9` | `686e34266c2a18ed6b0e9546` |
| 4 | AI AXMC padded handguard grip | Mod: Foregrip | 3,019 ₽ | 3 |  | Jaeger LL4 | `6281212a09427b40ab14e770` | `686e34296c2a18ed6b0e9677` |
| 4 | Mosin Rifle 7.62x54R ProMag Archangel OPFOR 10-round magazine | Mod: Magazine | 6,400 ₽ | 5 | P16 Courtesy Call - Part 4 (suggested); vanilla: The Tarkov Shooter - Part 8 | Jaeger LL4 | `5bae13ded4351e44f824bf38` | `686e34226c2a18ed6b0e936b` |
| 4 | Leupold Mark IMS 35mm ring scope mount | Mod: Mount | 8,000 ₽ | 5 |  | Jaeger LL4 | `6761759e7ee06333f108bf86` | `686e342c6c2a18ed6b0e97bf` |
| 4 | Leupold Mark 5HD 5-25x56mm 35mm riflescope (FDE) | Mod: OpticScope | 2× Jar of pickles | 5 |  | Jaeger LL4 | `676175789dcee773150c6925` | `686e342c6c2a18ed6b0e978b` |
| 4 | March Tactical 3-24x42 FFP 30mm riflescope | Mod: OpticScope | 43,700 ₽ | 1 |  | Jaeger LL4 | `57c5ac0824597754771e88a9` | `686e34206c2a18ed6b0e92c7` |
| 4 | NcSTAR ADO P4 Sniper 3-9x42 riflescope | Mod: OpticScope | 53,900 ₽ | 2 |  | Jaeger LL4 | `5dfe6104585a0c3e995c7b82` | `686e34256c2a18ed6b0e94d9` |
| 4 | Schmidt & Bender PM II 3-20x50 34mm riflescope | Mod: OpticScope | 68,200 ₽ | 1 |  | Jaeger LL4 | `61714eec290d254f5e6b2ffc` | `686e34266c2a18ed6b0e9577` |
| 4 | Crye Precision AirFrame Chops | Other | 64,600 ₽ | 3 |  | Peacekeeper LL4 | `5c178a942e22164bef5ceca3` | `686e344f6c2a18ed6b0ea4a9` |
| 4 | Crye Precision AirFrame Ears | Other | 44,300 ₽ | 5 |  | Peacekeeper LL4 | `5c1793902e221602b21d3de2` | `686e34516c2a18ed6b0ea51c` |
| 4 | Galvion Caiman Hybrid Ballistic Applique | Other | 71,800 ₽ | 3 |  | Peacekeeper LL4 | `5f60b85bbdb8e27dee3dc985` | `686e34556c2a18ed6b0ea71e` |
| 4 | Ops-Core FAST multi-hit ballistic face shield | Other | 43,200 ₽ | 4 | P19 The Good Stuff (suggested); vanilla: Samples | Peacekeeper LL4 | `5a16b7e1fcdbcb00165aa6c9` | `686e34496c2a18ed6b0ea1db` |
| 4 | S I C C organizational pouch | Other | 12× Paracord + 15× Duct tape + 15× Insulating tape + 15× Pack of nails | 1 |  | Jaeger LL4 | `5d235bb686f77443f4331278` | `686e34256c2a18ed6b0e94b1` |
| 4 | Team Wendy EXFIL Ballistic face shield (Black) | Other | 52,800 ₽ | 2 |  | Peacekeeper LL4 | `5e00cdd986f7747473332240` | `686e34536c2a18ed6b0ea631` |
| 4 | Team Wendy EXFIL Ballistic face shield (Coyote Brown) | Other | 52,800 ₽ | 2 |  | Peacekeeper LL4 | `5e01f37686f774773c6f6c15` | `686e34516c2a18ed6b0ea55d` |
| 4 | Team Wendy EXFIL Ear Covers (Black) | Other | 53,000 ₽ | 2 |  | Peacekeeper LL4 | `5e00cfa786f77469dc6e5685` | `686e34516c2a18ed6b0ea54d` |
| 4 | Team Wendy EXFIL Ear Covers (Coyote Brown) | Other | 53,000 ₽ | 2 |  | Peacekeeper LL4 | `5e01f31d86f77465cf261343` | `686e34536c2a18ed6b0ea5ed` |
| 4 | Vulkan-5 helmet face shield | Other | 5× Piece of plexiglass + 1× Bottle of Pevko Light beer | 1 |  | Ragman LL4 | `5ca2113f86f7740b2547e1d2` | `686e34096c2a18ed6b0e89d4` |
| 4 | LBT-1961A Load Bearing Chest Rig (MAS Grey) | Rig | 1× Axel parrot figurine + 2× Can of white salt | 2 |  | Ragman LL4 | `5e9db13186f7742f845ee9d3` | `686e340b6c2a18ed6b0e8b41` |
| 4 | ANA Tactical M2 plate carrier (EMR) | Rig (class 4) | 10× Dogtag USEC | 3 |  | Ragman LL4 | `5ab8dced86f774646209ec87` | `686e34086c2a18ed6b0e88ad` |
| 4 | Crye Precision AVS plate carrier (Ranger Green) | Rig (class 4) | 105,600 ₽ | 3 |  | Ragman LL4 | `544a5caa4bdc2d1a388b4568` | `686e34076c2a18ed6b0e8821` |
| 4 | WARTECH TV-110 plate carrier (Coyote) | Rig (class 4) | 90,100 ₽ | 2 |  | Ragman LL4 | `5c0e746986f7741453628fe5` | `686e34086c2a18ed6b0e891e` |

## Needle: Stims, painkillers, pistol and SMG ammo, cheap guns

RUB. Opens in Act I (Q13). Takes over Therapist's stims and drugs, and every pistol and SMG caliber.

| LL | Item | Type | Cost | Limit | Unlock | From | tpl | Offer |
|---|---|---|---|---|---|---|---|---|
| 1 | Beretta M9A3 9x19 pistol | Gun | 13,700 ₽ | 5 |  | Peacekeeper LL1 | `5cadc190ae921500103bb3b6` | `686e34506c2a18ed6b0ea4eb` |
| 1 | HK MP5 9x19 submachine gun (Navy 3 Round Burst) | Gun | 33,700 ₽ | 5 |  | Peacekeeper LL1 | `5926bb2186f7744b1c6c6e60` | `686e344a6c2a18ed6b0ea2a2` |
| 1 | Makarov PM (t) 9x18PM pistol | Gun | 5,500 ₽ | 5 |  | Mechanic LL1 | `579204f224597773d619e051` | `686e34426c2a18ed6b0ea00b` |
| 1 | PB 9x18PM silenced pistol | Gun | 21,500 ₽ | 5 |  | Prapor LL1 | `56e0598dd2720bb5668b45a6` | `686e34616c2a18ed6b0eabfb` |
| 1 | PP-19-01 Vityaz 9x19 submachine gun | Gun | 21,500 ₽ | 5 |  | Prapor LL1 | `59984ab886f7743e98271174` | `686e34646c2a18ed6b0ead51` |
| 1 | PP-9 Klin 9x18PMM submachine gun | Gun | 23,400 ₽ | 5 | N4 Poor Mans Propitol (suggested); vanilla: BP Depot | Prapor LL1 | `57f4c844245977379d5c14d1` | `686e34626c2a18ed6b0eac5f` |
| 1 | PPSh-41 7.62x25 submachine gun | Gun | 26,600 ₽ | 5 |  | Prapor LL1 | `5ea03f7400685063ec28bfa8` | `686e34696c2a18ed6b0eafe9` |
| 1 | Stechkin APS 9x18PM machine pistol | Gun | 1× Bolts | 3 |  | Prapor LL1 | `5a17f98cfcdbcb0980087290` | `686e34666c2a18ed6b0eae48` |
| 1 | TT-33 7.62x25 TT pistol | Gun | 8,200 ₽ | 3 |  | Prapor LL1 | `571a12c42459771f627b58a0` | `686e34626c2a18ed6b0eac63` |
| 1 | Yarygin MP-443 Grach 9x19 pistol | Gun | 13,800 ₽ | 3 |  | Prapor LL1 | `576a581d2459771e7b1bc4f1` | `686e34646c2a18ed6b0ead4d` |
| 1 | 9x19mm PSO gzh | Ammo (pen 10) | 54 ₽ | 1000 |  | Prapor LL1 | `58864a4f2459770fcc257101` | `686e34636c2a18ed6b0ead00` |
| 1 | 7.62x25mm TT FMJ43 | Ammo (pen 11) | 55 ₽ | 1000 |  | Prapor LL1 | `5735ff5c245977640e39ba7e` | `686e34636c2a18ed6b0ead1f` |
| 1 | .357 Magnum SP | Ammo (pen 12) | 105 ₽ | 120 |  | Jaeger LL1 | `62330c40bdd19b369e1e53d1` | `686e34276c2a18ed6b0e9582` |
| 1 | 7.62x25mm TT AKBS | Ammo (pen 12) | 54 ₽ | 1000 |  | Prapor LL1 | `5735fdcd2459776445391d61` | `686e34626c2a18ed6b0eac59` |
| 1 | 9x18mm PM Pst gzh | Ammo (pen 12) | 50 ₽ | 1000 |  | Prapor LL1 | `5737201124597760fc4431f1` | `686e34606c2a18ed6b0eabea` |
| 1 | 9x18mm PM RG028 gzh | Ammo (pen 13) | 94 ₽ | 400 |  | Prapor LL1 | `573720e02459776143012541` | `686e34616c2a18ed6b0eabf0` |
| 1 | 9x19mm Green Tracer | Ammo (pen 14) | 65 ₽ | 500 |  | Mechanic LL1 | `5c3df7d588a4501f290594e5` | `686e343b6c2a18ed6b0e9d0b` |
| 1 | 9x21mm PE gzh | Ammo (pen 15) | 77 ₽ | 1000 |  | Prapor LL1 | `5a26ac06c4a282000c5a90a8` | `686e34636c2a18ed6b0eacf1` |
| 1 | 5.7x28mm SS198LF | Ammo (pen 17) | 87 ₽ | 300 |  | Peacekeeper LL1 | `5cc80f79e4a949033c7343b2` | `686e344f6c2a18ed6b0ea4ac` |
| 1 | .357 Magnum HP | Ammo (pen 18) | 129 ₽ | 120 |  | Jaeger LL1 | `62330bfadc5883093563729b` | `686e34266c2a18ed6b0e9563` |
| 1 | 4.6x30mm Action SX | Ammo (pen 18) | 70 ₽ | 400 |  | Mechanic LL1 | `5ba26812d4351e003201fef1` | `686e34356c2a18ed6b0e9b01` |
| 1 | .45 ACP Lasermatch FMJ | Ammo (pen 19) | 82 ₽ | 1000 |  | Peacekeeper LL1 | `5efb0d4f4bc50b58e81710f3` | `686e34526c2a18ed6b0ea5e4` |
| 1 | .50 AE Hawk JSP | Ammo (pen 26) | 185 ₽ | 150 |  | Jaeger LL1 | `66a0d1f88486c69fce00fdf6` | `686e341f6c2a18ed6b0e924d` |
| 1 | 9x19mm PBP gzh | Ammo (pen 39) | 700 ₽ | 150 | N3 I Can't Aim (suggested); vanilla: Hint | Skier LL1 | `5efb0da7a29a85116f6ea05f` | `6492e44bf4287b13040fccf6` |
| 1 | 9x18mm PM P gzh | Ammo (pen 5) | 14 ₽ | 1000 |  | Prapor LL1 | `573719762459775a626ccbc1` | `686e34646c2a18ed6b0ead8d` |
| 1 | 9x18mm PM PSO gzh | Ammo (pen 5) | 24 ₽ | 1000 |  | Prapor LL1 | `57371f8d24597761006c6a81` | `686e34646c2a18ed6b0ead48` |
| 1 | 9x18mm PM PRS gs | Ammo (pen 6) | 43 ₽ | 300 |  | Prapor LL1 | `57371eb62459776125652ac1` | `686e34646c2a18ed6b0ead62` |
| 1 | 9x18mm PM PS gs PPO | Ammo (pen 6) | 32 ₽ | 1000 |  | Prapor LL1 | `57371f2b24597761224311f1` | `686e34616c2a18ed6b0eac44` |
| 1 | 7.62x25mm TT LRNPC | Ammo (pen 7) | 72 ₽ | 1000 |  | Jaeger LL1 | `573602322459776445391df1` | `686e34206c2a18ed6b0e92a0` |
| 1 | 9x18mm PM PPe gzh | Ammo (pen 7) | 56 ₽ | 1000 |  | Prapor LL1 | `57371b192459775a9f58a5e0` | `686e34626c2a18ed6b0eac8c` |
| 1 | 7.62x25mm TT LRN | Ammo (pen 8) | 51 ₽ | 1000 |  | Jaeger LL1 | `573601b42459776410737435` | `686e341f6c2a18ed6b0e926d` |
| 1 | 9x18mm PM PPT gzh | Ammo (pen 8) | 47 ₽ | 1000 |  | Prapor LL1 | `57371e4124597760ff7b25f1` | `686e34646c2a18ed6b0ead5f` |
| 1 | Analgin painkillers | Meds | 8,500 ₽ | 10 |  | Therapist LL1 | `544fb37f4bdc2dee738b4567` | `686e34706c2a18ed6b0eb3fa` |
| 2 | IWI UZI PRO Pistol 9x19 submachine gun | Gun | 33,900 ₽ | 5 |  | Peacekeeper LL2 | `6680304edadb7aa61d00cef0` | `686e345c6c2a18ed6b0eaa44` |
| 2 | Magnum Research Desert Eagle L5 .357 pistol | Gun | 1× Pressure gauge | 5 |  | Jaeger LL2 | `669fa409933e898cce0c2166` | `686e34286c2a18ed6b0e961e` |
| 2 | Serdyukov SR-1MP Gyurza 9x21 pistol | Gun | 1× Gunpowder "Kite" | 2 |  | Prapor LL2 | `59f98b4986f7746f546d2cef` | `686e34666c2a18ed6b0eae9a` |
| 2 | 9x18mm PM SP8 gzh | Ammo (pen 1) | 76 ₽ | 400 |  | Prapor LL2 | `5737218f245977612125ba51` | `686e34616c2a18ed6b0eac26` |
| 2 | 5.7x28mm R37.X | Ammo (pen 11) | 220 ₽ | 150 |  | Mechanic LL2 | `5cc86840d7f00c002412c56c` | `686e34326c2a18ed6b0e9a24` |
| 2 | .50 AE JHP | Ammo (pen 12) | 224 ₽ | 150 |  | Jaeger LL2 | `66a0d1c87d0d369e270bb9de` | `686e342c6c2a18ed6b0e9784` |
| 2 | 7.62x25mm TT P gl | Ammo (pen 14) | 57 ₽ | 1000 |  | Prapor LL2 | `5736026a245977644601dc61` | `686e34636c2a18ed6b0eacf4` |
| 2 | 7.62x25mm TT PT gzh | Ammo (pen 18) | 69 ₽ | 1000 |  | Prapor LL2 | `573603c924597764442bd9cb` | `686e34626c2a18ed6b0eac77` |
| 2 | 9x18mm PM BZhT gzh | Ammo (pen 18) | 71 ₽ | 1000 |  | Prapor LL2 | `573718ba2459775a75491131` | `686e34646c2a18ed6b0ead38` |
| 2 | 9x19mm FMJ M882 | Ammo (pen 18) | 129 ₽ | 1000 |  | Peacekeeper LL2 | `64b7bbb74b75259c590fa897` | `686e34576c2a18ed6b0ea82c` |
| 2 | 9x21mm P gzh | Ammo (pen 18) | 153 ₽ | 1000 |  | Prapor LL2 | `5a26abfac4a28232980eabff` | `686e34636c2a18ed6b0eacf7` |
| 2 | 9x18mm PM SP7 gzh | Ammo (pen 2) | 183 ₽ | 450 | N8 Marathon Dose - Part 2 (suggested); vanilla: You've Got Mail | Prapor LL2 | `57372140245977611f70ee91` | `686e34626c2a18ed6b0eac92` |
| 2 | 9x19mm Pst gzh | Ammo (pen 20) | 71 ₽ | 600 |  | Prapor LL2 | `56d59d3ad2720bdb418b4577` | `686e34616c2a18ed6b0eac35` |
| 2 | 9x21mm PS gzh | Ammo (pen 22) | 264 ₽ | 220 | N9 Marathon Dose - Part 3 (suggested); vanilla: The Bunker - Part 1 | Prapor LL2 | `5a269f97c4a282000b151807` | `686e34616c2a18ed6b0eac3b` |
| 2 | 4.6x30mm Subsonic SX | Ammo (pen 23) | 100 ₽ | 1000 |  | Mechanic LL2 | `5ba26844d4351e00334c9475` | `686e34336c2a18ed6b0e9a3c` |
| 2 | .357 Magnum JHP | Ammo (pen 24) | 196 ₽ | 80 |  | Jaeger LL2 | `62330c18744e5e31df12f516` | `686e34286c2a18ed6b0e960f` |
| 2 | 9x18mm PMM PstM gzh | Ammo (pen 24) | 126 ₽ | 450 |  | Prapor LL2 | `57371aab2459775a77142f22` | `686e34636c2a18ed6b0eacfd` |
| 2 | .45 ACP Match FMJ | Ammo (pen 25) | 102 ₽ | 1000 |  | Peacekeeper LL2 | `5e81f423763d9f754677bf2e` | `686e34536c2a18ed6b0ea655` |
| 2 | 5.7x28mm SS197SR | Ammo (pen 25) | 162 ₽ | 300 | N7 Marathon Dose - Part 1 (suggested); vanilla: Scrap Metal | Peacekeeper LL2 | `5cc80f8fe4a949033b0224a2` | `686e344e6c2a18ed6b0ea3f7` |
| 2 | 7.62x25mm TT Pst gzh | Ammo (pen 25) | 77 ₽ | 1000 |  | Prapor LL2 | `573603562459776430731618` | `686e34616c2a18ed6b0eabf6` |
| 2 | 9x18mm PM PBM gzh | Ammo (pen 28) | 132 ₽ | 350 |  | Prapor LL2 | `573719df2459775a626ccbc2` | `686e34646c2a18ed6b0ead42` |
| 2 | 9x18mm PM PSV | Ammo (pen 3) | 77 ₽ | 400 |  | Jaeger LL2 | `5737207f24597760ff7b25f2` | `686e34206c2a18ed6b0e92bf` |
| 2 | .50 AE Copper Solid | Ammo (pen 33) | 435 ₽ | 150 |  | Mechanic LL2 | `66a0d1e0ed648d72fe064d06` | `686e34476c2a18ed6b0ea18d` |
| 2 | .357 Magnum FMJ | Ammo (pen 35) | 150 ₽ | 80 |  | Jaeger LL2 | `62330b3ed4dc74626d570b95` | `686e34286c2a18ed6b0e960b` |
| 2 | Adrenaline injector | Meds | 1× Classic matches + 1× Ultraviolet lamp | 1 |  | Therapist LL2 | `5c10c8fd86f7743d7d706df3` | `686e34716c2a18ed6b0eb463` |
| 2 | Propital regenerative stimulant injector | Meds | 5× Pack of apple juice | 2 | N10 Inject Me Scotty (suggested); vanilla: Ambulances Again | Therapist LL2 | `5c0e530286f7747fa1419862` | `686e34726c2a18ed6b0eb4c9` |
| 2 | Injector case | Other | 20× Medical tools + 15× Disposable syringe + 12× Bottle of hydrogen peroxide | 1 | N13 Much Needed Shipment (proposed) | Therapist (moved) | `619cbf7d23893217ec30b689` | `686e34726c2a18ed6b0eb4a5` |
| 3 | Magnum Research Desert Eagle L5 .50 AE pistol | Gun | 1× Fuel conditioner | 1 |  | Jaeger LL3 | `669fa3f88abd2662d80eee77` | `686e342c6c2a18ed6b0e97d8` |
| 3 | RSh-12 12.7x55 revolver | Gun | 1× Military cable + 5× AA Battery | 2 |  | Prapor LL3 | `633ec7c2a6918cb895019c6c` | `686e346c6c2a18ed6b0eb151` |
| 3 | 9x19mm Luger CCI | Ammo (pen 10) | 170 ₽ | 180 |  | Mechanic LL3 | `5a3c16fe86f77452b62de32a` | `686e342f6c2a18ed6b0e98a0` |
| 3 | .45 ACP Hydra-Shok | Ammo (pen 13) | 162 ₽ | 180 |  | Peacekeeper LL3 | `5efb0fc6aeb21837e749c801` | `686e34526c2a18ed6b0ea5c2` |
| 3 | 5.7x28mm SB193 | Ammo (pen 27) | 292 ₽ | 200 |  | Peacekeeper LL3 | `5cc80f67e4a949035e43bbba` | `686e344f6c2a18ed6b0ea48b` |
| 3 | 9x21mm 7U4 | Ammo (pen 27) | 298 ₽ | 150 |  | Prapor LL3 | `6576f93989f0062e741ba952` | `686e346b6c2a18ed6b0eb112` |
| 3 | 9x19mm AP 6.3 | Ammo (pen 30) | 227 ₽ | 210 |  | Peacekeeper LL3 | `5c925fa22e221601da359b7b` | `686e344e6c2a18ed6b0ea3f1` |
| 3 | 4.6x30mm JSP SX | Ammo (pen 32) | 280 ₽ | 180 |  | Mechanic LL3 | `64b6979341772715af0f9c39` | `686e34416c2a18ed6b0e9f78` |
| 3 | 9x21mm BT gzh | Ammo (pen 32) | 609 ₽ | 180 | N12 Poppin a Proppie (suggested); vanilla: Test Drive - Part 2 | Prapor LL3 | `5a26ac0ec4a28200741e1e18` | `686e346e6c2a18ed6b0eb26b` |
| 3 | 5.7x28mm L191 | Ammo (pen 33) | 335 ₽ | 300 |  | Peacekeeper LL3 | `5cc80f53e4a949000e1ea4f8` | `686e344f6c2a18ed6b0ea482` |
| 3 | .50 AE FMJ | Ammo (pen 40) | 824 ₽ | 100 |  | Mechanic LL3 | `668fe62ac62660a5d8071446` | `686e342d6c2a18ed6b0e9831` |
| 3 | 5.7x28mm R37.F | Ammo (pen 8) | 335 ₽ | 150 | N11 It's Wrapping Time (suggested); vanilla: Gunsmith - Part 9 | Mechanic LL3 | `5cc86832d7f00c000d3a6e6c` | `686e34346c2a18ed6b0e9a81` |
| 3 | SJ1 TGLabs combat stimulant injector | Meds | 1× Disposable syringe + 1× Bottle of hydrogen peroxide + 1× Pack of sodium bicarbonate | 1 |  | Therapist LL3 | `5c0e531286f7747fa54205c2` | `686e34716c2a18ed6b0eb47b` |
| 3 | eTG-change regenerative stimulant injector | Meds | 4× Schaman shampoo | 1 |  | Therapist LL3 | `5c0e534186f7747fa1419867` | `686e34716c2a18ed6b0eb46c` |
| 4 | 9x19mm RIP | Ammo (pen 2) | 422 ₽ | 120 |  | Mechanic LL4 | `5c0d56a986f774449d5de529` | `686e34456c2a18ed6b0ea079` |
| 4 | .45 ACP RIP | Ammo (pen 3) | 420 ₽ | 90 | N15 Soundcloud Soliloquy (suggested); vanilla: Broadcast - Part 4 | Mechanic LL4 | `5ea2a8e200685063ec28c05a` | `686e343d6c2a18ed6b0e9e2c` |
| 4 | 5.7x28mm SS190 | Ammo (pen 37) | 497 ₽ | 150 |  | Peacekeeper LL4 | `5cc80f38e4a949001152b560` | `686e344f6c2a18ed6b0ea49d` |
| 4 | .45 ACP AP | Ammo (pen 38) | 725 ₽ | 100 |  | Peacekeeper LL4 | `5efb0cabfb3e451d70735af5` | `686e34536c2a18ed6b0ea622` |
| 4 | 9x21mm 7N42 Zubilo | Ammo (pen 38) | 859 ₽ | 120 |  | Prapor LL4 | `6576f4708ca9c4381d16cd9d` | `686e346b6c2a18ed6b0eb134` |
| 4 | 4.6x30mm FMJ SX | Ammo (pen 40) | 425 ₽ | 120 | N17 The Gig is Up (suggested); vanilla: Import | Mechanic LL4 | `5ba2678ad4351e44f824b344` | `686e34316c2a18ed6b0e99a5` |
| 4 | 4.6x30mm AP SX | Ammo (pen 53) | 1,331 ₽ | 60 | N16 This Cranker is Crazy (suggested); vanilla: The Punisher. Harvest | Peacekeeper LL4 | `5ba26835d4351e0035628ff5` | `656629d07cac3c3b160e6400` |
| 4 | 9x19mm QuakeMaker | Ammo (pen 8) | 324 ₽ | 180 |  | Peacekeeper LL4 | `5efb0e16aeb21837e749c7ff` | `686e34526c2a18ed6b0ea5d4` |
| 4 | Augmentin antibiotic pills | Meds | 45,100 ₽ | 2 |  | Therapist LL4 | `590c695186f7741e566b64a2` | `686e34706c2a18ed6b0eb3fd` |
| 4 | Ibuprofen painkillers | Meds | 1× Medical bloodset + 3× Pile of meds | 1 |  | Therapist LL4 | `5af0548586f7743a532b7e99` | `686e34716c2a18ed6b0eb469` |
| 4 | Morphine injector | Meds | 42,100 ₽ | 4 | N15 Soundcloud Soliloquy (suggested); vanilla: Health Care Privacy - Part 3 | Therapist LL4 | `544fb3f34bdc2d03748b456a` | `686e34706c2a18ed6b0eb41b` |
| 4 | SJ6 TGLabs combat stimulant injector | Meds | 2× Bottle of saline solution + 1× Bottle of hydrogen peroxide | 1 |  | Therapist LL4 | `5c0e531d86f7747fa23f4d42` | `686e34716c2a18ed6b0eb457` |
| 4 | Zagustin hemostatic drug injector | Meds | 46,500 ₽ | 3 |  | Therapist LL4 | `5c0e533786f7747fa23f4d47` | `686e34716c2a18ed6b0eb45d` |

## Weiss: Medicine, Labs and experimental gear

EUR. Opens in Act II (after Q16). Takes over Therapist's meds, keys and cases, class 5–6 armour, night vision and thermals.

| LL | Item | Type | Cost | Limit | Unlock | From | tpl | Offer |
|---|---|---|---|---|---|---|---|---|
| 1 | Dorm room 206 key | Key | 7× Pile of meds | 1 |  | Therapist LL1 | `5938603e86f77435642354f4` | `686e34726c2a18ed6b0eb4c0` |
| 1 | Dorm room 303 key | Key | 7× T-Shaped plug + 3× Insulating tape | 1 |  | Therapist LL1 | `593aa4be86f77457f56379f8` | `686e34716c2a18ed6b0eb499` |
| 1 | Portable bunkhouse key | Key | 1× Pack of Vita juice + 1× Pack of milk + 1× Toilet paper | 1 |  | Therapist LL1 | `5938144586f77473c2087145` | `686e34726c2a18ed6b0eb4cf` |
| 1 | Armasight Vulcan universal base | Mod: Mount | 19.73 € | 5 |  | Jaeger LL1 | `5b3b6dc75acfc47a8773fb1e` | `686e34226c2a18ed6b0e936f` |
| 1 | L3Harris AN/PVS-14 night vision monocular | Mod: NightVision | 2× Broken GPhone smartphone + 3× Broken LCD | 1 |  | Mechanic LL1 | `57235b6f24597759bf5a30f1` | `686e34336c2a18ed6b0e9a3f` |
| 1 | PNV-57E night vision goggles | Mod: NightVision | 2× Apollo Soyuz cigarettes | 3 |  | Prapor LL1 | `67506ca81f18589016006aa6` | `686e346d6c2a18ed6b0eb25c` |
| 1 | Armasight Vulcan MG 3.5x Bravo night vision scope | Mod: SpecialScope | 1× Electric drill + 1× Broken GPhone smartphone | 5 |  | Mechanic LL1 | `5b3b6e495acfc4330140bd88` | `686e34346c2a18ed6b0e9a9d` |
| 1 | NSPU-M 3.5x dovetail night vision scope | Mod: SpecialScope | 112 € | 3 |  | Prapor LL1 | `5a7c74b3e899ef0014332c29` | `686e34626c2a18ed6b0eac56` |
| 1 | Bottle of OLOLO Multivitamins | Other | 5× Apollo Soyuz cigarettes | 5 | S1 Real Life Wacka Mole (suggested); vanilla: Bad Habit | Therapist LL1 | `62a0a043cf4a99369e2624a5` | `686e34726c2a18ed6b0eb4cc` |
| 1 | Dogtag case | Other | 2,568 € | 1 |  | Therapist LL1 | `5c093e3486f77430cb02e593` | `686e34716c2a18ed6b0eb445` |
| 1 | Pile of meds | Other | 3× Crickent lighter + 2× Classic matches | 4 |  | Therapist LL1 | `5d1b3a5d86f774252167ba22` | `686e34716c2a18ed6b0eb47e` |
| 1 | Toothpaste | Other | 2× Ortodontox toothpaste | 2 |  | Therapist LL1 | `57347c93245977448d35f6e3` | `686e34726c2a18ed6b0eb4b7` |
| 2 | Dorm room 220 key | Key | 1× Pack of Arseniy buckwheat + 1× Aquapeps water purification tablets + 5× Pile of meds | 1 |  | Therapist LL2 | `5780cfa52459777dfb276eb1` | `686e34726c2a18ed6b0eb4c6` |
| 2 | Health Resort west wing room 221 key | Key | 8× Pack of chlorine | 1 |  | Therapist LL2 | `5a0ee37f86f774023657a86f` | `686e34716c2a18ed6b0eb493` |
| 2 | Aluminum splint | Meds | 2× Disposable syringe | 1 |  | Therapist LL2 | `5af0454c86f7746bf20992e8` | `686e34716c2a18ed6b0eb45a` |
| 2 | Army bandage | Meds | 16.98 € | 20 | S10 It Must Be The Illuminati! (suggested); vanilla: Operation Aquarius - Part 2 | Therapist LL2 | `5751a25924597722c463c472` | `686e34706c2a18ed6b0eb418` |
| 2 | Grizzly medical kit | Meds | 1× Gas analyzer + 1× Ultraviolet lamp | 2 | S11 Super Trooper (suggested); vanilla: Lost Contact | Therapist LL2 | `590c657e86f77412b013051d` | `686e34716c2a18ed6b0eb44e` |
| 2 | IFAK individual first aid kit | Meds | 1× Pack of sodium bicarbonate | 3 |  | Therapist LL2 | `590c678286f77426c9660122` | `686e34706c2a18ed6b0eb3f7` |
| 2 | Surv12 field surgical kit | Meds | 1× Antique vase | 1 | S12 Discombobulated - Part 1 (suggested); vanilla: Broadcast - Part 3 | Jaeger LL2 | `5d02797c86f774203f38e30a` | `686e34276c2a18ed6b0e95b9` |
| 2 | PNV-10T night vision goggles | Mod: NightVision | 240 € | 2 |  | Skier LL2 | `5c0696830db834001d23f5da` | `686e34116c2a18ed6b0e8d7f` |
| 2 | 42 Signature Blend English Tea | Other | 4× Can of Ice Green tea | 2 |  | Therapist LL2 | `5bc9be8fd4351e00334cae6e` | `686e34716c2a18ed6b0eb496` |
| 2 | Documents case | Other | 1× Cat figurine + 1× Bronze lion figurine + 4× Horse figurine | 1 |  | Therapist LL2 | `590c60fc86f77412b13fddcf` | `686e34716c2a18ed6b0eb451` |
| 2 | Expeditionary fuel tank | Other | 4× Pack of Arseniy buckwheat | 1 |  | Therapist LL2 | `5d1b371186f774253763a656` | `686e34726c2a18ed6b0eb4ab` |
| 2 | Key tool | Other | 10× Bottle of hydrogen peroxide + 10× Bottle of saline solution + 10× Pack of chlorine | 1 |  | Therapist LL2 | `59fafd4b86f7745ca07e1232` | `686e34706c2a18ed6b0eb427` |
| 2 | Medicine case | Other | 7× Medical bloodset + 7× Disposable syringe + 2× Vaseline balm + 4× Medical tools | 1 |  | Therapist LL2 | `5aafbcd986f7745e590fff23` | `686e34716c2a18ed6b0eb475` |
| 2 | Pistol case | Other | 6× Pile of meds + 4× Disposable syringe | 1 |  | Therapist LL2 | `567143bf4bdc2d1a0f8b4567` | `686e34706c2a18ed6b0eb433` |
| 3 | RB-AK key | Key | 2× Canister with purified water + 2× Water filter | 1 |  | Therapist LL3 | `5d80c78786f774403a401e3e` | `686e34716c2a18ed6b0eb484` |
| 3 | Cyclone Shakhin mount | Mod: Mount | 6.04 € | 5 |  | Prapor LL3 | `67641a851b2899700609901a` | `686e346e6c2a18ed6b0eb2d4` |
| 3 | Armasight N-15 night vision goggles | Mod: NightVision | 604 € | 2 |  | Peacekeeper LL3 | `5c066e3a0db834001b7353f0` | `686e344e6c2a18ed6b0ea3fd` |
| 3 | L3Harris GPNVG-18 night vision goggles | Mod: NightVision | 1× Bottle of Fierce Hatchling moonshine | 1 |  | Peacekeeper LL3 | `5c0558060db834001b735271` | `686e34516c2a18ed6b0ea538` |
| 3 | Cyclone Shakhin 3.7x thermal scope | Mod: SpecialScope | 5× Secure Flash drive + 2× Topographic survey maps | 1 |  | Prapor LL3 | `67641b461c2eb66ade05dba6` | `686e346e6c2a18ed6b0eb289` |
| 3 | FLIR RS-32 2.25-9x 35mm 60Hz thermal riflescope | Mod: SpecialScope | 10× Pack of sugar + 6× Aquamari water bottle with filter | 1 |  | Jaeger LL3 | `5d1b5e94d7ad1a2b865a96b0` | `686e34236c2a18ed6b0e9439` |
| 3 | SIG Sauer ECHO1 1-2x30mm 30Hz thermal reflex scope | Mod: SpecialScope | 1,343 € |  | S14 A Tasty Treat (current) | current RTT2 stock | `6478641c19d732620e045e17` | `6afeb415c2377a139fe30289` |
| 3 | Torrey Pines Logic T12W 30Hz thermal reflex sight | Mod: SpecialScope | 735 € | 1 |  | Mechanic LL3 | `609bab8b455afd752b2e6138` | `686e343f6c2a18ed6b0e9edd` |
| 3 | Trijicon REAP-IR thermal scope | Mod: SpecialScope | 1,866 € |  | S8 Smooth Brains - Part 2 (current) | current RTT2 stock | `5a1eaa87fcdbcb001865f75e` | `6afeb40dd169672825b0306b` |
| 3 | Altyn helmet face shield | Other | 3× Altyn helmet face shield | 3 |  | Ragman LL3 | `5aa7e373e5b5b000137b76f0` | `686e34086c2a18ed6b0e88b6` |
| 3 | Item case | Other | 15,193 € | 1 |  | Therapist LL3 | `59fb042886f7746c5005a7b2` | `686e34706c2a18ed6b0eb3ee` |
| 3 | Keycard holder case | Other | 3,798 € | 1 |  | Therapist LL3 | `619cbf9e0a7c3a1a2731940a` | `686e34726c2a18ed6b0eb49f` |
| 3 | LEDX Skin Transilluminator | Other | 20× Dogtag USEC + 140× Dogtag USEC | 1 |  | Therapist LL3 | `5c0530ee86f774697952d952` | `686e34726c2a18ed6b0eb4b1` |
| 3 | Korund-VM ballistic plate (Back) | Plate (class 5) | 248 € | 5 |  | Prapor LL3 | `657b2797c3dbcb01d60c35ea` | `686e346d6c2a18ed6b0eb1f4` |
| 3 | Korund-VM ballistic plates (Front) | Plate (class 5) | 1× Golden egg | 2 | S13 Discombobulated - Part 2 (suggested); vanilla: Reconnaissance | Prapor LL3 | `656f664200d62bcd2e024077` | `686e346b6c2a18ed6b0eb140` |
| 3 | SSAPI level III+ ballistic plate (Side) | Plate (class 5) | 71.09 € | 8 |  | Peacekeeper LL3 | `6557458f83942d705f0c4962` | `686e345a6c2a18ed6b0ea96c` |
| 4 | FORT Defender-2 body armor | Armour (class 5) | 1× Fierce Blow sledgehammer | 1 |  | Ragman LL4 | `5e9dacf986f774054d6b89f4` | `686e340b6c2a18ed6b0e8b1e` |
| 4 | FORT Redut-M body armor | Armour (class 5) | 2× Battered antique book + 4× Tech manual | 1 | S20 My Masterpiece (suggested); vanilla: Charisma Brings Success | Ragman LL4 | `5ca2151486f774244a3b8d30` | `686e340a6c2a18ed6b0e8a9a` |
| 4 | Hexatac HPC Plate Carrier (MultiCam Black) | Armour (class 5) | 3× Roler Submariner gold wrist watch | 2 |  | Ragman LL4 | `63737f448b28897f2802b874` | `686e340a6c2a18ed6b0e8a77` |
| 4 | IOTV Gen4 body armor (Assault Kit, MultiCam) | Armour (class 5) | 1,532 € | 1 | S20 My Masterpiece (suggested); vanilla: Textile - Part 1 | Ragman LL4 | `5b44cf1486f77431723e3d05` | `686e34096c2a18ed6b0e89a3` |
| 4 | IOTV Gen4 body armor (Full Protection Kit, MultiCam) | Armour (class 5) | 2× VPX Flash Storage Module + 2× SAS drive | 1 |  | Ragman LL4 | `5b44cd8b86f774503d30cba2` | `686e340c6c2a18ed6b0e8b8d` |
| 4 | NPP KlASS Korund-VM body armor (Black) | Armour (class 5) | 1,384 € | 1 |  | Prapor LL4 | `5f5f41476bdad616ad46d631` | `686e34686c2a18ed6b0eaf4d` |
| 4 | FORT Redut-T5 body armor (Smog) | Armour (class 6) | 3× Bronze lion figurine | 1 | S21 Ultimate Body (suggested); vanilla: Supervisor | Ragman LL4 | `5ca21c6986f77479963115a7` | `686e34086c2a18ed6b0e88f8` |
| 4 | Altyn bulletproof helmet (Olive Drab) | Headwear (class 5) | 3× Round pliers + 1× Hand drill + 3× Pack of nails | 1 | S21 Ultimate Body (suggested); vanilla: Calibration | Ragman LL4 | `5aa7e276e5b5b000171d0647` | `686e34066c2a18ed6b0e8813` |
| 4 | Vulkan-5 LShZ-5 bulletproof helmet (Black) | Headwear (class 5) | 1× Graphics card | 1 |  | Ragman LL4 | `5ca20ee186f774799474abc2` | `686e34076c2a18ed6b0e8882` |
| 4 | Kiba Arms outer door key | Key | 60× Can of condensed milk + 10× Pack of oat flakes | 1 |  | Therapist LL4 | `5ad5d7d286f77450166e0a89` | `686e34706c2a18ed6b0eb436` |
| 4 | AFAK tactical individual first aid kit | Meds | 410 € | 2 | S20 My Masterpiece (suggested); vanilla: Wet Job - Part 5 | Peacekeeper LL4 | `60098ad7c2240c0fe85c570a` | `686e34546c2a18ed6b0ea698` |
| 4 | Armasight Zeus universal base | Mod: Mount | 20.04 € | 5 |  | Jaeger LL4 | `63fc449f5bd61c6cf3784a88` | `686e342b6c2a18ed6b0e9730` |
| 4 | Armasight Zeus-Pro 640 2-8x50 30Hz thermal scope | Mod: SpecialScope | 1× LEDX Skin Transilluminator | 1 | S20 My Masterpiece (suggested); vanilla: The Huntsman Path - Big Game | Jaeger LL4 | `63fc44e2429a8a166c7f61e6` | `686e34296c2a18ed6b0e9660` |
| 4 | MP-155 Ultima thermal camera | Mod: SpecialScope | 2× NIXXOR lens | 1 | S21 Ultimate Body (suggested); vanilla: The Huntsman Path - Eraser - Part 2 | Jaeger LL4 | `606f2696f2cb2e02a42aceb1` | `686e34266c2a18ed6b0e9526` |
| 4 | T-7 Thermal Goggles with a Night Vision mount | Mod: ThermalVision | 4,851 € |  | S20 My Masterpiece (current) | current RTT2 stock | `5c110624d174af029e69734c` | `6afeb41b45a92a0ad3ca0fa5` |
| 4 | LShZ-2DTM aventail | Other | 275 € | 4 |  | Ragman LL4 | `5d6d3be5a4b9361bc73bc763` | `686e340a6c2a18ed6b0e8a41` |
| 4 | Maska-1SCh face shield (Olive Drab) | Other | 2× Propane tank (5L) | 1 |  | Prapor LL4 | `5c0919b50db834001b7ce3b9` | `686e34666c2a18ed6b0eae4f` |
| 4 | Money case | Other | 5× Golden neck chain + 2× Roler Submariner gold wrist watch + 2× Gold skull ring | 1 |  | Therapist LL4 | `59fb016586f7746d0d4b423a` | `686e34706c2a18ed6b0eb415` |
| 4 | Ops-Core SLAAP armor helmet plate (Tan) | Other | 811 € | 5 | S20 My Masterpiece (suggested); vanilla: The Guide | Peacekeeper LL4 | `5c0e66e2d174af02a96252f4` | `686e344e6c2a18ed6b0ea41a` |
| 4 | Rys-T face shield | Other | 4× Piece of plexiglass + 1× Bolts | 1 |  | Ragman LL4 | `5f60c85b58eff926626a60f7` | `686e340b6c2a18ed6b0e8aa6` |
| 4 | T H I C C item case | Other | 15× Portable defibrillator + 15× LEDX Skin Transilluminator + 15× Ibuprofen painkillers + 15× Toothpaste | 1 |  | Therapist LL4 | `5c0a840b86f7742ffa4f2482` | `686e34716c2a18ed6b0eb442` |
| 4 | Experimental Lightweight L.I.M.P. | Plate | 1,343 € |  | S21 Ultimate Body (current) | current RTT2 stock | `69d44b9ec379dcfd2bf8de40` | `6afeb41ded8527ecb98f22b4` |
| 4 | Cult Locust ballistic plate | Plate (class 5) | 1× Golden rooster figurine | 2 | S21 Ultimate Body (suggested); vanilla: Peacekeeping Mission | Skier LL4 | `656fa8d700d62bcd2e024084` | `686e34196c2a18ed6b0e905b` |
| 4 | Granit 4 ballistic plate (Front) | Plate (class 5) | 356 € | 2 | S20 My Masterpiece (suggested); vanilla: Energy Crisis | Prapor LL4 | `656f611f94b480b8a500c0db` | `686e346d6c2a18ed6b0eb240` |
| 4 | Granit Br4 ballistic plate | Plate (class 5) | 1× Wooden clock | 4 | S21 Ultimate Body (suggested); vanilla: Sales Night | Ragman LL4 | `65573fa5655447403702a816` | `686e340b6c2a18ed6b0e8b4e` |
| 4 | Korund-VM ballistic plate (Side) | Plate (class 5) | 62.04 € | 6 |  | Prapor LL4 | `654a4f8bc721968a4404ef18` | `686e346c6c2a18ed6b0eb1cc` |
| 4 | SAPI level III+ ballistic plate | Plate (class 5) | 1× SAS drive | 5 | S21 Ultimate Body (suggested); vanilla: Insomnia | Peacekeeper LL4 | `655746010177119f4a097ff7` | `686e345a6c2a18ed6b0ea94c` |
| 4 | CQC Osprey MK4A plate carrier (Protection, MTP) | Rig (class 5) | 3× SAS drive | 1 |  | Peacekeeper LL4 | `60a3c68c37ea821725773ef5` | `686e34566c2a18ed6b0ea778` |
| 4 | NPP KlASS Bagariy plate carrier (EMR) | Rig (class 5) | 1,085 € | 2 |  | Ragman LL4 | `628d0618d1ba6e4fa07ce5a4` | `686e340a6c2a18ed6b0e8a82` |
| 4 | Tasmanian Tiger Plate Carrier MKIII (Coyote Brown) | Rig (class 5) | 3× Veritas guitar pick + 2× Old firesteel | 3 |  | Ragman LL4 | `66b6295a8ca68c6461709efa` | `686e340c6c2a18ed6b0e8bd1` |

## Voron: Cult, stealth and high-penetration Russian ammo

RUB, mostly barters. Opens in Act III (after Q20). Takes over 9x39 guns and ammo, Russian ammo at 40+ penetration, and knives.

| LL | Item | Type | Cost | Limit | Unlock | From | tpl | Offer |
|---|---|---|---|---|---|---|---|---|
| 1 | Labrys access keycard | Key | 121,000 ₽ |  | Q25 Daedalus' Curse (current) | current RTT2 stock | `679b9819a2f2dd4da9023512` | `6afe7ed50a628975841f95ac` |
| 1 | Cultist knife | Melee | 1× Bottle of Fierce Hatchling moonshine + 1× Raven figurine |  | V1 Welcome to the Family - Part 1 (current) | current RTT2 stock | `5fc64ea372b0dd78d51159dc` | `6afeb324c44ae2aae78f953a` |
| 1 | PB 9x18PM sound suppressor | Mod: Silencer | 10,600 ₽ | 3 |  | Prapor LL1 | `56e05b06d2720bb2668b4586` | `686e346e6c2a18ed6b0eb2d7` |
| 2 | 5.45x39mm 7N40 | Ammo (pen 42) | 650 ₽ | 150 | V9 The Eye Requires Munitions - Part 1 (current) | current RTT2 stock | `61962b617c6c7b169525f168` | `6afeb32f8824b9ad3f4ee400` |
| 2 | 7.62x51mm M80A1 | Ammo (pen 60) | 900 ₽ | 120 | V6 Welcome to the Family - Part 6 (current) | current RTT2 stock | `6768c25aa7b238f14a08d3f6` | `6afeb329a6457b3b32f01ccb` |
| 2 | 6Kh5 Bayonet | Melee | 2× Aquamari water bottle with filter + 1× Gas mask air filter | 2 |  | Prapor LL2 | `5bffdc370db834001d23eca8` | `686e34656c2a18ed6b0eae27` |
| 2 | MPL-50 entrenching tool | Melee | 2× Pompon hat | 2 |  | Prapor LL2 | `5bead2e00db834001c062938` | `686e34656c2a18ed6b0eadf1` |
| 2 | 9A-91 9x39 sound suppressor | Mod: Silencer | 21,800 ₽ | 2 |  | Prapor LL2 | `64527a3a7da7133e5a09ca99` | `686e346d6c2a18ed6b0eb247` |
| 3 | VSS Vintorez 9x39 special sniper rifle | Gun | 1× Ratchet wrench + 1× Gunpowder "Kite" | 1 |  | Prapor LL3 | `57838ad32459774a17445cd2` | `686e346b6c2a18ed6b0eb129` |
| 3 | 7.62x54mm R T-46M gzh | Ammo (pen 41) | 389 ₽ | 120 |  | Prapor LL3 | `5e023cf8186a883be655e54f` | `686e34686c2a18ed6b0eafc1` |
| 3 | 5.45x39mm BP gs | Ammo (pen 45) | 750 ₽ | 150 | V10 The Eye Requires Munitions - Part 2 (current) | current RTT2 stock | `56dfef82d2720bbd668b4567` | `6afeb330ee909155fdd53272` |
| 3 | 7.62x39mm BP gzh | Ammo (pen 47) | 850 ₽ | 150 | V10 The Eye Requires Munitions - Part 2 (current) | current RTT2 stock | `59e0d99486f7744a32234762` | `6afeb330ee909155fdd53276` |
| 3 | Camper axe | Melee | 5× Toothpaste + 5× Toilet paper + 2× Bottle of hydrogen peroxide | 1 |  | Jaeger LL3 | `5c012ffc0db834001d23f03f` | `686e34226c2a18ed6b0e93a5` |
| 3 | Red Rebel ice pick | Melee | 15× Propane tank (5L) + 10× Fuel conditioner + 15× Dry fuel | 1 |  | Jaeger LL3 | `5c0126f40db834002a125382` | `686e34256c2a18ed6b0e94be` |
| 3 | AKS-74U PBS-4 5.45x39 sound suppressor | Mod: Silencer | 36,000 ₽ | 4 | V12 The Eye Never Forgets (suggested); vanilla: Shaking Up the Teller | Prapor LL3 | `57ffb0e42459777d047111c5` | `686e34646c2a18ed6b0ead87` |
| 4 | AS VAL 9x39 special assault rifle | Gun | 159,500 ₽ | 1 |  | Prapor LL4 | `57c44b372459772d2b39b8ce` | `686e34626c2a18ed6b0eac79` |
| 4 | SR-3M 9x39 compact assault rifle | Gun | 147,800 ₽ | 2 | V17 Reap The Wicked (suggested); vanilla: Perfect Mediator | Prapor LL4 | `651450ce0e00edc794068371` | `686e346e6c2a18ed6b0eb2a6` |
| 4 | 7.62x39mm PP gzh | Ammo (pen 41) | 774 ₽ | 120 |  | Prapor LL4 | `64b7af434b75259c590fa893` | `686e346a6c2a18ed6b0eb0a7` |
| 4 | 7.62x54mm R PS gzh | Ammo (pen 45) | 1,003 ₽ | 90 | V17 Reap The Wicked (suggested); vanilla: The Punisher - Part 6 | Prapor LL4 | `59e77a2386f7742ee578960a` | `686e346e6c2a18ed6b0eb2c2` |
| 4 | 12.7x55mm PS12B | Ammo (pen 46) | 981 ₽ | 60 |  | Prapor LL4 | `5cadf6eeae921500134b2799` | `686e34666c2a18ed6b0eaeaf` |
| 4 | .338 Lapua Magnum FMJ | Ammo (pen 47) | 1,600 ₽ | 40 | V11 The Eye Requires Munitions - Part 3 (current) | current RTT2 stock | `5fc275cf85fd526b824a571a` | `6afeb331ea2105fd5ee9ba20` |
| 4 | 9x39mm SP-6 gs | Ammo (pen 48) | 1,003 ₽ | 60 | V18 Reap The Unfortunate (suggested); vanilla: Capturing Outposts | Prapor LL4 | `57a0e5022459774d1673f889` | `686e34646c2a18ed6b0ead78` |
| 4 | 7.62x39mm MAI AP | Ammo (pen 58) | 2,783 ₽ | 30 | V16 The Eye Requires Pickup - Part 4 (suggested); vanilla: The Punisher. Harvest | Peacekeeper LL4 | `601aa3d2b2bcb34913271e6d` | `656629d07cac3c3b160e63fd` |
| 4 | .338 Lapua Magnum AP | Ammo (pen 79) | 4,500 ₽ | 40 | V11 The Eye Requires Munitions - Part 3 (current) | current RTT2 stock | `5fc382a9d724d907e2077dab` | `6afeb331ea2105fd5ee9ba24` |
| 4 | Crash Axe | Melee | 1× Dorm room 314 marked key + 1× Health Resort west wing office room 112 key + 5× Paracord | 1 | V19 Reap the Cursed (suggested); vanilla: Scavenger | Ragman LL4 | `5bffe7930db834001b734a39` | `686e34096c2a18ed6b0e8995` |
| 4 | Miller Bros. Blades M-2 Tactical Sword | Melee | 2× Military COFDM Wireless Signal Transmitter + 1× Military checkpoint key + 2× Chain with Prokill medallion + 2× Phased array element | 1 | V20 One Final Delivery (suggested); vanilla: Flint | Skier LL4 | `5bffdd7e0db834001b734a1a` | `686e34116c2a18ed6b0e8d82` |
| 4 | SOG Voodoo Hawk tactical tomahawk | Melee | 1× SP-8 Survival Machete + 1× 6Kh5 Bayonet + 1× Crash Axe | 1 | V16 The Eye Requires Pickup - Part 4 (suggested); vanilla: Slaughterhouse | Jaeger LL4 | `63920105a83e15700a00f168` | `686e34296c2a18ed6b0e967b` |
| 4 | AS VAL 9x39 integral barrel-suppressor | Mod: Silencer | 25,400 ₽ | 5 |  | Prapor LL4 | `57c44dd02459772d2e0ae249` | `686e346e6c2a18ed6b0eb25f` |
