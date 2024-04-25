import json
import sys
import random


def gen_onecube(offset):
    g = {"type": "Solid", "lod": "1.1", "boundaries": []}
    i = offset
    b = []
    b.append([ [i+0, i+3, i+2, i+1] ])
    b.append([ [i+4, i+5, i+6, i+7] ])
    b.append([ [i+0, i+1, i+5, i+4] ])
    b.append([ [i+1, i+2, i+6, i+5] ])
    b.append([ [i+2, i+3, i+7, i+6] ])
    b.append([ [i+0, i+4, i+7, i+3] ])
    g["boundaries"].append(b)

    return g

def gen_vertices(total):
    vs = []
    for i in range(total):
        vs.append([random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000)])
    return vs


def main():
    number_of_co = 5000000
    j = {"type": "CityJSON", "version": "2.0", "CityObjects": {}, "transform": {}}
    j["transform"]["scale"] = [0.01, 0.01, 0.01]
    j["transform"]["translate"] = [85000.1, 445006.2, 0.1]
    offset = 0
    for i in range(number_of_co):
        cgeom = gen_onecube(offset)
        offset += 8
        coj = {"type": "Building", "geometry": []}
        coj["geometry"].append(cgeom)
        coid = "id_" + str(i)
        j["CityObjects"][coid] = coj
    j["vertices"] = gen_vertices(number_of_co * 8) 

    json_str = json.dumps(j, separators=(',',':'))
    # json_str = json.dumps(j, indent=2)
    fname = "gen_" + str(int(number_of_co / 1000)) + "k.json"
    with open(fname, "w") as foo:
        foo.write(json_str)


if __name__ == '__main__':
    main()
