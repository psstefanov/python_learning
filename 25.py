import re

def make_ing_form(verb):

    vowels = ["a", "e", "i", "o", "u"]
    suffix1 = ("e")
    suffix2 = ("ie")
#
    if verb == ["be", "see", "flee", "knee"]:
        print "Qkata rabota"
    elif verb.endswith(suffix1):
        return re.sub('e$','isng ',verb)
    elif verb.endswith(suffix2):
        return  "".join((verb, "es"))
    else:
        return  "".join((verb, "s"))

verbs = "lie", "see", "move", "hug"
for verb in verbs:
    print (make_ing_form(verb))


#        if verb not in ["be", "see", "flee", "knee"]: