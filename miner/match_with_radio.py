# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import json
import nltk
import re
import collections
import operator

from nltk.stem.snowball import SnowballStemmer
from unidecode import unidecode

field = "Motivations"

# open the data
with open('letters.json') as data_file:    
    data = json.load(data_file)

inter_1 = "Soyez solidaires accueillez un réfugié chez vous. C'est ce que propose l'association Singa qui vient en aide à ces hommes et ces femmes qui ont vu leur demande d'asile acceptée. Ils étaient près de 14.000 en France l'année dernière. Ces réfugiés ont beau avoir obtenu ce statut ils n'arrivent généralement pas à trouver un logement et ils restent des mois dans les centres d'accueil de demandeurs d'asile. Chambres d'accueil chez soi pour personnes réfugiées. Reportage de Julie piétri.\nJ'ai deux chats, 90 moutons et une chambre de disponible pour un réfugié. Des propositions d'hébergement, Nathanaël molle le directeur de l'association Singa On a reçu 200 en deux jours de la plus classique chambre d'amis dans un appartement en ville, à celle ci dans la ferme d'une bergère. L'accueil des personnes qui fuient la persécution ce n'est pas juste l'affaire de l'Etat. Bien sûr l'Etat joue son rôle et c'est très important de le rappeler. C'est aussi l'affaire de n'importe quel citoyen.\nCe soir les futurs hôtes seront formés avec explications sur le parcours des réfugiés découverte du numéro de téléphone qu'ils pourront composer 24 heures sur 24 en cas de difficulté. L'association leur proposera aussi de poser des conditions.\nSi par exemple il y a des femmes qui ne se sentent pas forcément à l'aise d'accueillir un homme chez elles elles peuvent cocher femme sur le formulaire d'inscription. On a eu des personnes qui nous ont dit moi je suis vegan et je ne veux pas d'animaux morts dans mon frigidaire donc il faut que la personne soit d'accord avec ça.\nC'est exigeant c'est un petit peu comme faire son marché?\nCe qui est important c'est que les gens vivent bien ensemble.\nPour l'instant l'association cherche un logement pour près de 30 personnes des Syriens des Congolais des Iraniens. L'association pose quelques conditions pour l'hébergement. Avoir un vrai espace à proposer et être prêt à recevoir la personne de deux semaines à six mois. Et une première réunion d'information destinée aux familles qui aimeraient participer aura lieu ce soir à Paris au sens cube à 19h30. Renseignements également disponibles sur le site internet de l'association.\n"
inter_2 = "Le 5/7. Oui dans l'esprit d'initiative. Ce matin nous allons dans les locaux de l'association Singa une association qui organise l'accueil des réfugiés dans des familles françaises et bien plus encore.\nBonjour Eric, Bonjour Catherine. Au moment où les initiatives citoyennes se multiplient pour accueillir les réfugiés on peut souligner qu'héberger est une chose accueillir en est une autre. C'est le cœur même de l'action menée par Singa une jeune association qui accompagne les réfugiés qui ont été reconnus à développer des projets culturels ou d'entreprise sur notre territoire. Avant de lancer ce programme ambitieux son fondateur Nathanel Molle a mené une étude dans quinze pays pour étudier ce qui se fait à l'étranger en terme d'intégration afin de trouver la formule la mieux adaptée à la France. Pari réussi puisqu' aujourdhui la plate forme qu'il a créée permettant de mettre en rapport bénévoles et réfugiés est victime de son succès. La clé qui ouvre toutes les portes est fondée sur la rencontre pour d'abord faire tomber les préjugés Nathanael Molle.\nL'idée c'est de réunir les gens tout leur passion commune et leurs projets. ça a été notre première action donc on a créé une communauté dans laquelle il va y avoir un grand nombre d'événements qui vont être toujours ouverts autant aux réfugiés qu'à la société parce que pendant ces événements là il n'y a pas de réfugiés. Il n'y a pas de Français. Il y a juste des gens qui sont passionnés par le yoga par le football et par l'art et par le théâtre. Et cette rencontre là elle vaut beaucoup plus qu'une rencontre qui serait organisée pour venir rencontrer les réfugiés. L'année dernière on a eu plus de mille personnes par exemple qui sont engagés d'une manière ou d'une autre en Ile de France sur l'accueil de personnes réfugiées. Nous on demande aux gens de partager avec la communauté des choses qu'ils veulent faire qu'ils aiment faire et qu'ils ont envie de faire. Et ça ça change vraiment tout.\nConcrètement quels sont les projets qui ont abouti.\nPour nous l'aboutissement c'est quand la personne est autonome quand elle a son réseau social professionnel qu'elle parle suffisamment français pour se débrouiller et donc on a plus de 80 pour cent des projets qu'on a accompagné et qui sont dans cette situation là.\nEt si vous souhaitez vous aussi proposer des projets ou si vous avez des passions à partager tout en voulant accueillir des réfugiés. Quelques clics sur la page de la chronique esprit d'initiative sur France Inter point fr et vous retrouverez les coordonnées de cette association Singa. Et l'accueil des réfugiés chez soi. Ce sera le thème d'un jour en France à diserts avec comme invité le fondateur de Singa nathanaël molle que vous venez d'entendre et a quelques minutes."
inter_3 = "Au standard d'un jour en France également nathanaël molle. Bonjour. Oui bonjour. Confondateur. Cofondateur et directeur de l'association Singa on a beaucoup parlé de vous ces derniers jours vous mettez en relation via Internet des réfugiés des particuliers qui souhaitent accueillir des personnes chez elles. Réaction peut être à ce que vient de dire Pierre Henry sur le thème c'est à l'Etat d'organiser ça. Ce n'est pas aux particuliers.\nMoi je pense que c'est une responsabilité partagée en chacun doit jouer son rôle et en tant que citoyen on a un rôle à jouer dans l'accueil des personnes qui fuient la persécution. Il faut aussi éviter la situation où des personnes réfugiées sont en France depuis 3 4 ans et ne connaissent que des personnes qui sont payées par l'Etat pour les accompagner. On a une vraie problématique d'isolation des personnes. Et aujourd'hui il faut que la société joue son rôle et participe également comme le dit Pierre Henry de manière simple mais de manière importante à l'accueil des réfugiés.\nNathanaël molle Combien de propositions avez vous reçu à ce jour de personnes qui disent moi je suis prêt à recevoir quelqu'un chez moi?\nAlors on a reçu plus de 7200 propositions aujourd'hui provenant de toute la France de personnes de toutes catégories socio-professionnelles. C'est assez incroyable d'ailleurs on a des personnes qui nous disent voilà j'ai mon voilier qui est disponible dans le port et qui du coup peut héberger une famille. Et à côté de cela on a deux personnes qui nous disent moi j'ai une chambre et un salon et du coup je suis prêt à partager avec cette personne le salon. Alors bien sûr on leur explique que c'est pas tout à fait possible. Il faut quand même un certain nombre de critères.\nAlors voilà justement ce qu'il y, mes deux questions suivantes Combien de personnes combien de colocation entre guillemets se sont déjà mises en place et quelles sont les règles. Quel est le cahier des charges?\n Est ce qu'il y a un cadre juridique précis?\nEn fait pour vous dire la vérité on ne s'attendait absolument pas à un tel nombre de personnes. Donc on a mis un peu de temps à réagir.Aujourd'hui on a placé plus de trente personnes en 5 jours. parce que ca fait 5 jour qu'on a commencé à réellement placer les gens.\nDonc 30 sur 7200?\nOui on va avoir un outil très prochainement ce qui va nous permettre de placer beaucoup plus de personnes beaucoup plus rapidement. On va proposer à partir du mois prochain à d'autres villes de France de pouvoir héberger parce que pour l'instant c'est surtout en ile de France.\nEt sur le cadre juridique, sur le cahier des charges?\nPour nous ce qui est important, c'est que la personne ait un minimum d'intimité. Ca c'est la première chose, donc souvent une chambre est nécessaire. Il y a des familles qui nous disent voilà il y a un petit salon qu'on peut mettre à disposition. Mais on sait que sur le long terme ça peut etre difficile. Du coup on garde ces propositions là pour des situations d'urgence. Mais l'idée c'est cette question de l'intimité, et de l'autre coté on a aussi parce que nous Singa on travaille avec des personnes réfugiées statutaires qui ont obtenus leurs statut de réfugier.Et il faut que la personne réfugiée touche au moins le RSA. Pour pouvoir aller chez une famille avec l'idée qu'elle va pouvoir ainsi contribuer aux dépenses de la famille ou niveau de la nourriture etc..\nMerci d'être intervenu au standard nathanaël molle."

