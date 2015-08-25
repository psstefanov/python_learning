def translate(english2):
    dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
    english = english2.split()
    translate = []
    for i in (english):
        if  (i.upper()  in (char.upper() for char in  dictionary)):
                translate.append(dictionary[i])
    swedish = ' '.join(translate)
    print (swedish)

english2 = raw_input("Enter English word: ")
translate(english2)
