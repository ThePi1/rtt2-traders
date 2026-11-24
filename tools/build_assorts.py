"""Build the RTT2 trader assorts from ASSORTS.md.

Every row of a trader's table in ASSORTS.md becomes an offer in data/<code>-assort.json, except the rows marked
"current RTT2 stock", which are already there and are left alone. A row's gun or armour parts, and its barter
price, are copied from the vanilla offer in its Offer column. A row with a quest in its Unlock column is locked
behind that quest: the offer goes in the trader's QuestAssort file, and the quest gets an AssortmentUnlock reward.

Everything this script writes has an id starting with GEN_PREFIX. Each run first removes what the last run wrote,
so after editing ASSORTS.md you just run it again. Run from the repo root:

    python tools/build_assorts.py [--game <SPT_Data/database folder>] [--check]

--check reports what would change without writing anything.
"""
import argparse
import glob
import hashlib
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

GEN_PREFIX = "a55027"
TRADERS = ["Chimera", "Xiaoming", "Atlas", "Price", "Needle", "Weiss", "Voron"]
VANILLA = ["54cb50c76803fa8b248b4571", "54cb57776803fa99248b456e", "58330581ace78e27b8b10cee", "5935c25fb3acc3127c3d8cd9",
           "5a7c2eca46aef81a7ca2145d", "5ac3b934156ae10c4430e83c", "5c0647fdd443bc2504c2d371"]
CURRENCY = {"₽": "5449016a4bdc2d6f028b456f", "$": "5696686a4bdc2da3298b456a", "€": "569668774bdc2da2298b4568"}
CURRENT = "current RTT2 stock"


def load(path):
    """A JSON file and its layout (indent, line endings, BOM, final newline), so it can be written back the same way."""
    raw = open(path, "rb").read()
    text = raw.decode("utf-8-sig")
    body = text.replace("\r\n", "\n")
    data = json.loads(body)
    for indent in (4, 2, "\t"):
        for ascii_ in (False, True):
            out = json.dumps(data, indent=indent, ensure_ascii=ascii_)
            for tail in ("", "\n"):
                if out + tail == body:
                    return data, dict(indent=indent, ascii=ascii_, tail=tail, crlf="\r\n" in text, bom=raw.startswith(b"\xef\xbb\xbf"))
    if isinstance(data, dict) and not any(data.values()):  # (an empty, hand-written file: use the other assorts' layout)
        return data, dict(indent=2, ascii=False, tail="", crlf="\r\n" in text, bom=raw.startswith(b"\xef\xbb\xbf"))
    sys.exit(f"{path}: can't tell how this file is laid out, so it can't be rewritten safely")


def dump(data, layout):
    text = json.dumps(data, indent=layout["indent"], ensure_ascii=layout["ascii"]) + layout["tail"]
    if layout["crlf"]:
        text = text.replace("\n", "\r\n")
    return (b"\xef\xbb\xbf" if layout["bom"] else b"") + text.encode("utf-8")


def gen_id(*parts):
    return GEN_PREFIX + hashlib.md5(":".join(parts).encode()).hexdigest()[: 24 - len(GEN_PREFIX)]


def is_gen(i):
    return isinstance(i, str) and i.startswith(GEN_PREFIX)


