end=36950

with open("TaxiData.txt","rb") as R:
    with open("cleaned.txt","wb") as W:
        tid , last = None, None
        for line in R:
            res = line.strip().split(",")
            towritedown=res[0]+","+res[1]+","+res[2]+","+res[3]
            tid = res[0]
            if last!=tid:
                if last: f.close()
                f = open("Trajectories/"+tid,"wb")
                last=tid
                print tid,"/",end
            f.write(towritedown+'\n')
            W.write(towritedown+'\n')
        f.close()

print "Done"
