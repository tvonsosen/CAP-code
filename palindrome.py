# Gives you the longest palindrome in a string of integers

import string
def palindromeFind(stringofLett):
    palindromeright = ''
    palindromeleft = ''
    alphabet = list(string.ascii_letters)
    letValues = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    other = ''
    for i in list(stringofLett):
        letValues[ord(i)-ord('a')] += 1
    for x in range(26):
        i = letValues[x]
        for y in range((i-i%2)//2):
            palindromeleft += alphabet[x]
            palindromeright = alphabet[x]+palindromeright
        if i % 2 == 1 and other == '':
            other = alphabet[x]
    return (palindromeleft+other+palindromeright)
    
  palindromeFind('abc')
