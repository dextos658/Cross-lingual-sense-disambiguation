import stanza
import nltk
from pprint import pprint

# nltk.download('stopwords')
stanza.download('sl')       # This downloads the Slovene models for the neural pipeline
nlp = stanza.Pipeline('sl', preorocessors='tokenize') # This sets up a default neural pipeline in Slovene
doc = nlp("V Belorusiji se je začel tretji krog pogajanj o premirju. Na mizi so zahteve o notranjepolitični rešitvi krize, mednarodno humanitarnem in vojaškem vidiku.".lower())


def remove_stopwords(text, to_ignore):
    return [token for token in text if token not in to_ignore]


def remove_letters(text):
    return [token for token in text if len(token) > 1]


def preprocess(doc):
    s = []
    for sent in doc.sentences:
        tokens = []
        for word in sent.words:
            tokens.append(word.lemma)
        tokens = remove_stopwords(tokens, nltk.corpus.stopwords.words("slovene"))
        tokens = remove_letters(tokens)
        s.append(tokens)
    pprint(s)


preprocess(doc)