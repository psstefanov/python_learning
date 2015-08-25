def find_longest_word(inputList):
    lenght = []
    for i in (inputList):
        lenght.append(len(i))
    print (max(lenght))

#List = ["test","new","script", "jhsdabvkljhgdfkjhsakl", "r 2"]
List = input("Please input a list of words to evaluate: ")
find_longest_word(List)
