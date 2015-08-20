def countStringLength(inputString):
    count = 0

    for i in inputString:
        count = count+1
        print (i)

    print ("Length of the String is " + str(count))

inputString = raw_input("Enter the string: ")

countStringLength(inputString)
