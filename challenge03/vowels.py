
def vowel_counter(a_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0

    # define our loop
    for char in a_string:
        if char.lower() in vowels:
            counter += 1

    # return the counter value
    return counter


test_string = "And this is another string, what does this come back with?"
no_of_vowels = vowel_counter(test_string)
print('Found ' + str(no_of_vowels) + " in this string")