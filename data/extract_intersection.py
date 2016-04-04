import pickle, sys
import pandas as pd

INTERSECTION_PATH = sys.argv[1]
with open(INTERSECTION_PATH,"rb") as f:
    res = pickle.load(f)
df = pd.DataFrame(res)
df.ix[:,[1,0]].to_csv("intersections",header=False)
