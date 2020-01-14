
def readTextFile(fileLocation):
    # Read the phrases file and remove new line character
    
    lineList = [line.rstrip('\n') for line in open(fileLocation)]

    # Cleaning the tab character from phrases
    cleanedList = [line.rstrip('\t') for line in lineList]

    return cleanedList

    