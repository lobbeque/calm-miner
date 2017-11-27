import csv
import matplotlib.pyplot as plt

from pprint import pprint

xs   = [] 
ys   = []
ids  = []
tags = []

with open("coordoBack.csv", "rb") as f:
    reader = csv.reader(f, delimiter=";")
    for i, line in enumerate(reader):
    	if i == 0 :
    		continue
    	xs.append(float(line[0]))
    	ys.append(float(line[1]))
    	tmp = line[2][0]  + str(float(line[2][1:]) + 1)
    	ids.append(tmp)
    	tags.append(line[3])


colorRef = {'2015-09' :"#0F4AEB",
'2015-10' :"#1A47DD",
'2015-11' :"#2644D0",
'2015-12' :"#3241C3", 
'2016-01' :"#3E3FB6",
'2016-02' :"#493CA9",
'2016-03' :"#55399C",
'2016-04' :"#61378F",
'2016-05' :"#6D3482",
'2016-06' :"#783175",
'2016-07' :"#842F68",
'2016-08' :"#902C5B",
'2016-09' :"#9C294E",
'2016-10' :"#A72741",
'2016-11' :"#B32434", 
'2016-12' :"#BF2127", 
'2017-02' :"#CB1F1A"}

for x, y, id, tag in zip(xs, ys, ids, tags):
	color = colorRef[tag]
	plt.scatter(x, y, c=color, s=5)
	plt.text(x, y, id)

plt.show()
