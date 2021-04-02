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

   """
    Why use Fibonacci Sequence: 
    
     Permutations for stairs:
     0: 1 in this case
     1: 1         --> 1 + 2 = 12
     2: 2 11      --> 2 + 1 = 21   1 + 1 + 1  = 111
     3: 21 12 111     < -- ^^    
     4: 22 211 121 112 1111
     5: 221 122 212 1112 1121 1211 2111 1111

    Permutations for n:
    
    P(n) = P(n-1) + P(n-2)
    where P(n) is the number of permutations for n stairs
    This can be proved by induction

    """
