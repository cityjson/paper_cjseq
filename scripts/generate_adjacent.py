import json
import sys
import random
import uuid
import os
import glob
import math

def main():
    total_buildings = 100
    groups = range(0, math.floor(math.log(total_buildings, 2))+1)
    for group in groups:
        g = round(math.pow(2, group))
        co = round(total_buildings / g)
        write_cjseq(g, co)
    write_cjseq(1, total_buildings)
    #-- convert to cityjson
    fs = glob.glob('./data_adjacent/*.jsonl')
    for f in fs:
        s = "cjseq collect -f {} > {}".format(f, f[:-1])
        # print(s)
        os.system(s)

def write_cjseq(no_groups, no_co):
    fname = "./data_adjacent/" + str(no_co) + ".jsonl"
    fo = open(fname, "w")
    #-- write first line
    j = {"type": "CityJSON", "version": "2.0", "CityObjects": {}, "transform": {}, "vertices": []}
    j["transform"]["scale"] = [1.0, 1.0, 1.0]
    j["transform"]["translate"] = [0.0, 0.0, 0.0]
    json_str = json.dumps(j, separators=(',',':'))
    fo.write(json_str + "\n")
    #-- write CityJSONFeature lines
    for group in range(no_groups):
        new_cityjson_group(no_co, fo)


def gen_onecube():
    g = {"type": "Solid", "lod": "1.1", "boundaries": []}
    b = []
    b.append([ [0, 3, 2, 1] ])
    b.append([ [4, 5, 6, 7] ])
    b.append([ [0, 1, 5, 4] ])
    b.append([ [1, 2, 6, 5] ])
    b.append([ [2, 3, 7, 6] ])
    b.append([ [0, 4, 7, 3] ])
    g["boundaries"].append(b)
    return g


def gen_vertices(offsets):
    vs = []
    vs.append([offsets[0]  , offsets[1]  , offsets[2]])
    vs.append([offsets[0]+1, offsets[1]  , offsets[2]])
    vs.append([offsets[0]+1, offsets[1]+1, offsets[2]])
    vs.append([offsets[0]  , offsets[1]+1, offsets[2]])
    vs.append([offsets[0]  , offsets[1]  , offsets[2]+1])
    vs.append([offsets[0]+1, offsets[1]  , offsets[2]+1])
    vs.append([offsets[0]+1, offsets[1]+1, offsets[2]+1])
    vs.append([offsets[0]  , offsets[1]+1, offsets[2]+1])
    return vs


    

def new_cityjson_group(number_of_co, fo):        
    offsets = [random.randint(0,10000), random.randint(0,10000), random.randint(0,10000)]
    for i in range(number_of_co):
        j = {"type": "CityJSONFeature", "CityObjects": {}, "vertices": []}
        cgeom = gen_onecube()
        coj = {"type": "Building", "geometry": []}
        coj["geometry"].append(cgeom)
        coid = str(uuid.uuid4())
        j["id"] = coid    
        j["CityObjects"][coid] = coj
        j["vertices"] = gen_vertices(offsets) 
        offsets[2] += 1
        json_str = json.dumps(j, separators=(',',':'))
        fo.write(json_str + "\n")


if __name__ == '__main__':
    main()
