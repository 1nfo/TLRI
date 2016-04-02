import os, matplotlib
matplotlib.use('TKAgg')

from matplotlib import pyplot as plt
from pandas import DataFrame
from matplotlib import animation
import numpy as np
import sys

if len(sys.argv)>1:
    default=False
    tid=sys.argv[1]
else:
    default=True
    tid = "22241"

TRAJ_DIR = "./data/trajectories/"

def readTraj(tid,threshold):
    path=TRAJ_DIR+tid
    with open(path,"rb") as f:
        data = []
        for i in f:
            tmp = i.strip().split(",")
            #range_conditions = float(tmp[3])>23.1 or float(tmp[3])<22.4
            #if range_conditions:
                #return []
            data.append([int(tmp[0]),tmp[1],float(tmp[2]),float(tmp[3])])
    df=DataFrame(data).sort_values(by=1)
    return df

test = readTraj(tid,1).iloc[1060 if default else 0:,:]
#plt.plot(test.iloc[:,2],test.iloc[:,3])
#plt.show()

fig = plt.figure()
ax = plt.axes(xlim=(114 if default else 113.6, 114.13 if default else 114.5), ylim=(22.5 if default else 22.4, 22.62 if default else 23.1))
line, = ax.plot([], [], lw=1.5)

def init():
    line.set_data([],[])
    return line,

def animate(i):
    idx=i%test.shape[0]
    x=test.iloc[:,2][0:idx+1]
    y=test.iloc[:,3][0:idx+1]
    line.set_data(x,y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=140 if default else 10000, interval=250 if default else 1, blit=True)
plt.show()
