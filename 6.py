'''
def sum(a, b, c, d):
    result=(a+b+c+d)
    print ("The result on sum is "+ str(result))

def multiply(a, b, c, d):
    result=(a*b*c*d)
    print ("The result of multiply is "+ str(result))

a = input("Please enter a number: ")
b= input("Please enter a number: ")
c= input("Please enter a number: ")
d= input("Please enter a number: ")

sum(a, b, c, d)
multiply(a, b, c, d)

'''
def sum(input_numbers):
    result = 0
    #input_numbers.replace(" ", "")
    for i in input_numbers:
        result =result+int(i)
    return  result


input_numbers= raw_input("Please enter numbers: ")
print (sum(input_numbers.replace(" ", "")))
