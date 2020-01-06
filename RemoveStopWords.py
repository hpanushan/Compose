from nltk.corpus import stopwords 

def removeStopWords(tokenizedSentence):  
    stop_words = set(stopwords.words('english')) 
  
    filteredSentence = [w for w in tokenizedSentence if not w in stop_words] 
  
    return filteredSentence
