def filter_long_words(userInput, n):
    for i in (userInput):
        if len(i) >=n:
            print (i)

n = 5
List = ["test","new","script", "jhsdabvkljhgdfkjhsakl", "r 2"]
filter_long_words(List, n)