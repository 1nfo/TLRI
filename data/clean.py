from os.path import exists
from pandas import DataFrame

endT=36950
endB=65294

##Not finished, not sure need to split
__NOT_SPLIT__=True

taxiPath = "TaxiData.txt"
busPath = "BusData.txt"
outTaxi = ("" if __NOT_SPLIT__ else Split)+"TaxiCleaned.txt"
outBus = ("" if __NOT_SPLIT__ else Split)+"BusCleaned.txt"

def f(path,out,end,isTaxi):
    with open(path,"rb") as R:
        if not exists(out):
            jump1, Wlist = False, []
        else: jump1=True
        tid , last = None, None
        for line in R:
            res = line.strip().split(",")
            if isTaxi: towritedown=res[0:4]
            else: towritedown=res[0:2]+res[3:5]
            tid = res[0]
            if last!=tid:
                ##jump fisrt iter, when last is none tid is not.
                if last and not jump2:
                    DataFrame(flist).sort(by=1).to_csv("Trajectories/"+last,header=False,index=False)
                if not exists("Trajectories/"+tid):
                    jump2, flist = False, []
                else: jump2=True
                last=tid
                print tid,"/",end
            if not jump2: flist.append(towritedown)
            if not jump1: Wlist.append(towritedown)
        if not jump2:
            DataFrame(flist).sort(by=1).to_csv("Trajectories/"+last,header=False,index=False)
        if not jump1:
            DataFrame(Wlist).sort(by=1).to_csv(out,header=False,index=False)

f(taxiPath,outTaxi,endT,True)
f(busPath,outBus,endB,False)
print "Done"
