# load_cityjsonseq.py

import json
from sys import argv
import sys
import psutil
import resource

fpath = argv[1]

maxrss = 0.0
no_solid = 0
no_msurface = 0
with open(fpath, "r") as fo:
    meta = json.loads(fo.readline())
    for feature_str in fo:
        feature = json.loads(feature_str)
        memory = resource.getrusage(resource.RUSAGE_SELF)
        a = memory.ru_maxrss / 1024 / 1024
        if a > maxrss:
            maxrss = a
        # process the feature with the information in 'meta', then discard
        # pass
        for coid, co in feature["CityObjects"].items():
            for geom in co.get("geometry", []):
                if geom["type"] == "Solid":
                    no_solid += 1
                elif geom["type"] == "MultiSurface":
                    no_msurface += 1

memory = resource.getrusage(resource.RUSAGE_SELF)
a = memory.ru_maxrss / 1024 / 1024
if a > maxrss:
    maxrss = a

print(maxrss)
# print(no_solid)
# print(no_msurcdface)