import nltk
from nltk.corpus import wordnet

syns = wordnet.synsets("program")

#all synonyms as synsets
print(syns)

#referencing the first synset
print(syns[0])

#synset - just the name
print(syns[0].name())

#the lemmas of the first synset
print(syns[0].lemmas())

#just the word of the first lemma of the first synset
print(syns[0].lemmas()[0].name())

#definition - dictionary meaning of the first synset
print(syns[0].definition())

#examples - example sentences
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
	for l in syn.lemmas():
		#print("l: ",l)
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))