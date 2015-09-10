import re

def correct(inputString):
    whitespace =  (" ".join(inputString.split()))
    autocorrect = re.sub('\.','. ',whitespace)
    return autocorrect

inputString = "This   is  very funny  and    cool.Indeed!"
print (correct(inputString))
