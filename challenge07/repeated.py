
# import the Counter function in order to easily 
# create a dictionary of instance occurances of letters
# in the string to be passed in
from collections import Counter

# define the function
def find_first_non_repeated(string):
    char_counts = Counter(string) # define the dictionary of characters in the string
    
    # loop over all characters in the string
    for char in string:
        if char_counts[char] == 1: # looks for the key where in the KVP with a single instance
            return char # returns that char when it is found
    return None # if none are found it returns 'None'
    
# run the function
print(find_first_non_repeated("abracadabra")) #Output shoudl be "c"
