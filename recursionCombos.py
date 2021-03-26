# A function that uses recursion to print all distinct combinations of a given length k, can repeat values from list
def combosList(list1, k):
    new = []
    # removes duplicate elements in given list so duplicate lists aren't printed
    for i in list1:
        if i not in new:
            new.append(i)
    generateCombos(new,0,k,[])
    
def generateCombos(list1,start,k,combo):
    # Prints list using recursion and then pops/replaces last value to print other combinations
    for i in range(start,len(list1)):
        combo.append(list1[i])
     
        if k == 1:
            print(combo)
        else:
            generateCombos(list1,i,k-1,combo)
 
        combo.pop()


combosList([1,2,3], 2)
