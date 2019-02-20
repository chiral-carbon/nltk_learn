import nltk
from nltk.stem import PorterStemmer as ps
from nltk.tokenize import word_tokenize

sample = ["python", "pythonly", "pythoning", "pythoned", "pythoner"]

for w in sample:
	print(ps().stem(w))

example_text = "It is important to be pythonly while pythoning with python. All pythoners have pythoned orally at least once."

new_sample = word_tokenize(example_text)

print("\nStemming the sentence:\n")

for w in new_sample:
	print(ps().stem(w))
