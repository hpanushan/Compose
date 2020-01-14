from gensim.models.doc2vec import TaggedDocument
from nltk.tokenize import word_tokenize

from ReadTextFile import readTextFile
from RemoveStopWords import removeStopWords
from TrainModel import trainModel

def main():
    # Attributes
    datasetLocation = 'data/train.csv'
    modelLocation = 'data/d2v.model'

    # Reading the dataset
    phrasesList = readTextFile(datasetLocation)

    # Tagging the dataset
    taggedData = [TaggedDocument(words=removeStopWords(word_tokenize(_d.lower())),tags=[str(i)]) for i, _d in enumerate(phrasesList)]
    print("Tgging part is done")

    trainModel(taggedData,modelLocation)

if __name__ == '__main__':
    
    main()

