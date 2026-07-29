#!/usr/bin/env python3
"""Build a self-contained site/index.html.

Reads build/index.template.html and inlines site/data.js and site/app.js so the
page works even when opened directly from disk (file://), with no dependency on
loading separate .js files. Audio still loads from the relative audio/ folder.

Run:  python3 build/inline.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tpl = open(os.path.join(ROOT, "build", "index.template.html"), encoding="utf-8").read()

SCRIPTS = ["data.js", "data2.js", "data3.js", "data4.js", "data5.js", "data6.js", "data7.js", "data10.js", "app.js"]
tags = "\n".join('<script src="%s"></script>' % s for s in SCRIPTS)
inlined = "\n".join(
    "<script>\n" + open(os.path.join(ROOT, "site", s), encoding="utf-8").read() + "\n</script>"
    for s in SCRIPTS
)

out = tpl.replace(tags, inlined)

if "<script src=" in out.split("</body>")[0].split("<audio")[-1]:
    raise SystemExit("ERROR: script tags were not replaced — check template markers.")

with open(os.path.join(ROOT, "site", "index.html"), "w", encoding="utf-8") as f:
    f.write(out)
print("Wrote self-contained site/index.html")