months = ['2015-09','2015-10','2015-11','2015-12','2016-01','2016-02','2016-03','2016-04','2016-05','2016-06','2016-07','2016-08','2016-09','2016-10','2016-11','2016-12','2017-02']

french_stopwords = set(["au","aux","avec","parce","plus","ce","dont","ces","toute","tous","toutes","dans","de","des","du","elle","en","et","eux","il","je","la","le","leur","lui","ma","mais","me","meme","mes","moi","mon","ne","nos","notre","nous","on","ou","par","pas","pour","qu","que","qui","sa","se","ses","son","sur","ta","te","tes","toi","ton","tu","un","une","vos","votre","vous","c","d","j","l","a","m","n","s","t","y","ete","etee","etees","etes","etant","suis","es","est","sommes","etes","sont","serai","seras","sera","serons","serez","seront","serais","serait","serions","seriez","seraient","etais","etait","etions","etiez","etaient","fus","fut","femes","futes","furent","sois","soit","soyons","soyez","soient","fusse","fusses","fut","fussions","fussiez","fussent","ayant","eu","eue","eues","eus","ai","as","avons","avez","ont","aurai","auras","aura","aurons","aurez","auront","aurais","aurait","aurions","auriez","auraient","avais","avait","avions","aviez","avaient","eut","eumes","eutes","eurent","aie","aies","ait","ayons","ayez","aient","eusse","eusses","eut","eussions","eussiez","eussent","ceci","cela","cela","cet","cette","ici","ils","les","leurs","quel","quels","quelle","quelles","sans","soi"])
stopwords_set = set(nltk.corpus.stopwords.words('french')) | french_stopwords
stemmer = SnowballStemmer("french")

