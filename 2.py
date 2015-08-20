def max_of_three(a,b,c):

    list = [a,b,c]
    list.sort
    max=list[-1]
    return max

print ("Please enter first number to compare: ")
a = input()

print ("Please enter second number to compare: ")
b= input()

print ("Please enter third number to compare: ")
c= input()


print (str(max_of_three(a,b,c)) + ' is largest')