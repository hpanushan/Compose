import multiprocessing
from gensim.models.doc2vec import Doc2Vec

def trainModel(taggedData):
    # Getting number of CPU core
    cpu_cores = multiprocessing.cpu_count()

    # Training
    model = Doc2Vec(taggedData,vector_size=300,
	            window=2,min_count=1,workers=cpu_cores,epochs=1000,dm=1)
    
    model.save('d2v.model')                
    print("Model Saved")

