# def is_member(value):
#     group="jkjhliyugoiuhp98u-98u-98uw-e59"
#     for i in group:
#         if value==i:
#             print "True"
#         else:
#             print "False"
#
# value= raw_input("Enter a char to compare: ")
# is_member(value)


chars = set('01111123456789$,')
s="zzz"
if any((c in chars) for c in s):
    print('Found')
else:
    print('Not Found')