def token_txt(txt):
    txt    = txt.replace("'"," ") 
    tokens = [word.lower() for sent in nltk.sent_tokenize(txt) for word in nltk.word_tokenize(sent)]
    tokens = [x for x in tokens if x not in stopwords_set]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

def stem_txt(txt):
    stems = [stemmer.stem(t) for t in txt]
    return stems    

inter_1_token = token_txt(unicode(inter_1, 'utf-8'))
inter_2_token = token_txt(unicode(inter_2, 'utf-8'))
inter_3_token = token_txt(unicode(inter_3, 'utf-8'))

inter_1_stem = stem_txt(inter_1_token)
inter_2_stem = stem_txt(inter_2_token)
inter_3_stem = stem_txt(inter_3_token)

result = {"inter_1":{},"inter_2":{},"inter_3":{}}
result["inter_1"]["full"] = inter_1
result["inter_2"]["full"] = inter_2
result["inter_3"]["full"] = inter_3

result["inter_1"]["stem"] = inter_1_stem
result["inter_2"]["stem"] = inter_2_stem
result["inter_3"]["stem"] = inter_3_stem

result["inter_1"]["token"] = {}
result["inter_2"]["token"] = {}
result["inter_3"]["token"] = {}

cpt = 1
for tk in inter_1_token:
    result["inter_1"]["token"][tk] = [0,"I1-" + str(cpt),[]]
    cpt = cpt + 1

