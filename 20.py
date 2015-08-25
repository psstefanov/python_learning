def translate(english):
    swedish = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
    for i in (english):
        if  (i.upper()  in (char.upper() for char in  swedish)):
            print (swedish[i])

english = raw_input("Enter English word: ")
translate(english)
