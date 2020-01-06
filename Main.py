from nltk.tokenize import word_tokenize
from RemoveStopWords import removeStopWords
from gensim.models.doc2vec import TaggedDocument

from ReadTextFile import readTextFile
from TrainModel import trainModel

def main():
    # Read the dataset 
    phrasesList = readTextFile("data/food_order.txt")

    print(len(phrasesList))

    # Use Map-reduce method
    taggedData = [TaggedDocument(words=removeStopWords(word_tokenize(_d.lower())),tags=[str(i)]) for i, _d in enumerate(phrasesList)]
    print("Tgging part is done")

    trainModel(taggedData)

if __name__ == '__main__':
    main()
