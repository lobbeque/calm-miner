import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
import json
import mpld3
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn import feature_extraction
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.manifold import MDS
from sklearn.metrics import pairwise_distances_argmin_min
from pprint import pprint

# Parlez nous de vous

# http://brandonrose.org/clustering

clusterField = "Parlez nous de vous"

# open the data
with open('letters.json') as data_file:    
    data = json.load(data_file)

docs  = []
ids   = []
dates = []

for d in data: 
    if clusterField not in d or d[clusterField] == "" or d["Date d'inscription"] is None:
        continue
    if d[clusterField] == "#NAME?" or d[clusterField] == "compagnie." or d[clusterField] == "." or d[clusterField] == "Xx":
        continue 
    if len(d[clusterField]) < 30:
        continue
    dates.append(d["Date d'inscription"].split("T")[0].split("-")[0] + "-" + d["Date d'inscription"].split("T")[0].split("-")[1])
    ids.append(d["Phase"] + d["Ligne"])
    docs.append(d[clusterField])

#clean the docs
frenchStopWords = set(["au","aux","avec","parce","plus","ce","dont","ces","toute","tous","toutes","dans","de","des","du","elle","en","et","eux","il","je","la","le","leur","lui","ma","mais","me","meme","mes","moi","mon","ne","nos","notre","nous","on","ou","par","pas","pour","qu","que","qui","sa","se","ses","son","sur","ta","te","tes","toi","ton","tu","un","une","vos","votre","vous","c","d","j","l","a","m","n","s","t","y","ete","etee","etees","etes","etant","suis","es","est","sommes","etes","sont","serai","seras","sera","serons","serez","seront","serais","serait","serions","seriez","seraient","etais","etait","etions","etiez","etaient","fus","fut","femes","futes","furent","sois","soit","soyons","soyez","soient","fusse","fusses","fut","fussions","fussiez","fussent","ayant","eu","eue","eues","eus","ai","as","avons","avez","ont","aurai","auras","aura","aurons","aurez","auront","aurais","aurait","aurions","auriez","auraient","avais","avait","avions","aviez","avaient","eut","eumes","eutes","eurent","aie","aies","ait","ayons","ayez","aient","eusse","eusses","eut","eussions","eussiez","eussent","ceci","cela","cela","cet","cette","ici","ils","les","leurs","quel","quels","quelle","quelles","sans","soi"])

stopwords_set = set(nltk.corpus.stopwords.words('french')) | frenchStopWords

stemmer = SnowballStemmer("french")

def clean(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    cpt = 0
    tmp = []
    for token in tokens:
    	if len(token.split("'")) > 1 :
    		for tk in token.split("'"):
    			tmp.append(tk)
    	else :
    		tmp.append(token)

    tokens  = [x for x in tmp if x not in stopwords_set]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token) and len(token) > 1:
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

totalvocab_stemmed = []
totalvocab_tokenized = []

for d in docs:
    stemmed = tokenize_and_stem(d)
    totalvocab_stemmed.extend(stemmed)
    allwords_tokenized = tokenize_only(d)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
# print 'there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame'    

# print vocab_frame.head()
# print
# print
# print
# print

tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000, min_df=0.01,use_idf=True, strip_accents='unicode', stop_words=stopwords_set, tokenizer=clean, ngram_range=(1,3))
tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
# print(tfidf_matrix.shape)

terms = tfidf_vectorizer.get_feature_names()
# print(terms)

dist = 1 - cosine_similarity(tfidf_matrix)

num_clusters = 5
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
clusters = km.labels_.tolist()

# joblib.dump(km,  'doc_cluster.pkl')
# km = joblib.load('doc_cluster.pkl')
# clusters = km.labels_.tolist()

letters = { 'ids': ids, 'dates': dates, 'docs': docs, 'cluster': clusters}

frame = pd.DataFrame(letters, index = [clusters] , columns = ['ids', 'dates', 'cluster'])

print
print("======== Clusters ========")
print
print(frame['cluster'].value_counts())
print
print

# print("Top terms per cluster:")
# print
#sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1] 

for i in range(num_clusters):

    print
    print("----- Cluster " + str(i) + " -----")
    print

    clusterIdx = []
    cpt = 0
    for cluster in letters["cluster"] :
        if cluster == i :
            clusterIdx.append(cpt)
        cpt = cpt + 1
    
    nbWords = 10

    print
    print("Relevant " + str(nbWords) + " words :")
    print
    print("-----")
    for ind in order_centroids[i, :nbWords]:
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0])
    print("-----")
    print

    nbDocs = 10 
    
    matrix_by_cluster = []
    ids_by_cluster = []
    for cpt in range(len(letters['cluster'])):
        if letters["cluster"][cpt] == i:
            matrix_by_cluster.append(tfidf_matrix[cpt])
            ids_by_cluster.append(ids[cpt])

    print
    print("Top " + str(nbDocs) + " closest docs :")
    print
    d = km.transform(tfidf_matrix)[:, i]
    
    distCluster  = [d[idx]    for idx in clusterIdx]
    idsCluster   = [ids[idx]  for idx in clusterIdx]
    docsCluster  = [docs[idx] for idx in clusterIdx]

    idsIdx = np.argsort(distCluster)[::][:nbDocs]
    for idx in idsIdx:
        print('-- ' + idsCluster[idx])
        print(docsCluster[idx])
        print
    print
    print