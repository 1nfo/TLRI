# Project2

## To do:

1. Find the intersections. [openstreet]

## some usages:
### clean.py
	python clean.py

Get remove the last two columns, rewrite into a new file cleaned.txt. And also generate a directory, where each trajectories will be formed as a single file.  
>Need to set:  
>1. original dataset [TaxiData.txt](http://www-users.cs.umn.edu/~tianhe/BIGDATA/UrbanCPS/TaxiData/TaxiData) and [BusData.txt](http://www-users.cs.umn.edu/~tianhe/BIGDATA/UrbanCPS/BusData/BusData) (from http://www-users.cs.umn.edu/~zhang/data.html)   
>2. manually create a new directory Trajectories

### plot.py
	python plot.py

Plot each trajectory under the trajectories folder.
Default plot first 5. Can manually change the range.
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
