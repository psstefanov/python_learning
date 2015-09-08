import string
keys  = string.lowercase
values  = range(1,27)
dictionary = dict(zip(keys, values))
#code = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
code = "pnrfne pvcure? v zhpu cersre pnrfne fnynq!"
translate=[]
for i in code:
    if dictionary.get(i):
        id = dictionary.get(i)
        ceaser = id + 13
        if ceaser <= 26:
            key=list(dictionary.keys())[list(dictionary.values()).index(ceaser)]
            #print (key)
            translate.append(key)
        else:
            ceaser = ceaser - 26
            ceaser = abs(ceaser)
            key=list(dictionary.keys())[list(dictionary.values()).index(ceaser)]
            #print (key)
            translate.append(key)
    else:
        #print (i)
        translate.append(i)
message = ''.join(translate)
print message
