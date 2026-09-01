import sys, json, subprocess
sys.path.insert(0, "build")
from run import run_sql, parse, NULLTOK
import catalog

PG_VERSION = subprocess.run(
    ["/opt/homebrew/opt/postgresql@16/bin/psql", "-U", "pgmaster", "-d", "pgmaster_demo",
     "-XtAc", "SHOW server_version"], capture_output=True, text=True).stdout.strip()

data, fails = [], []
for f in catalog.FUNCS:
    entry = {"c": f["cat"], "n": f["name"], "g": f["sig"], "d": f["desc"], "q": f["code"].strip()}
    if f.get("setup"):
        entry["s"] = f["setup"].strip()
    if f.get("volatile"):
        entry["v"] = 1
    if f.get("out"):
        entry["o"] = {"m": f["out"][4:] if f["out"].startswith("MSG:") else f["out"], "x": 1}
    else:
        rc, out, err = run_sql(f["code"], f.get("setup"))
        if rc != 0:
            fails.append((f["cat"], f["name"], err.strip().split("\n")[0]))
            continue
        p = parse(out)
        if p[0] == "msg":
            entry["o"] = {"m": p[1]}
        else:
            entry["o"] = {"h": p[2], "r": p[3]}
            if p[1]:
                entry["o"]["p"] = p[1]
    data.append(entry)

if fails:
    print("FAILURES:", *fails, sep="\n  ")
    sys.exit(1)

counts = {}
for e in data:
    counts[e["c"]] = counts.get(e["c"], 0) + 1
print(f"{len(data)} functions verified against PostgreSQL {PG_VERSION}")
for cid, label, colour in catalog.CATS:
    print(f"  {label:<34} {counts.get(cid, 0)}")

payload = {
    "version": PG_VERSION,
    "cats": [{"id": c, "label": l, "color": k} for c, l, k in catalog.CATS],
    "funcs": data,
}
json.dump(payload, open("build/payload.json", "w"), separators=(",", ":"))
tpl = open("build/template.html").read()
html = (tpl.replace("__PAYLOAD__", json.dumps(payload, separators=(",", ":")))
           .replace("__PGVERSION__", PG_VERSION)
           .replace("__COUNT__", str(len(data))))
open("index.html", "w").write(html)
print("wrote index.html", round(len(html) / 1024), "KB")
