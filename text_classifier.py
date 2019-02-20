#Classifying text for sentiment analysis
#Opinion mining in this program: +ve or -ve connotation to sentiments
#This methodology can be applied to any category as long as:
#	1. They are tagged
#	2. Only two categories and not a range of categories
#	Eg. good or bad, spam or not spam
#	NOT: very good, slightly bad, etc.

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
				for category in movie_reviews.categories()
				for fileid in movie_reviews.fileids(category)]
"""
documents = []

for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.append(list(movie_reviews.words(fileid)), category)
"""

random.shuffle(documents)

#print(documents[0])

all_words = [w.lower() for w in movie_reviews.words()]

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(20))

print(all_words["stupid"])
