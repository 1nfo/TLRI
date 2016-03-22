from os.path import exists

endT=36950
endB=65294

taxiPath = "TaxiData.txt"
busPath = "BusData.txt"
outTaxi = "TaxiCleaned.txt"
outBus = "BusCleaned.txt"

def f(path,out,end,isTaxi):
    with open(path,"rb") as R:
        if not exists(out):
            W, jump1 = open(out,"wb"), False
        else: jump1=True
        tid , last = None, None
        for line in R:
            res = line.strip().split(",")
            if isTaxi: towritedown=res[0]+","+res[1]+","+res[2]+","+res[3]
            else: towritedown=res[0]+","+res[1]+","+res[3]+","+res[4]
            tid = res[0]
            if last!=tid:
                if last and not jump2: f.close()
                if not exists("Trajectories/"+tid):
                    f, jump2 = open("Trajectories/"+tid,"wb"), False
                else: jump2=True
                last=tid
                print tid,"/",end
            if not jump2: f.write(towritedown+'\n')
            if not jump1: W.write(towritedown+'\n')
        if not jump2: f.close()
        if not jump1: W.close()

f(taxiPath,outTaxi,endT,True)
f(busPath,outBus,endB,False)
print "Done"
