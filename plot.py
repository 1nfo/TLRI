#check each trajectories plot
from matplotlib import pyplot as plt
from pandas import DataFrame
import numpy as np
import os
import time
import sys

TRAJ_DIR = "./trajectories/"
tids = os.listdir(TRAJ_DIR)

def plotTraj(df):
    plt.plot(np.array(df[2]),np.array(df[3]),color='b')

def spliTraj(df,threshold):
    curr, last = None, None
    split=[0]
    for i in xrange(df.shape[0]):
        if type(curr)!=type(None):
            last=curr
        curr = df.iloc[i,2:4]
        if type(last)!=type(None):
            conditions = curr.iloc[1]>23.1 or curr.iloc[1]<22.4 or \
             curr.iloc[0]<113.6 or curr.iloc[0]>114.5
            if ((last-curr)**2).sum()>threshold or conditions:
                split.append(i)
    split.append(i+1)
    ret = []
    for i in xrange(1,len(split)):
        splited=df.iloc[split[i-1]:split[i],:]
        if splited.shape[0]>5:
            plotTraj(splited)
            ret.append(splited)
    return ret

def plotT(tid):
    path=TRAJ_DIR+tid
    curr, last = 0, 0
    with open(path,"rb") as f:
        data = []
        for i in f:
            tmp = i.strip().split(",")
            if type(curr)!=int: last=curr.copy()
            curr = np.array(tmp[2:4],float)

            data.append([int(tmp[0]),tmp[1],float(tmp[2]),float(tmp[3])])
    df=DataFrame(data).sort_values(by=1)
    if flag:
        dfs =spliTraj(df,0.001)
    else:
        plotTraj(df)

#change trajectories id range
#tids is a list of all trajectores
if len(sys.argv)>3:
    flag=sys.argv[3]
else: flag=False
if len(sys.argv)>2:
    l=int(sys.argv[2])
else: l=5
if len(sys.argv)>1:
    start = int(sys.argv[1])
    for i in xrange(l):
        plotT(str(start+i))
        plt.title(str(start+i))
        plt.show()
else:
    for i in range(5):
        plotT(tids[i])
        plt.title(str(i))
        plt.show()
