# Function to find sum of arguments

def findSum(*args):
    value = 0
    for i in args:
        value = value + i
    return value

print(findSum(-1,2,3.4,4,5.5))
