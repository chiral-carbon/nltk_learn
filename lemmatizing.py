import nltk
from nltk.stem import WordNetLemmatizer as wn

print(wn().lemmatize("cats"))
print(wn().lemmatize("cacti"))
print(wn().lemmatize("geese"))
print(wn().lemmatize("rocks"))
print(wn().lemmatize("python"))

print(wn().lemmatize("better"))#<---prints better
print(wn().lemmatize("better", pos="a"))#<---prints good
print(wn().lemmatize("best", pos="a"))#<---prints best
print(wn().lemmatize("best"))#<---prints best, passing it  as an adjective

print(wn().lemmatize("run"))#<---prints run, passing it as a verb
print(wn().lemmatize("run", 'v'))#<---prints run

#Correctly printed the root of 'run', also for 'best'
#with and without passing the POS tag

#But that is not always the case
#as seen in the case of 'better'

#When not lemmatizing a noun
#pass the POStag for that word
