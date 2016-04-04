# Project2

## Dir Structure

__Root__  
> ...some scripts  
>__data__  
> ... raw data (busdata.txt, taxidata.txt) and clean scripts    
>>__Trajectories__  (ignored by repo)  
>> ... Each file is a trajectory  
>>__JoinResults__  (ignored)  
>> ... Each file is an intersection join result. 
>
>__results__  
> ... some results  
>__SpatialJoin__  
> ... MapReduce join

## some usages:
### clean.py
	python clean.py

Get remove the last two columns, rewrite into a new file cleaned.txt. And also generate a directory, where each trajectories will be formed as a single file.  
>Need to set:  
>1. original dataset [TaxiData.txt](http://www-users.cs.umn.edu/~tianhe/BIGDATA/UrbanCPS/TaxiData/TaxiData) and [BusData.txt](http://www-users.cs.umn.edu/~tianhe/BIGDATA/UrbanCPS/BusData/BusData) (from http://www-users.cs.umn.edu/~zhang/data.html)   
>2. manually create a new directory Trajectories

### plot.py
	python plot.py [trajectory start-ID [plot number [split-flag] ] ]

Plot each trajectory under the trajectories folder.
Default plot first 5 (no args given). Can manually set start trajectories id and continue to plot a number of trajectories, if number is not given, default value is 5. The split-flag will yield the results with split plot. It is necessary When to ***plot bus trajectories*** since there are many abnormal points.
>Need to set:  
>The trajectories data under "Trajectories" folder.  
>i.e. run clean.py first

### WhatHappened.py
	python WhatHappened.py [taxi-ID]
	
Plot Animation of trajectory. taxi-id is optional. By default, it will plot an abnormal example.  
>Need to set:  
>The trajectories data under "Trajectories" folder.  
>i.e. run clean.py first

### results/
some ipynb results will be saved in this folder. 

##  Spatial Join
usage:  

	cd SpatialJoin/
	python SpatialJoin.py

make sure has all data under "data/Trajectoies/" and intersection data from **extract_itrsctn.py**

Plot Join:

	python plotJoinResult.py [ number of plot [threshold]]
