def generate_n_chars(n,c):
    print  (''.join([ c for i in range(int(n))]))


c = raw_input("Please enter a character: ")
n = raw_input("Please enter how many times to repeat the character: ")
generate_n_chars(n,c)


