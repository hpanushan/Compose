import re

def cleanString(text):
    # Removing all non-letters
    text = re.sub("[^a-zA-Z]", " ", text)

    return text

