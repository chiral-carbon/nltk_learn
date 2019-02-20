from nltk.corpus import wordnet

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

#prints similarity between the two words w1 and w2
#semantic relationship between all the words,
#as proposed by WUP
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")

print(w1.wup_similarity(w2))
