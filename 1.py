# Exercises from http://www.ling.gu.se/~lager/python_exercises.html

def max(a,b):

    if a>b:
        return a
    elif a<b:
        return b

print ("Please enter first number to compare: ")
a = input()

print ("Please enter second number to compare: ")
b= input()

print  (str(max(a,b)) + ' is larger')
