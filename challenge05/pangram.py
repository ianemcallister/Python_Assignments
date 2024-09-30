from string import ascii_lowercase #import the lowercase alphabet

# define the function
def pan_check(string):
    alphabet = set(ascii_lowercase) # assign the lowercase alphabet to the alphabet variable as a set
    return set(string.lower()) >= alphabet #checks that string is a subset of alphabet

print(pan_check('The quick brown fox jumps over the lazy dog'))