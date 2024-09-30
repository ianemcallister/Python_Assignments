
# check for anagrams
def is_anagram(str1, str2):
    # sort each string passed in
    # compare the strings passed in for equivilancy
    return sorted(str1.lower()) == sorted(str2.lower())

# define the strings to evalue AND return results
print(is_anagram('listen', 'silent')) # should return true
print(is_anagram('listen', 'bark')) # should return false