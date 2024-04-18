# load_cityjson.py

import json
import sys
import resource

fpath = sys.argv[1]

no_solid = 0
no_msurface = 0
with open(fpath, "r") as fo:
    cm = json.load(fo)
    for coid, co in cm["CityObjects"].items():
        # process the CityObject with information from cm['transform']
        # pass
        for geom in co.get("geometry", []):
            if geom["type"] == "Solid":
                no_solid += 1
            elif geom["type"] == "MultiSurface":
                no_msurface += 1

memory = resource.getrusage(resource.RUSAGE_SELF)
print(memory.ru_maxrss / 1024 / 1024)

# print(no_solid)
# print(no_msurface)