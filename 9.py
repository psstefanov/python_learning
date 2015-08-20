def is_member(value):
    group="111111"
    # for i in group:
    #     if value==i:
    #         print "True"
    #     else:
    #         print "False"

    b= group.find(value)

value= raw_input("Enter a char to compare: ")
is_member(value)