import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

example_sentence = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(word_tokenize(example_sentence))

print(sent_tokenize(example_sentence))
