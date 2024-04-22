
import json
import sys
from pathlib import Path
import sys
import csv


inpath1 = Path("/Users/hugo/data/cityjson/3dcities/v2.0/VM05_2009.city.json").resolve()
# inpath1 = Path("/Users/hugo/temp/r/Rotterdam_wo_tex.json").resolve()
with inpath1.open("r") as f:
    j = json.load(f)
v_json = len(j["vertices"])

inpath2 = Path("/Users/hugo/data/cityjson/3dcities/v2.0/VM05_2009.city.jsonl").resolve()
# inpath2 = Path("/Users/hugo/temp/r/Rotterdam_wo_tex.jsonl").resolve()
f = open(inpath2)
v_jsonl = 0
for (i, line) in enumerate(f.readlines()):
    j2 = json.loads(line)
    v_jsonl += len(j2["vertices"]) 
            

# print(v_json)
print(v_jsonl / v_json)
print(v_json / v_jsonl)



