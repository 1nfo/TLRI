import numpy as np
import pandas as pd
import pickle
INTERSECTION_PATH = itrsctn
with open(INTERSECTION_PATH,"rb") as f:
    res=[]
    for i in f:
        s=i.split("'")
        if len(s)==3:
            res.append(float(s[1]))

tmp=np.array(res)
df = pd.DataFrame(tmp.reshape(len(tmp)/2,2))

df.to_csv("intersections",header=False)
