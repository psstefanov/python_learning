#is_pangram = lambda s: not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())

def is_pangram(s):
     return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())

print (is_pangram('The quick brown fox jumps over the lazy dog'))