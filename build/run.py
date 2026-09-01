import subprocess
PSQL = "/opt/homebrew/opt/postgresql@16/bin/psql"
DB = "pgmaster_demo"
FS, RS, NULLTOK = "\x1f", "\x1e", "\u27eaNULL\u27eb"
TMP = "/tmp/pgm_query.sql"
ARGS = [PSQL, "-U", "pgmaster", "-d", DB, "-X", "-v", "ON_ERROR_STOP=1",
        "-P", "format=unaligned", "-P", "fieldsep=" + FS,
        "-P", "recordsep=" + RS, "-P", "null=" + NULLTOK,
        "-P", "footer=off", "-f", TMP]

def run_sql(code, setup=None):
    script = ("\\o /dev/null\nBEGIN;\n"
              + ((setup.rstrip() + "\n") if setup else "")
              + "\\o\n" + code.rstrip() + "\n"
              + "\\o /dev/null\nROLLBACK;\n")
    open(TMP, "w").write(script)
    p = subprocess.run(ARGS, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr

def parse(stdout):
    """-> ('msg', text) or ('table', preamble_lines, headers, rows)."""
    raw = stdout.rstrip("\n")
    if RS not in raw:
        return ("msg", raw.strip())
    recs = raw.split(RS)
    head = recs[0]
    pre = []
    if "\n" in head:
        before, _, head = head.rpartition("\n")
        pre = [l for l in before.split("\n") if l.strip()]
    return ("table", pre, head.split(FS), [r.split(FS) for r in recs[1:]])

if __name__ == "__main__":
    for q in ["SELECT abs(-17.4) AS abs, sign(-3) AS sign;",
              "SELECT name, dept_id FROM employees LIMIT 2;",
              "CREATE TABLE t(x int);",
              "SELECT setseed(0.42);",
              "SELECT * FROM generate_series(1,3);"]:
        rc, out, err = run_sql(q)
        print(rc, parse(out) if rc == 0 else err[:80])
