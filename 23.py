import re

def correct(inputString):
    autocorrect =  (" ".join(inputString.split()))

    return autocorrect

inputString = "This   is  very funny  and    cool.Indeed!"
print (correct(inputString))