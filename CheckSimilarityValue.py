
def checkSimilarityValue(similarityValue):
    # Checking similarity value and pass to manual assistance(Check new activation,booking and ordering)
    thresholdValue = 0.75
    if similarityValue>thresholdValue:
        return True

    else:
        return False

