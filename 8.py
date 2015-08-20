def is_palindrome(input_string):
    reverse_string=input_string[::-1]
    if reverse_string==input_string:
        print ("True")
    else:
        print ("False")

input_string = raw_input("Please enter a string: ")
is_palindrome(input_string)