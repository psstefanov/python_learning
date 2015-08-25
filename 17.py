import re

def is_palindrome2(input_string):
    clear_string=re.sub(r'[^\w]', '', input_string).lower()
    reverse_string=clear_string[::-1]
    if reverse_string==clear_string:
        print ("True")
        print (clear_string)
        print (reverse_string)
    else:
        print ("False")
        print (clear_string)
        print (reverse_string)

input_string = raw_input("Please enter a string: ")
is_palindrome2(input_string)