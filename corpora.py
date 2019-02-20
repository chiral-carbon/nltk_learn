import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

#Path for corpora: /home/blackcanary/nltk_data/corpora

sample = gutenberg.raw("austen-emma.txt")

tok = sent_tokenize(sample)

print(tok[:15])

