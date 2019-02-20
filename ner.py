import nltk
from nltk.corpus import state_union as su
from nltk.tokenize import PunktSentenceTokenizer as pst

train_text = su.raw("2005-GWBush.txt")
sample_text = su.raw("2006-GWBush.txt")

custom_sent_tokenizer = pst(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			
			namedEnt = nltk.ne_chunk(tagged, binary=True)

			namedEnt.draw()

	except Exception as e:
		print(str(e))

process_content()