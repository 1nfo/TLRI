#check each trajectories plot
from matplotlib import pyplot as plt
from pandas import DataFrame
import numpy as np
import os
import time
import sys

TRAJ_DIR = "./trajectories/"
tids = os.listdir(TRAJ_DIR)

def plotT(tid):
    theta=0.00001
    path=TRAJ_DIR+tid
    dataset, dfs=[], []
    curr, last = 0, 0
    with open(path,"rb") as f:
        data = []
        for i in f:
            tmp = i.strip().split(",")
            if type(curr)!=int: last=curr.copy()
            curr = np.array(tmp[2:4],float)
            #conditions = float(tmp[3])>23.1 or float(tmp[3])<22.4 or type(last)!=int and ((curr-last)**2).sum>theta
            #if conditions: dataset.append(data)
            data.append([int(tmp[0]),tmp[1],float(tmp[2]),float(tmp[3])])
        else:
            dataset.append(data)
    for data in dataset:
        df=DataFrame(data).sort_values(by=1)
        plt.plot(np.array(df[2]),np.array(df[3]),color='b')
        dfs.append(df)
    return dfs

#change trajectories id range
#tids is a list of all trajectores
for i in range(20):
    plotT(tids[i])
    plt.title(str(i))
    plt.show()
