# Function that adds and subtracts every successive number passed in


# This function's argument, *args creates a tuple with the values input
def addSubtract(*args):
    value = 0
    for i in range(len(args)):
        value = value + (args[i] if i%2 != 0 or i == 0 else - args[i])
    # Starts out adding the first and second values, i = 0 and i = 1
    return value

print(addSubtract(1,2,3,4,-5.5))
