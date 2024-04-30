
import json
import sys
from pathlib import Path
import sys
import csv
import glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib

fs = glob.glob('./data/*.json')

fout = open("shared.csv", 'w')
fout.write("group,percentage")

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

    print(each, (v_jsonl - v_json) / v_json)
    fout.write("{},{}\n".format(each, (v_jsonl - v_json) / v_json))




