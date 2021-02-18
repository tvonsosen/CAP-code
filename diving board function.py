# returns all possible lengths of a diving board based on the parameters

def boardLength(longBoard, shortBoard, planksNum):
    possibleLengths = []
    for i in range(planksNum+1):
        possibleLengths.append((longBoard*(planksNum-i)) + (shortBoard*i))
    return possibleLengths
