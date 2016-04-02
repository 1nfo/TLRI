import math, time
import MapReduce
from scipy.spatial.distance import euclidean
from collections import defaultdict

BLOCKSIZE=.001
BLOCKPREC=int(-math.log10(BLOCKSIZE))
BLOCKEDGE=.0005
ITSCTNRNG=.0005

class Timer:
    def __enter__(self):
        self.t0 = time.time()
        return self
    def __exit__(self, *args):
        print "Elapsed Time: %f" % (time.time()-self.t0)

class Mapper(MapReduce.Mapper):
    count=0
    def map(self,key,value,context):
        s=value.split(",")
        if len(s)==3:
            tmp = map(lambda x:float(x),s[1:])
            outkeys=[tuple(map(lambda x:round(x,BLOCKPREC),[tmp[0]+ii,tmp[1]+jj]))
                for ii in [-BLOCKEDGE,0,BLOCKEDGE]
                for jj in [-BLOCKEDGE,0,BLOCKEDGE]]
            for outkey in set(outkeys):
                context.setdefault(tuple(outkey),defaultdict(list))
                context[tuple(outkey)]["I"].append(value)
        elif len(s)==4:
            outkey = map(lambda x:round(float(x),BLOCKPREC),s[2:])
            context.setdefault(tuple(outkey),defaultdict(list))
            context[tuple(outkey)]["T"].append(value)

class Reducer(MapReduce.Reducer):
    def reduce(self,key,values,context):
        intersections=values["I"]
        points=values["T"]
        for p in points:
            nearest=[]
            for i in intersections:
                if dist(i,p)<ITSCTNRNG:
                    context[i].append(p)

def dist(i,p):
    return euclidean(map(float,i.split(",")[1:]),map(float,p.split(",")[2:]))

mr=MapReduce.MapReduce(Mapper,Reducer)
mr.set_input_traj("../data/Trajectories/")
mr.set_input_itsc("../data/intersections")
mr.set_output("../data/JoinResults/")
with Timer():
    mr.execute(1)
