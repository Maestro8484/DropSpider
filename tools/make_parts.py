"""Parts to buy, from the bill of materials.

Reads bom/BOM.csv and writes:
  docs/parts.md                      the full list: what to buy, the links, the "only if" rows
  README.md, between <!-- parts:start --> and <!-- parts:end -->
                                     the short version: the disclosure line, the total, the main table

    python tools/make_parts.py            write both (only if something changed)
    python tools/make_parts.py --check    exit 1 if either file is stale against the CSV (check_repo runs this)
    python tools/make_parts.py --no-tag   plain Amazon links, no Associates tag

Rules, all decided by the CSV, never by hand here:
  status "have", "TO BUY" or "owner's stock" -> the main table (a note starting "spare" means a spare I had: left out)
  status starting "ONLY IF"            -> the "only if" table
  "not needed", "parked",
  "ceiling install only", source "printed" -> left out (the print list covers the printed parts)
  source amazon.com with an ASIN        -> https://www.amazon.com/dp/<ASIN>?tag=maestro8484-20
  source dfrobot.com                    -> the DFRobot product page
  anything else                         -> "any hardware store" or "any", with the spec in the item column
  column price_now_usd, if present      -> a Price column and the total of the main table's priced rows

The CSV's first line is its header; extra columns are fine. The notes shown to a builder come from the
notes column unless PUBLIC_NOTE below has a shorter one for that row (the CSV note is written for me).
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOM = os.path.join(ROOT, "bom", "BOM.csv")
PARTS_MD = os.path.join(ROOT, "docs", "parts.md")
README = os.path.join(ROOT, "README.md")
TAG = "maestro8484-20"
DISCLOSURE = "As an Amazon Associate I earn from qualifying purchases. The Amazon links below carry my tag; the price is the same for you."
DFROBOT = {"SEN0691": "https://www.dfrobot.com/product-3081.html"}

GROUP_ORDER = ["Brain and power", "Motor, drive and lock", "Radar and home switch", "Screws and small hardware", "Line and spider"]
GROUP_BY_LETTER = {"C": "Brain and power", "P": "Brain and power", "W": "Brain and power",
                   "M": "Motor, drive and lock", "D": "Motor, drive and lock", "H": "Motor, drive and lock",
                   "S": "Radar and home switch", "N": "Line and spider", "I": "Screws and small hardware"}
GROUP_BY_REF = {"S2": "Motor, drive and lock", "N6": "Brain and power", "N10": "Brain and power",
                "H5": "Screws and small hardware", "H6": "Screws and small hardware", "H7": "Screws and small hardware",
                "H8": "Screws and small hardware", "N8": "Screws and small hardware", "N9": "Screws and small hardware"}

# Shorter notes for a builder where the CSV note is written for me. Everything else shows the CSV note.
PUBLIC_NOTE = {
    "M1": "set the driver to 0.85 V before it moves (build guide, section 07)",
    "D1": "the stepper driver",
    "D2": "the driver plugs into this; it has the screw terminal for 12 V",
    "C1": "a 3 pack; the 38-pin NodeMCU-32S works too, same pin numbers",
    "S5": "the trigger: a 24 GHz mmWave radar that reports how far away someone is and which way they're walking",
    "S3": "the home switch, under the base in the fairlead block",
    "S2": "swings the finger that locks the spool; an MG90 works too",
    "P1": "12 V for the motor; the buck makes 5 V from it for everything else",
    "P2": "fixed 5 V out; meter it before anything is connected",
    "H1": "joins the motor shaft to the rod; blue threadlocker on the set screws",
    "H2": "the axle everything rides on",
    "H3": "the one-way clutch inside the spool; comes as a 5 pack; which way round it goes in matters (doc 05, step 1)",
    "H4": "carries the far end of the rod; comes as a 10 pack",
    "H5": "limit switch to the fairlead block",
    "H8": "the flap's hinge pin",
    "H6": "a 10 mm scrap of printer filament the line is tied round inside the spool",
    "H7": "the radar case's pivot bolt",
    "I1": "fairlead block to the base",
    "I3": "radar mount to the base",
    "I2": "two 6 inch steel corner braces hold the device on the beam; the bolts through the base are yours to place (doc 06)",
    "N8": "spool cap to spool body",
    "N9": "motor to the motor plate",
    "N4": "limp thread that lies flat on the spool and stretches, which is the shock absorber; 7 ft is plenty",
    "N2": "the stopper: slides on the line and lifts the flap when the spider is home",
    "N3": "between the stopper and the spider",
    "N11": "a soft foam spider only, weighted to about 30 g; keep it under 60 g",
    "W1": "the ESP32 sits on one quarter of it in sockets (build guide, section 05b)",
    "W2": "the ESP32's sockets",
    "W3": "signal and power pins on the protoboard",
    "W4": "signals by jumper; the 12 V run in 22 AWG",
    "N10": "radar and switch leads round the end of the base to the board",
    "N6": "12 V from the outlet up to the beam",
    "N13": "the line's guide tube through the base, the kind a 3D printer feeds filament through; on my build it's what keeps the line lined up and the re-spooling smooth",
    "N1": "only if you use braid or fishing line instead of the nylon thread",
    "N5": "only if the board restarts when the finger moves",
}


def rows():
    with open(BOM, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def group_of(ref):
    return GROUP_BY_REF.get(ref) or GROUP_BY_LETTER.get(ref[0], "Screws and small hardware")


def price_of(r):
    p = (r.get("price_now_usd") or "").strip()
    try:
        return float(p)
    except ValueError:
        return None


def qty_number(q):
    m = re.match(r"^\s*(\d+)\s*$", q or "")
    return int(m.group(1)) if m else 1


def link(r, tag):
    src = (r["source"] or "").strip().lower()
    code = (r["asin_or_part"] or "").strip()
    hardware = group_of(r["ref"]) == "Screws and small hardware"
    if src == "amazon.com" and code:
        if (r.get("price_now_usd") or "").strip().lower() == "gone":
            # the listing I bought from is gone: link a search for the same part instead
            words = "+".join(re.sub(r"[^A-Za-z0-9. ]", " ", r["item"].split("(")[0]).split()[:6])
            url = "https://www.amazon.com/s?k=" + words + ("&tag=" + tag if tag else "")
            return "[Amazon search](" + url + ") (my listing is gone)"
        url = "https://www.amazon.com/dp/" + code + ("?tag=" + tag if tag else "")
        return "[Amazon](" + url + ")"
    if src == "dfrobot.com" and code in DFROBOT:
        return "[DFRobot](" + DFROBOT[code] + ")"
    if src.startswith("wawak"):
        return "[WAWAK](https://www.wawak.com/) or any sewing supply"
    return "any hardware store" if hardware else "any"


def note_of(r):
    return PUBLIC_NOTE.get(r["ref"], (r["notes"] or "").strip())


def cell(s):
    return (s or "").replace("|", "/").strip()


def sort_rows(rs):
    return sorted(rs, key=lambda r: (GROUP_ORDER.index(group_of(r["ref"])), rs.index(r)))


def build(tag):
    all_rows = rows()
    priced = any((r.get("price_now_usd") or "").strip() for r in all_rows)
    main, only_if, spares = [], [], []
    for r in all_rows:
        status = (r["status"] or "").strip()
        if (r["source"] or "").strip().lower() == "printed":
            continue
        if status in ("have", "TO BUY", "owner's stock"):
            (spares if (r["notes"] or "").strip().lower().startswith("spare") else main).append(r)
        elif status.upper().startswith("ONLY IF"):
            only_if.append(r)
    main = sort_rows(main)

    total, counted, unpriced = 0.0, 0, []
    for r in main:
        p = price_of(r)
        if p is None:
            if (r["source"] or "").strip().lower() == "amazon.com":
                unpriced.append(r)
            continue
        total += p * qty_number(r["qty"])
        counted += 1

    head = ["| Part | Qty | Where | Note |" + (" Price |" if priced else ""),
            "|---|---|---|---|" + ("---|" if priced else "")]

    def table(rs, when=False):
        out = ["| Part | Qty | Where | " + ("When" if when else "Note") + " |" + (" Price |" if priced and not when else ""),
               "|---|---|---|---|" + ("---|" if priced and not when else "")]
        last = None
        for r in rs:
            g = group_of(r["ref"])
            if not when and g != last:
                out.append("| **" + g + "** | | | |" + (" |" if priced else ""))
                last = g
            when_text = note_of(r)
            p = price_of(r)
            line = "| " + cell(r["item"]) + " | " + cell(r["qty"]) + " | " + link(r, tag) + " | " + cell(when_text) + " |"
            if priced and not when:
                line += (" $%.2f |" % p) if p is not None else " |"
            out.append(line)
        return out

    if priced:
        total_line = ("Parts, if you own none of it: about $%d (today's Amazon prices, %d items; the printer, filament, "
                      "a 12 V adapter and screws you may already have)." % (round(total), counted))
        for r in unpriced:
            paid = (r.get("paid_usd") or "").strip()
            total_line += " Plus the " + cell(r["item"]).split(" (")[0] + ": the listing I bought from is gone" + \
                          (" (it was $%d)" % round(float(paid)) if re.match(r"^\d", paid) else "") + ", so its link is a search for the same part."
    else:
        total_line = "Parts total coming."

    short = [DISCLOSURE, "", total_line, ""] + table(main)
    full = ["# Parts", "",
            "Every part a builder needs for the inverted install (the device turned over on two steel corner braces on the porch beam), "
            "generated from `bom/BOM.csv` by `tools/make_parts.py`. Edit the CSV, not this file. The printed parts are in the print list in "
            "`05_assembly.md`, section A.", "",
            DISCLOSURE, "", total_line, "",
            "## Buy these", ""] + table(main)
    if only_if:
        full += ["", "## Only if", "", "Skip these to start. Each one has a test that says whether you need it.", ""] + table(only_if, when=True)
    skipped = [r for r in all_rows if (r["status"] or "").strip() == "ceiling install only" and (r["source"] or "").strip().lower() != "printed"]
    if skipped or spares:
        full += ["", "## Not on this list", ""]
        if skipped:
            full.append("- The ceiling install's own screws and anchors (BOM rows " + ", ".join(r["ref"] for r in skipped) +
                        ") are in `bom/BOM.csv`; this list is the inverted install.")
        if spares:
            full.append("- Spares I had on the bench and don't use: " + "; ".join(cell(r["item"]) for r in spares) + ".")
    return "\n".join(short) + "\n", "\n".join(full) + "\n"


def splice(text, name, body):
    start, end = "<!-- " + name + ":start -->", "<!-- " + name + ":end -->"
    if start not in text or end not in text:
        return None
    a = text.index(start) + len(start)
    b = text.index(end)
    return text[:a] + "\n" + body + text[b:]


def main():
    tag = "" if "--no-tag" in sys.argv else TAG
    check = "--check" in sys.argv
    short, full = build(tag)
    stale = []

    old = open(PARTS_MD, encoding="utf-8").read() if os.path.exists(PARTS_MD) else ""
    if old != full:
        stale.append("docs/parts.md")
        if not check:
            open(PARTS_MD, "w", encoding="utf-8", newline="\n").write(full)

    readme = open(README, encoding="utf-8").read()
    new = splice(readme, "parts", short)
    if new is None:
        print("README.md has no <!-- parts:start --> / <!-- parts:end --> slot; only docs/parts.md written")
    elif new != readme:
        stale.append("README.md parts slot")
        if not check:
            open(README, "w", encoding="utf-8", newline="\n").write(new)

    if check:
        if stale:
            print("STALE: " + ", ".join(stale) + " (run python tools/make_parts.py)")
            sys.exit(1)
        print("parts list matches bom/BOM.csv")
    else:
        print(("wrote " + ", ".join(stale)) if stale else "nothing changed")


if __name__ == "__main__":
    main()
