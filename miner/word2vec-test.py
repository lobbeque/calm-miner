import sys
import json
import nltk
import re
import gensim

# nltk.download('stopwords')
# https://medium.com/towards-data-science/a-gentle-introduction-to-doc2vec-db3e8c0cce5e
# https://medium.com/@mishra.thedeepak/doc2vec-in-a-simple-way-fa80bfe81104
# https://radimrehurek.com/gensim/models/doc2vec.html

from pprint import pprint
from nltk import RegexpTokenizer
from nltk.corpus import stopwords

with open('letters.json') as data_file:    
    data = json.load(data_file)

tokenizer = RegexpTokenizer(' ')
stopword_set = set(stopwords.words('french'))

# pprint(stopword_set)

def nlp_clean(str):
	new_str = str.lower()
	words = re.split('\s+', new_str)
	words = [x for x in words if x not in stopword_set]
	return words

docs = []
labels = {}

for d in data: 
	# pprint(d)
	if "Motivations" not in d or d["Motivations"] == "" or d["Date d'inscription"] is None:
		continue
	tag = d["Date d'inscription"].split("T")[0].split("-")[0] + "-" + d["Date d'inscription"].split("T")[0].split("-")[1]
	txt = nlp_clean(d["Motivations"])
	labels[d["Phase"] + d["Ligne"]] = tag
	# docs.append(set(txt))
	# labels.append([d["Phase"] + d["Ligne"],tag])
	docs.append(gensim.models.doc2vec.TaggedDocument(txt,[d["Phase"] + d["Ligne"],tag]))

model = gensim.models.Doc2Vec(size=2, min_count=0, alpha=0.025, min_alpha=0.025)
model.build_vocab(docs)

for epoch in range(100):
	print 'iteration ' +str(epoch+1)
	model.train(docs,total_examples=model.corpus_count,epochs=model.iter)
	model.alpha -= 0.002
	model.min_alpha = model.alpha

docvec = model.docvecs[1]
print docvec
docvec = model.docvecs[0]
print docvec

print model.docvecs.index_to_doctag(9)

similar_doc = model.docvecs.most_similar(14) 
print similar_doc

model.save("calmModel")

path = open("coordoWord.csv", "w") 
path.write("x;y;id;label\n")
cpt = 0
for d in model.docvecs:
	x  = str(d[0])
	y  = str(d[1])
	id = model.docvecs.index_to_doctag(cpt) 
	if id in labels :
		label = labels[id]
	else :
		cpt = cpt + 1
		continue
	cpt = cpt + 1 
	print(label)
	path.write(x + ";" + y + ";" + id + ";" + label + "\n")