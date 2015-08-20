def vowel(input_string):
    vowels = ["a", "e", "i", "o", "u"]
    if  ( input_string.upper()  in (char.upper() for char in  vowels)):
        print ("True")
    else:
        print ("False")

input_string = raw_input("Please enter a letter: ")
vowel(input_string[0])