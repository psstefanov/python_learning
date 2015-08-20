def translate(input_string):
    vowels = ["a", "e", "i", "o", "u"]
    output_string=""
    for i in input_string:
        if  ( i.upper()  in (char.upper() for char in  vowels)):
            output_string+=i
        else:
            output_string+=i+"o"+i
    return output_string

input_string = raw_input("Please enter a string: ")
print (translate(input_string))