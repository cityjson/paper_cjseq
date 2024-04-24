
import json
import sys
from pathlib import Path
import sys
import csv
import glob

fs = glob.glob('/Users/hugo/data/cityjson/CityJSONSeq-demo-files/*.json')

for each in fs:
    #-- json
    with Path(each).resolve().open("r") as f:
        j = json.load(f)
    v_json = len(j["vertices"])

    #-- jsonl
    eachl = each + "l"
    f = open(eachl)
    v_jsonl = 0
    for (i, line) in enumerate(f.readlines()):
        j2 = json.loads(line)
        v_jsonl += len(j2["vertices"]) 

    print(each, v_jsonl / v_json)



