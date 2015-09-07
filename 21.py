#Exercise 21
 
#Write a function char_freq() that takes a string and builds a frequency
#listing of the characters contained in it. Represent the frequency listing
#as a Python dictionary. Try it with something like
#char_freq("abbabcbdbabdbdbabababcbcbab").
 
def char_freq(inputString):
 
    dictionary = {}
    keyWord = ""
 
    print(inputString)
     
    for i in range(len(inputString)):
 
        if inputString[i] in dictionary:
            dictionary[inputString[i]]= int(dictionary.get(inputString[i]))+1
        else:
            dictionary[inputString[i]]= 1
 
    return dictionary
         
print(str(char_freq("abbabcbdbabdbdbabababcbcbab")))