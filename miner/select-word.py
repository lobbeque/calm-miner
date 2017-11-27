import json


# Parlez nous de vous

# http://brandonrose.org/clustering

clusterField = "Motivations"

# open the data
with open('letters.json') as data_file:    
    data = json.load(data_file)

motiv  = []
nous   = []
ids    = []
dates  = []

for d in data: 
    if clusterField not in d or d[clusterField] == "" or d["Date d'inscription"] is None:
        continue
    if d[clusterField] == "#NAME?" or d[clusterField] == "compagnie." or d[clusterField] == "." or d[clusterField] == "Xx":
        continue 
    if len(d[clusterField]) < 30:
        continue
    if "2016" in d["Date d'inscription"] :
        dates.append(d["Date d'inscription"])
        ids.append(d["Phase"] + d["Ligne"])
        motiv.append(d["Motivations"])
        nous.append(d["Parlez nous de vous"])



for i in range(len(motiv)):

    print('-- ' + ids[i] + ' -- ' + dates[i].split('T')[0]) 
    print(motiv[i].encode('utf-8'))
    print
    print(nous[i].encode('utf-8'))
    print