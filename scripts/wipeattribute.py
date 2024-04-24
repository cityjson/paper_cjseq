# load_cityjson.py

import json
import sys
import resource

fpath = sys.argv[1]

with open(fpath, "r") as fo:
    cm = json.load(fo)
    for coid, co in cm["CityObjects"].items():
        del cm["CityObjects"][coid]["attributes"]

json_str = json.dumps(cm, separators=(',',':'))
with open("out.json", "w") as foo:
    foo.write(json_str)