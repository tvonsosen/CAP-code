# A function to return the number of ways a person can climb n stairs through lists by jumping 1 or 2 stairs at a time

# Returns 1 for 0 stairs

def stairsList(n):
    # Uses Fibonacci Sequence: adds number of permutations of n-1 and n-2 to get number of permutations for n

    currentValue = 1 
    lastnumber = 0
   
    for i in range(1, n+1):
    
        secondLast = lastnumber
        lastnumber = currentValue
        currentValue = secondLast + lastnumber
     
    return currentValue


print(stairsList(8))
