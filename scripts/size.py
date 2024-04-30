import sys
import json
import os
import glob


fs = glob.glob('./data/*.jsonl')

# print(fs)
# sys.exit()

for each in fs:
    # f = open('/Users/hugo/data/cityjson/3dcities/v2.0/3-20-DELFSHAVEN.city.jsonl')
    f = open(each)
    
    totalkb = 0.0
    maxchar = 0
    maxv = 0
    li = 0
    for (i, line) in enumerate(f.readlines()):
        kb = round(len(line) / 1024.0)
        totalkb += kb
        if kb > maxchar:
            maxchar = kb
            li = i
        j = json.loads(line)
        if len(j["vertices"]) > maxv:
            maxv = len(j["vertices"])

    # print("max:", maxchar, li)
    # print("max:", maxchar)
    # print("avg: {:.1f}".format(totalkb / (i+1.0)))
    # f.seek(0)
    # j2 = json.dumps(j, separators=(',', ':'))
    # fo = open('out.jsonl', 'w')
    # fo.write(j2)
    # thesize = round(os.path.getsize("out.jsonl") / 1024.0)
    # print(each, thesize)
    print(each, maxchar, "{:.1f}".format(totalkb / (i+1.0)), maxv)

fs = glob.glob('../data/*.json')
for each in fs:
    f = open(each)
    j = json.loads(f.read())
    print(each, len(j["vertices"]))