cpt = 1
for tk in inter_2_token:
    result["inter_2"]["token"][tk] = [0,"I2-" + str(cpt),[]]
    cpt = cpt + 1    

cpt = 1
for tk in inter_3_token:
    result["inter_3"]["token"][tk] = [0,"I3-" + str(cpt),[]]
    cpt = cpt + 1

# go through letters

docs     = []
letters  = []
ids      = []
dates    = []

for d in data: 
    if field not in d or d[field] == "" or d["Date d'inscription"] is None:
        continue
    dates.append(d["Date d'inscription"].split("T")[0].split("-")[0] + "-" + d["Date d'inscription"].split("T")[0].split("-")[1])
    ids.append(d["Phase"] + d["Ligne"])
    letters.append(d[field])
    docs.append(stem_txt(token_txt(d[field])))

result_letters = []

cpt = 0
for d in docs:
    if "radio" in d or "inter" in d:
        result_letters.append({"id":ids[cpt],"date":dates[cpt],"sort":months.index(dates[cpt]),"text":letters[cpt],"token":docs[cpt],"inter_tk":[]})
    cpt = cpt + 1

from operator import itemgetter
result_letters = sorted(result_letters, key=itemgetter("sort")) 

cpt = 0
for doc in result_letters:

    idl = doc["id"]
    for tkl in doc["token"]:  
        if tkl in result["inter_1"]["stem"] :
            # on gère inter
            idx_inter_stem = result["inter_1"]["stem"].index(tkl)
            inter_tk = inter_1_token[idx_inter_stem]
            if result["inter_1"]["token"][inter_tk][0] == 0:
                result["inter_1"]["token"][inter_tk][0] = 1
            result["inter_1"]["token"][inter_tk][2].append(idl)
            #on gère letters
            if result["inter_1"]["token"][inter_tk][1] not in doc["inter_tk"]:
                doc["inter_tk"].append(result["inter_1"]["token"][inter_tk][1])

        if tkl in result["inter_2"]["stem"] :
            # on gère inter
            idx_inter_stem = result["inter_2"]["stem"].index(tkl)
            inter_tk = inter_2_token[idx_inter_stem]
            if result["inter_2"]["token"][inter_tk][0] == 0:
                result["inter_2"]["token"][inter_tk][0] = 1
            result["inter_2"]["token"][inter_tk][2].append(idl)
            #on gère letters
            if result["inter_2"]["token"][inter_tk][1] not in doc["inter_tk"]:
                doc["inter_tk"].append(result["inter_2"]["token"][inter_tk][1])

        if tkl in result["inter_3"]["stem"] :
            # on gère inter
            idx_inter_stem = result["inter_3"]["stem"].index(tkl)
            inter_tk = inter_3_token[idx_inter_stem]
            if result["inter_3"]["token"][inter_tk][0] == 0:
                result["inter_3"]["token"][inter_tk][0] = 1
            result["inter_3"]["token"][inter_tk][2].append(idl)
            #on gère letters
            if result["inter_3"]["token"][inter_tk][1] not in doc["inter_tk"]:
                doc["inter_tk"].append(result["inter_3"]["token"][inter_tk][1])

for res in result:
    result[res].pop("stem")

for doc in result_letters:
    doc.pop("token")

# top_inter_3 = {}

# for res in result["inter_3"]["token"]:
#     top_inter_3[res] = len(result["inter_3"]["token"][res][2])

# top_inter_3_sorted = sorted(top_inter_3.items(), key=operator.itemgetter(1), reverse=True)

# print top_inter_3_sorted

# for k in top_inter_3_sorted[:20]:
#     print k

# with open('france_inter_match.json', 'w') as outfile:
#     json.dump(result, outfile)

# with open('letters_match.json', 'w') as outfile:
#     json.dump(result_letters, outfile)    

