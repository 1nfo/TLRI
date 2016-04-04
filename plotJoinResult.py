from matplotlib import pyplot as plt
import pandas as pd
import os, sys

PATH = "./data/JoinResults/"
plotN = 10
LEAST = 100

Iids = os.listdir(PATH)

if len(sys.argv)>1:
    plotN = int(sys.argv[1])
if len(sys.argv)>2:
    LEAST = int(sys.argv[2])

count=0
for i in Iids:
    with open(PATH+i,"rb") as f:
        res = []
        for i in f:
            res.append(i.strip().split(","))
    df = pd.DataFrame(res[1:])
    if len(df[2])>LEAST:
        df[2], df[3] = df[2].astype(float), df[3].astype(float)
        plt.scatter(df[2],df[3])
        plt.scatter(float(res[0][1]),float(res[0][2]),color="r")
        plt.title(str(len(df[2])))
        plt.show()
        count+=1
    if count>=plotN: break
else:
    print "No satisfied!"
