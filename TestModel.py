from ReadTextFile import readTextFile
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize

phrase = input("Enter phrase - ")
test_doc = word_tokenize(phrase.lower())

# Read the dataset

fileLocation = 'data/food_order.txt'

# Read the text file 
phrasesList = readTextFile(fileLocation)

# Load the model
model = Doc2Vec.load("d2v.model")

# Getting similar phrases
similarPhrases = model.docvecs.most_similar(positive=[model.infer_vector(test_doc)],topn=5)

for i in similarPhrases:
	print(phrasesList[int(i[0])],i[1])


