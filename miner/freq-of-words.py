import json
import nltk
import re

from   nltk.stem.snowball import SnowballStemmer

field = "Motivations"

# open the data
with open('letters.json') as data_file:    
    data = json.load(data_file)

month = ['2015-09','2015-10','2015-11','2015-12','2016-01','2016-02','2016-03','2016-04','2016-05','2016-06','2016-07','2016-08','2016-09','2016-10','2016-11','2016-12','2017-02']
count_by_month = []
count_by_days  = []

french_stopwords = set(["au","aux","avec","parce","plus","ce","dont","ces","toute","tous","toutes","dans","de","des","du","elle","en","et","eux","il","je","la","le","leur","lui","ma","mais","me","meme","mes","moi","mon","ne","nos","notre","nous","on","ou","par","pas","pour","qu","que","qui","sa","se","ses","son","sur","ta","te","tes","toi","ton","tu","un","une","vos","votre","vous","c","d","j","l","a","m","n","s","t","y","ete","etee","etees","etes","etant","suis","es","est","sommes","etes","sont","serai","seras","sera","serons","serez","seront","serais","serait","serions","seriez","seraient","etais","etait","etions","etiez","etaient","fus","fut","femes","futes","furent","sois","soit","soyons","soyez","soient","fusse","fusses","fut","fussions","fussiez","fussent","ayant","eu","eue","eues","eus","ai","as","avons","avez","ont","aurai","auras","aura","aurons","aurez","auront","aurais","aurait","aurions","auriez","auraient","avais","avait","avions","aviez","avaient","eut","eumes","eutes","eurent","aie","aies","ait","ayons","ayez","aient","eusse","eusses","eut","eussions","eussiez","eussent","ceci","cela","cela","cet","cette","ici","ils","les","leurs","quel","quels","quelle","quelles","sans","soi"])
stopwords_set = set(nltk.corpus.stopwords.words('french')) | french_stopwords
stemmer = SnowballStemmer("french")

docs  = []
ids   = []
dates = []

def clean_txt(txt):
    tokens = [word.lower() for sent in nltk.sent_tokenize(txt) for word in nltk.word_tokenize(sent)]
    tokens = [x for x in tokens if x not in stopwords_set]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

for d in data: 
    if field not in d or d[field] == "" or d["Date d'inscription"] is None or "2015-09" not in d["Date d'inscription"]:
        continue
    dates.append(d["Date d'inscription"].split("T")[0])
    # dates.append(d["Date d'inscription"].split("T")[0].split("-")[0] + "-" + d["Date d'inscription"].split("T")[0].split("-")[1])
    ids.append(d["Phase"] + d["Ligne"])
    docs.append(clean_txt(d[field]))

# for m in month:
#     count_by_month.append(dates.count(m))

def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

days = ['2015-09-01', '2015-09-02', '2015-09-03', '2015-09-04', '2015-09-05', '2015-09-06', '2015-09-07', '2015-09-08', '2015-09-09', '2015-09-10', '2015-09-11', '2015-09-12', '2015-09-13', '2015-09-14', '2015-09-15', '2015-09-16', '2015-09-17', '2015-09-18', '2015-09-19', '2015-09-20', '2015-09-21', '2015-09-22', '2015-09-23', '2015-09-24', '2015-09-25', '2015-09-26', '2015-09-27', '2015-09-28', '2015-09-29', '2015-09-30']

print(days)

for d in days:
    count_by_days.append(dates.count(d))

print
print count_by_days
print

