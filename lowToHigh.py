# function that sums all the numbers from  the lower bound number given to the higher bound number given (inclusively)

def lowHigh(lowB, highB):
    answer1 = 0
    for i in range(lowB,highB +1):
        answer1 = answer1 + i
    return answer1

print(lowHigh(-2,5))
