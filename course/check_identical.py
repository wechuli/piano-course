"""Check that finished volumes still generate exactly the same pages.

Every unit's LilyPond code (its exercises, text and pieces) and every volume's front matter is
fingerprinted with SHA-256 and compared with course/fingerprints.json. A finished unit must
never change: the user may have printed it.

Usage: python3 check_identical.py             compare (exit 1 on any difference)
       python3 check_identical.py --add V     record volume V's fingerprints once it is finished
       python3 check_identical.py --add V 1 2 record only units 1 and 2 of volume V (a volume in progress)
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import build  # noqa: E402

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fingerprints.json")


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def fingerprints(vol, units=None):
    out = {"front": sha(build.title_page(vol) + build.how_to_page(vol))}
    for u in build.VOLUMES[vol]["units"]:
        if units is None or u["id"] in units:
            out[f"unit{u['id']}"] = sha(build.unit_pages(u, vol))
    return out


def main():
    stored = json.load(open(FILE)) if os.path.exists(FILE) else {}
    args = sys.argv[1:]
    if args and args[0] == "--add":
        v, units = args[1], [int(x) for x in args[2:]] or None
        stored[v] = fingerprints(int(v), units)
        print(f"recorded Volume {v}" + (f", units {units}" if units else ""))
        json.dump(stored, open(FILE, "w"), indent=1, sort_keys=True)
        return
    bad = 0
    for v, prints in sorted(stored.items()):
        now = fingerprints(int(v), [int(k[4:]) for k in prints if k.startswith("unit")])
        changed = [k for k in prints if now.get(k) != prints[k]]
        print(f"Volume {v}: {'identical' if not changed else 'CHANGED: ' + ', '.join(changed)}")
        bad += len(changed)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
