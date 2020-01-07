from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize

from ReadTextFile import readTextFile

def testModel(dataFileLocation,modelFileLocation,phrase):
	
	test_doc = word_tokenize(phrase.lower())

	# Read the text file 
	phrasesList = readTextFile(dataFileLocation)

	# Load the model
	model = Doc2Vec.load(modelFileLocation)

	# Getting similar phrases
	similarPhrases = model.docvecs.most_similar(positive=[model.infer_vector(test_doc)],topn=1)

	return phrasesList[int(similarPhrases[0][0])],float(similarPhrases[0][1])


