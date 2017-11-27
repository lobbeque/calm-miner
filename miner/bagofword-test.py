import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import os 

from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pprint import pprint
from nltk.corpus import stopwords
from sklearn.manifold import MDS

with open('letters.json') as data_file:    
    data = json.load(data_file)

vectorizer = CountVectorizer(strip_accents='unicode', stop_words=set(stopwords.words('french')))

docs = []
ids  = []
tags = []

for d in data: 
	
	if "Motivations" not in d or d["Motivations"] == "" or d["Date d'inscription"] is None:
		continue
	# pprint(d)
	tags.append(d["Date d'inscription"].split("T")[0].split("-")[0] + "-" + d["Date d'inscription"].split("T")[0].split("-")[1])
	ids.append(d["Phase"] + d["Ligne"])
	id = d["Phase"] + d["Ligne"]
	if id == "B312" :
		print(d["Motivations"])
	# docs.append(d["Motivations"])

# print("data")

# vect  = vectorizer.fit_transform(docs)
# vocab = vectorizer.get_feature_names()

# path = open("motsAcceuil.txt", "w") 

# for w in vocab:
# 	path.write(w + "\n")

# print(len(vocab))
# un vocab de 2900 mots

# print("vect")

# dist = 1 - cosine_similarity(vect)
# np.round(dist, 2)

# print("dist")

# mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
# pos = mds.fit_transform(dist)

# print("pos")

# xs, ys = pos[:, 0], pos[:, 1]


# path = open("coordoBack.csv", "w") 
# path.write("x;y;id;label\n")

# cpt = 0
# for x, y in zip(xs, ys):
# 	path.write(str(x) + ";" + str(y) + ";" + ids[cpt] + ";" + tags[cpt] + "\n")
# 	# color = 'orange' if "Austen" in name else 'skyblue'
# 	plt.scatter(x, y)
# 	plt.text(x, y, ids[cpt])
# 	cpt = cpt + 1

# plt.show()
# print(DataFrame(vect.A, columns=vectorizer.get_feature_names()).to_string())