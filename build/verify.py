import sys, json
sys.path.insert(0, "build")
from run import run_sql, parse
import catalog

fails = []
results = {}
for f in catalog.FUNCS:
    if f.get("out"):
        continue
    rc, out, err = run_sql(f["code"], f.get("setup"))
    if rc != 0:
        fails.append((f["cat"], f["name"], err.strip().split("\n")[0][:150]))
    else:
        results[f["cat"] + "/" + f["name"]] = parse(out)
print(f"ran {len(results)+len(fails)}  ok {len(results)}  FAIL {len(fails)}")
for c, n, e in fails:
    print(f"  [{c}] {n}: {e}")
json.dump({k: v for k, v in results.items()}, open("build/results.json", "w"), indent=1)
