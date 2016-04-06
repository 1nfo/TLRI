from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os, random, sys

JoinResPath = "./data/JoinResults/"
Ilist = os.listdir(JoinResPath)
Id,LEAST=None,0
if len(sys.argv)>1:
    Id = int(sys.argv[1])
if len(sys.argv)>2:
    LEAST = int(sys.argv[2])

def readJR(Id=None,LEAST = 100):
    #least: threshold for number of trajectory points
    Iid = (str(Id) if type(Id)==int else Id) if Id else random.choice(Ilist)
    with open(JoinResPath+Iid,"rb") as f:
        res = []
        for i in f:
            res.append(i.strip().split(","))
    df = pd.DataFrame(res[1:])
    if not Id and not len(df)>LEAST:
        return readJR(None,LEAST)
    df[2], df[3] = df[2].astype(float), df[3].astype(float)
    return (int(res[0][0]),float(res[0][1]),float(res[0][2])),df

def plotJR(c,df):
    plt.scatter(df[2],df[3],color="b",s=2,alpha=.3)
    plt.scatter(float(c[1]),float(c[2]),color="r",s=30)
    xl,xu,yl,yu=df[2].min(),df[2].max(),df[3].min(),df[3].max()
    xrng,yrng = xu-xl or 0.001,yu-yl or 0.001
    plt.xlim([xl-.1*xrng,xu+.1*xrng])
    plt.ylim([yl-.1*yrng,yu+.1*yrng])
    plt.title("Intersection:%d, # of points:%d"%(c[0],len(df)))

plotJR(*readJR(Id,LEAST))
plt.show()
