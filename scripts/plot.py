import sys
import json
import os
import glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
import numpy as np
import pandas as pd


#-- 1. convert CityJSON => CityJSONSeq
# fs = glob.glob('*.json')
# for each in fs:
#     # cjseq cat -f out.json > out.jsonl
#     cmd = "cjseq cat -f {} > {}l".format(each, each)
#     print(cmd)
#     os.system(cmd)


shared = pd.read_csv("shared.csv")
# print(shared)
shared = shared.sort_values(by=['group'])
# sys.exit()


#-- 2. sizes
fs = glob.glob('./data/*.json')
groups = []
scj = []
scjseq = []
for f in fs:
    # print(f)
    groups.append(int(f[f.rfind("/")+1:f.rfind(".")]))
    scj.append(os.path.getsize(f) /1024/1024)
    fl = f + "l"
    scjseq.append(os.path.getsize(fl)/1024/1024)


df = pd.DataFrame(np.array([groups, scj, scjseq])).transpose()
df = df.sort_values(by=[0])
df["shared"] = shared['percentage']
# print(df)
# print(df.sort_values(by=[0]))
# print(df)
# sys.exit()


compr = (df[1] - df[2]) / df[1]
print(compr.min())
print(compr.max())


#-- 3. plot
fig, ax = plt.subplots()
# ax.plot(df[0], compr)
ax.plot(df['shared'], compr)
# ax.plot(z[:,0], compr, marker=".")

ax.set(xlabel='% shared vertices', ylabel='compression factor')
# ax.set(xlabel='Number of groups', ylabel='file compression')
# ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))

# ax.set_xlim(-1, 100000)
# ax.set_ylim(0.8, 1.01)
# fig.savefig("synthetic_compression.pdf")
plt.show()