def read_tables(path):
    """{trader: [row dict]} from ASSORTS.md's per-trader tables."""
    tables, trader = {}, None
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        m = re.match(r"^## (\w+): ", line)
        if m:
            trader = m.group(1) if m.group(1) in TRADERS else None
            continue
        if trader is None or not line.startswith("| ") or line.startswith("| LL |") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) != 9:
            sys.exit(f"ASSORTS.md line {n}: expected 9 columns, found {len(cells)}")
        ll, item, kind, cost, limit, unlock, src, tpl, offer = cells
        tables.setdefault(trader, []).append(dict(line=n, ll=int(ll), item=item, cost=cost, limit=limit, unlock=unlock, src=src,
                                                  tpl=tpl.strip("`"), offer=offer.strip("`")))
    return tables


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", default="I:/Games/SPT-4-1-6-testing/SPT_Runtime/SPT_Data/database")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    # quest rows (A5, Q16 ...) -> quest ids, from the tracker
    quest_ids = {}
    for line in open("QUESTS.md", encoding="utf-8"):
        c = line.split(" | ")
        if len(c) > 8 and re.match(r"^\| [A-Z]+\d+$", c[0]):
            quest_ids[c[0][2:]] = c[6].strip("` ")
    bases = {}
    for f in glob.glob("data/*-base.json"):
        b = json.loads(open(f, encoding="utf-8-sig").read())
        bases[b["nickname"]] = (b["_id"], f.replace("\\", "/").split("/")[-1].split("-")[0])
    # vanilla offers by id: (the offer's parts, its price)
    vanilla = {}
    for tid in VANILLA:
        a = json.load(open(f"{args.game}/traders/{tid}/assort.json", encoding="utf-8-sig"))
        kids = {}
        for i in a["items"]:
            kids.setdefault(i.get("parentId"), []).append(i)
        def tree(i):
            return [i] + [x for k in kids.get(i["_id"], []) for x in tree(k)]
        for r in kids.get("hideout", []):
            vanilla[r["_id"]] = (tree(r), a["barter_scheme"][r["_id"]][0])

    files, problems = {}, []
    def get(path):
        if path not in files:
            files[path] = load(path)
        return files[path][0]

    quest_file = {}
    for f in glob.glob("db/CustomQuests/*/Quests/*.json"):
        d = get(f)
        for q in (d.values() if isinstance(d, dict) else d):
            quest_file[q["_id"]] = q
    # undo the last run: generated offers, quest locks and unlock rewards
    removed = 0
    for q in quest_file.values():
        rewards = q["rewards"].get("Success") or []
        keep = [r for r in rewards if not (r.get("type") == "AssortmentUnlock" and is_gen(r.get("id")))]
        removed += len(rewards) - len(keep)
        if len(keep) != len(rewards):
            q["rewards"]["Success"] = keep

    tables = read_tables("ASSORTS.md")
    summary = {}
    for trader in TRADERS:
        tid, code = bases[trader]
        assort = get(f"data/{code}-assort.json")
        qa_path = glob.glob(f"db/CustomQuests/{tid}/QuestAssort/*.json")[0]
        qa = get(qa_path)
        gen_roots = {i["_id"] for i in assort["items"] if i.get("parentId") == "hideout" and is_gen(i["_id"])}
        def under_gen(i, by_id={i["_id"]: i for i in assort["items"]}):
            while i.get("parentId") not in (None, "hideout"):
                i = by_id.get(i["parentId"], {})
            return i.get("_id") in gen_roots
        assort["items"] = [i for i in assort["items"] if not under_gen(i)]
        for k in ("barter_scheme", "loyal_level_items"):
            assort[k] = {a: v for a, v in assort[k].items() if not is_gen(a)}
        for section in qa.values():
            for a in [a for a in section if is_gen(a)]:
                del section[a]
        qa.setdefault("success", {})

        added = locked = 0
        for row in tables.get(trader, []):
            if row["src"] == CURRENT:
                continue
            if row["offer"] not in vanilla:
                problems.append(f"line {row['line']} ({trader}, {row['item']}): vanilla offer {row['offer']} not found"); continue
            parts, scheme = vanilla[row["offer"]]
            if parts[0]["_tpl"] != row["tpl"]:
                problems.append(f"line {row['line']} ({trader}, {row['item']}): the offer is for {parts[0]['_tpl']}, not {row['tpl']}"); continue
            ids = {p["_id"]: gen_id(trader, row["offer"], p["_id"]) for p in parts}
            items = []
            for p in parts:
                c = json.loads(json.dumps(p))
                c["_id"] = ids[p["_id"]]
                if p.get("parentId") != "hideout":
                    c["parentId"] = ids[p["parentId"]]
                items.append(c)
            root = items[0]; rid = root["_id"]
            upd = root.setdefault("upd", {})
            for k in ("BuyRestrictionMax", "BuyRestrictionCurrent"):
                upd.pop(k, None)
            if row["limit"]:
                upd["BuyRestrictionMax"] = int(row["limit"]); upd["BuyRestrictionCurrent"] = 0
            m = re.fullmatch(r"([\d,]+(?:\.\d+)?) ([₽$€])", row["cost"])
            if m:
                count = float(m.group(1).replace(",", ""))
                price = [[{"count": int(count) if count.is_integer() else count, "_tpl": CURRENCY[m.group(2)]}]]
            else:
                if len(row["cost"].split(" + ")) != len(scheme):
                    problems.append(f"line {row['line']} ({trader}, {row['item']}): the barter text doesn't match the vanilla offer's barter")
                price = [json.loads(json.dumps(scheme))]
            assort["items"] += items
            assort["barter_scheme"][rid] = price
            assort["loyal_level_items"][rid] = row["ll"]
            added += 1
            # quest lock
            qrow = re.match(r"^([A-Z]+\d+)\b", row["unlock"])
            if row["unlock"] and not qrow:
                problems.append(f"line {row['line']} ({trader}, {row['item']}): unlock '{row['unlock']}' has no quest, so the item is left unlocked")
            if qrow:
                qid = quest_ids.get(qrow.group(1))
                if qid not in quest_file:
                    problems.append(f"line {row['line']} ({trader}, {row['item']}): quest {qrow.group(1)} not found"); continue
                qa["success"][rid] = qid
                reward_ids = {p["_id"]: gen_id("reward", trader, row["offer"], p["_id"]) for p in parts}
                reward_items = []
                for p in parts:
                    c = {k: v for k, v in json.loads(json.dumps(p)).items() if k not in ("parentId", "slotId", "upd")} if p.get("parentId") == "hideout" \
                        else json.loads(json.dumps(p))
                    c["_id"] = reward_ids[p["_id"]]
                    if p.get("parentId") != "hideout":
                        c["parentId"] = reward_ids[p["parentId"]]
                    else:
                        u = {k: v for k, v in (p.get("upd") or {}).items() if k not in ("StackObjectsCount", "UnlimitedCount", "BuyRestrictionMax", "BuyRestrictionCurrent")}
                        if u:
                            c["upd"] = u
                    reward_items.append(c)
                q = quest_file[qid]
                q["rewards"].setdefault("Success", []).append({
                    "availableInGameEditions": [], "gameMode": ["regular", "pve"], "id": gen_id("unlock", trader, row["offer"]), "isHidden": False,
                    "items": reward_items, "loyaltyLevel": row["ll"], "target": reward_items[0]["_id"], "traderId": tid,
                    "type": "AssortmentUnlock", "unknown": False})
                locked += 1
        summary[trader] = (added, locked)

    for trader, (a, l) in summary.items():
        print(f"{trader:9} {a:4} offers added, {l:3} behind quests")
    if removed:
        print(f"(replaced {removed} unlock rewards from the last run)")
    for p in problems:
        print("PROBLEM:", p)
    changed = [f for f, (d, lay) in files.items() if dump(d, lay) != open(f, "rb").read()]
    print(len(changed), "files would change" if args.check else "files changed")
    if not args.check:
        for f in changed:
            open(f, "wb").write(dump(*files[f]))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
