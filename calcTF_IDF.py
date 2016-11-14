#Compute TF IDF for words

from math import log


#Query term to calculate TF IDF

QUERY_TERMS = ['mr.' , 'green']

def tf(term , doc , normalize = True):

      doc = doc.lower().split()
      if normalize:
            return doc.count(term.lower()) / float(len(doc))
      else:
            return doc.count(term.lower()) / 1.0



def idf(term , corpus):
      numTextsWithTerm = len([True for text in corpus if term.lower()
                              in text.lower().split()])

      try:
            return 1.0 + log(float(len(corpus) / numTextsWithTerm))
      except ZeroDivisionError:
            return 1.0

def tf_idf(term , doc , corpus):
      return tf(term , doc) * idf(term , corpus)


corpus = {'a': 'Mr. Green killed Colonel Mustard in the study with the candlestick. \
Mr. Green is not a very nice fellow.',
'b': 'Professor Plum has a green plant in his study.',
'c': "Miss Scarlett watered Professor Plum's green plant while he was away \
from his office last week"}

for(key , value) in sorted(corpus.items()):
      print(key , " : " , value)

print("\n")

queryScores = {'a': 0 , 'b': 0 , 'c': 0}

for term in [t.lower() for t in QUERY_TERMS]:
      for doc in sorted(corpus):
            print("TF(%s) : %s" %(doc , term) , tf(term , doc))

      print("IDF : %s" %(term , ) , idf(term , corpus.values()))

      print("\n")
      
      for doc in sorted(corpus):
            score = tf_idf(term , corpus[doc] , corpus.values())
            print("TF-IDF(%s): %s" %(doc , term) , score)
            queryScores[doc] += score
      print("\n")

print("Overall TF - IDF scores for query %s" %(''.join(QUERY_TERMS) , ))
for(doc , score) in sorted(queryScores.items()):
      print(doc , score)

      