# top_words = ["accompagner","accueil","actions","actuel","administratif","agir","aider","aide","ailleurs","aimerais","ami","annees","appartement","apporterait","apprendre","arrive","article","association","attente","aujourd'hui","belle","besoin","cadre","calm","chaleur","chambre","chance","changer","cherche","choses","citoyenne","coeur","conditions","confiance","confort","connaitre","conscience","contacter","contribution","couple","coup","croiser","culture","decouvert","decouvrir","demarche","detresse","devoir","difference","difficile","dire","disponible","disposition","donne","drames","echange","egalement","enfants","engager","enrichir","entendu","entraider","envie","espace","esperant","essayer","etre","europe","evident","existe","experience","face","facile","faire","familles","femme","fille","fils","france","fuient","gens","guerre","habitants","hasard","hebergement","heureuse","hommes","humain","idee","immigration","important","informe","initiative","integrer","interessante","internet","inter","jeune","journaux","jour","langue","libre","lien","logement","longtemps","lu","main","maison","malheureusement","mal","medias","meilleur","mer","mesure","mieux","migrants","misere","moment","monde","montrer","motiver","moyens","necessaire","niveau","normal","nouveau","nuage","occasion","occuper","offrir","organisation","ouvrir","paix","parents","paris","parler","partager","participation","particulier","partie","pays","penser","permettre","personnelle","personne","petit","place","plusieurs","politique","porte","possible","pouvoir","preter","probleme","prochain","profiter","projet","proposer","quelqu'un","question","quitter","quotidien","radio","recevoir","recherche","refugies","regarder","relation","rencontrer","rendre","reponse","reportage","reseaux","respect","reste","retrouver","rien","sensible","sentir","serieux","services","seul","simplement","singa","site","situation","sociaux","societe","solidaire","solution","sorte","souhait","soutien","structures","supporte","syrie","temps","toit","tombee","touches","toujours","travail","trouver","tv","urgence","utile","valeurs","vecu","venir","vide","ville","vivre","voir","vouloir","voyager"]

# top_words_small = ["accompagner","accueil","agir","aider","aide","apporterait","apprendre","attente","aujourd'hui","belle","besoin","chaleur","changer","contribution","croiser","culture","decouvrir","demarche","detresse","devoir","difference","difficile","dire","disponible","donne","drames","echange","engager","enrichir","entraider","envie","essayer","evident","faire","fuient","guerre","heureuse","immigration","important","integrer","internet","inter","libre","lien","longtemps","malheureusement","mal","meilleur","mer","migrants","misere","montrer","motiver","normal","occuper","offrir","ouvrir","paix","parler","partager","penser","permettre","personne","politique","possible","pouvoir","preter","probleme","proposer","quitter","quotidien","radio","recevoir","refugies","regarder","relation","rencontrer","rendre","reponse","reportage","reseaux","respect","retrouver","sensible","sentir","seul","singa","site","situation","sociaux","societe","solidaire","solution","soutien","syrie","toit","travail","trouver","tv","urgence","utile","valeurs","venir","vivre","voir","vouloir"]

# top_words_verbe = ["accompagner","agir","aider","apprendre","changer","croiser","decouvrir","devoir","dire","engager","enrichir","entraider","essayer","faire","fuient","integrer","montrer","motiver","occuper","offrir","ouvrir","parler","partager","penser","pouvoir","preter","proposer","quitter","recevoir","rencontrer","rendre","retrouver","sentir","trouver","venir","vivre","voir","vouloir"]

top_words_media = ["internet","radio"]

csv = open("time_series_mots_media.csv", "w") 
csv.write("mot;date;percent\n")

top_stems = [stemmer.stem(t) for t in top_words_media]

cpt = 0
for word in top_stems:
    print("--- " + word)
    print

    count = []
    for d in days:
        count.append(0)
    
    idx = 0
    for doc in docs:
        count[days.index(dates[idx])] = count[days.index(dates[idx])] + (1 if word in doc else 0)
        idx  = idx + 1        

    percent = []

    idx = 0
    for c in count:
        tmp = (float(c)*100)/float(count_by_days[idx])
        percent.append(tmp)
        csv.write(top_words_media[cpt] + ";" + days[idx] + ";" + str(tmp) + "\n")
        idx  = idx + 1

    print count
    print
    print percent
    print

    idx  = 0
    d3js = []
    for d in days:
        tmp = {}
        tmp["date"] = d
        tmp["freq"] = percent[idx]
        d3js.append(tmp)
        idx = idx + 1

    print d3js
    print


    cpt = cpt + 1

#### Ajouter un stemmer