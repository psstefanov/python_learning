shopList = []
maxLengthList = 6
#while len(shopList) < maxLengthList:
item = []
while item != "":
    item = raw_input("Enter your Item to the List: ")
    shopList.append(item)
print "That's your Shopping List"
print shopList