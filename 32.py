def is_palindrome(fname):
    with open(fname) as f:
        lines = f.readlines()

    for line in lines:
        input_string = (" ".join(line.split()))
        reverse_string = input_string[::-1]

        if reverse_string == input_string:
            print (input_string)

fname = "/home/pavkata/test/test.txt"
is_palindrome(fname)