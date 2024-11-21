from nltk.stem.porter import *
tokens=["connection","connecting","disconnect","connect","connected"]
stemmer=PorterStemmer()
for token in tokens:
    print(token + "->"+stemmer.stem(token))
print("------------------------------------------")
from nltk.stem.lancaster import *
lancaster=LancasterStemmer()
tokens2=["lovely","decentralized","better","information","disable","did"]
for token in tokens2:
    print(token + "->"+stemmer.stem(token))
    print(token + "->"+lancaster.stem(token))
    print("------------------------------------------")
#--------------------------------------------------------------------
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
for token in tokens2:
    print(token + "->"+stemmer.stem(token))
    print(token + "->"+lemmatizer.lemmatize(token))
    print(token + "->"+lemmatizer.lemmatize(token,pos="a"))
    print(token + "->"+lemmatizer.lemmatize(token,pos="v"))
    print("=================================================")
