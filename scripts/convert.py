import sys
import json
import os
import glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
import numpy as np



#-- 1. convert CityJSON => CityJSONSeq
# fs = glob.glob('*.json')
# for each in fs:
#     # cjseq cat -f out.json > out.jsonl
#     cmd = "cjseq cat -f {} > {}l".format(each, each)
#     print(cmd)
#     os.system(cmd)


#-- 2. sizes
fs = glob.glob('./data/*.json')
nocubes = []
scj = []
scjseq = []
for f in fs:
    # print(f)
    nocubes.append(int(f[f.find("_")+1:f.rfind(".")]))
    scj.append(os.path.getsize(f) /1024/1024)
    fl = f + "l"
    scjseq.append(os.path.getsize(fl)/1024/1024)

z = np.sort(np.array([nocubes, scj, scjseq]).transpose(), axis=0)

compr = (z[:,1] - z[:,2]) / z[:,1]
print(compr.min())
print(compr.max())
# sys.exit()
# print(z[0])
# print(z[:,0])
# print(z[:,1])


# sys.exit()
#-- 3. plot
fig, ax = plt.subplots()
ax.plot(z[:,0], compr)
# ax.plot(z[:,0], compr, marker=".")

ax.set(xlabel='Number of Buildings', ylabel='file compression')
# ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))

# ax.set_xlim(-1, 100000)
# ax.set_ylim(0.8, 1.01)
fig.savefig("synthetic_compression.pdf")
plt.show()