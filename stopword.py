import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
#print(stop_words)
example = "This is an example sentence for showing off stopword filtration."
words = word_tokenize(example)

filtered_sentence = [w for w in words if w not in stop_words]

print(filtered_sentence)