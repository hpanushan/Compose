from flask import Flask
from flask_restful import Resource, Api

from CheckSimilarityValue import checkSimilarityValue
from activation.ActivationMain import activationMain
from booking.BookingMain import bookingMain
from ordering.OrderingMain import orderingMain

app = Flask(__name__)
api = Api(app)

# Categories indexing
# 1 --> Activation
# 2 --> Booking
# 3 --> Ordering
class New(Resource):
    def get(self,category,phrase):
        # Activation
        if (category==1):
            fileLocation = 'activation/'
            modifiedPhrase = phrase.replace('+',' ')
            # Run main function in activation
            similarPhrase,similarPhraseValue = activationMain(fileLocation,modifiedPhrase)
            return {"similarPhrase":similarPhrase,"new?":checkSimilarityValue(similarPhraseValue)}, 200
        
        # Booking
        elif (category==2):
            fileLocation = 'booking/'
            modifiedPhrase = phrase.replace('+',' ')
            # Run main function in booking
            similarPhrase,similarPhraseValue = bookingMain(fileLocation,modifiedPhrase)
            return {"similarPhrase":similarPhrase, "new?":checkSimilarityValue(similarPhraseValue)}, 200

        # Ordering
        elif (category==3):
            fileLocation = 'ordering/'
            modifiedPhrase = phrase.replace('+',' ')
            # Run main function in ordering
            similarPhrase,similarPhraseValue = orderingMain(fileLocation,modifiedPhrase)
            return {"similarPhrase":similarPhrase,"new?":checkSimilarityValue(similarPhraseValue)}, 200

        else:
            return {"Error message": "Category number is not defined"}, 404

# Routes
api.add_resource(New,'/new/<int:category>/<string:phrase>')

if __name__ == '__main__':
    app.run(port='5000',debug=True)

