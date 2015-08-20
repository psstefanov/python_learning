file = open ("test.txt",'r+w')

file.write("first line\n")
print file.read()
file.write("second line\n")

#file.write("and another line\n")

#print file.read()

file.close()

#file = open ("test.txt",'r')
#print file.read()