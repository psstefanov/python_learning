import re

def make_ing_form(verb):

    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z" ]
    suffix1 = ("e")
    suffix2 = ("ie")
    if verb in ["be", "see", "flee", "knee"]:
        return  "".join((verb, "ing"))
    elif verb.endswith(suffix1):
        return re.sub('e$','ing ',verb)
    elif verb.endswith(suffix2):
        return  "".join((verb, "es"))
    else:
        return  "".join((verb, "ing"))

verbs = "lie", "see", "move", "hug", "be"
for verb in verbs:
    print (make_ing_form(verb))
