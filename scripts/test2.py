import os
import glob
import math
import sys

# total_buildings = 1000000
# groups = range(0, math.floor(math.log(total_buildings, 2))+1)

# for group in groups:
#     g = round(math.pow(2, group))
#     co = round(total_buildings / g)
#     s = "python generate_adjacent.py {} {} > ./data/{}.jsonl".format(g, co, g)
#     # print(s)
#     os.system(s)
# s = "python generate_adjacent.py {} {} > ./data/{}.jsonl".format(total_buildings, 1, total_buildings)
# # print(s)
# os.system(s)





fs = glob.glob('./data/*.jsonl')
for f in fs:
    s = "cjseq collect -f {} > {}".format(f, f[:-1])
    # print(s)
    os.system(s)