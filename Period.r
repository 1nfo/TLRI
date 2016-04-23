library(forecast)
find.freq <- function(x)
{
  n <- length(x)
  spec <- spec.ar(c(na.contiguous(x)),plot=FALSE)
  if(max(spec$spec)>10) # Arbitrary threshold chosen by trial and error.
  {
    period <- round(1/spec$freq[which.max(spec$spec)])
    if(period==Inf) # Find next local maximum
    {
      j <- which(diff(spec$spec)>0)
      if(length(j)>0)
      {
        nextmax <- j[1] + which.max(spec$spec[j[1]:500])
        if(nextmax <= length(spec$freq))
          period <- round(1/spec$freq[nextmax])
        else
          period <- 1
      }
      else
        period <- 1
    }
  }
  else
    period <- 1
 
  return(period)
}

args <- commandArgs(trailingOnly = TRUE)
print(args)
data<-read.csv(args[1],header = T)
print("Reading Done")
result <- as.data.frame(matrix(NA,nrow=4,ncol=29))
for (k in 2:5){
    ts1<-ts(data[,k])
    print (k)
    l<-rep(NA,29)
    for(i in 2:30){
        s<-ma(ts1,order = i, centre = TRUE)
        s<-s[i * 0:(86400 / i)]
        l[i-1]<-find.freq(100*s) * i
    }
    result[k-1,] = l
}
fname = strsplit(args[1], '/')[[1]]
write.csv(result,paste0('./periods/result_',fname[length(fname)],'.csv'))

