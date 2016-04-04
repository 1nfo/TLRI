import math, time, sys
import MapReduce
from scipy.spatial.distance import euclidean
from collections import defaultdict

BLOCKSIZE =.002#have to be 0.5,0.25,0.2,0.1,0.05,0.02,...reciprocal is int
BLOCKEDGE =.002
ITSCTNRNG =.002
limit = None if len(sys.argv)<2 else int(sys.argv[1])

prec_func = lambda x:round(float(x)/BLOCKSIZE)*BLOCKSIZE

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
            outkeys=[tuple(map(prec_func,[tmp[0]+ii,tmp[1]+jj]))
                for ii in [-BLOCKEDGE,0,BLOCKEDGE]
                for jj in [-BLOCKEDGE,0,BLOCKEDGE]]
            for outkey in set(outkeys):
                context.setdefault(tuple(outkey),defaultdict(list))
                context[tuple(outkey)]["I"].append(value)
        elif len(s)==4:
            outkey = map(prec_func,s[2:])
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
mr.set_param("traj_limit",limit)# None for all trajectories
with Timer():
    mr.execute(1)
