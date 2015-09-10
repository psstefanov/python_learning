import re

def make_3sg_form(verb):

    suffix1 = ("y")
    suffix2 = ("o", "ch", "s", "sh", "x", "z")

    if verb.endswith(suffix1):
        return re.sub('y$','ies ',verb)
    elif verb.endswith(suffix2):
        return  "".join((verb, "es"))
    else:
        return  "".join((verb, "s"))

verbs = "try", "brush", "run", "fix"
for verb in verbs:
    print (make_3sg_form(verb))