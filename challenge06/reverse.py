

# define the function
def word_reverse(sentence):
    words_list = sentence.split() # transform the string into a list
    reverse_sentence = " ".join(reversed(words_list)) # run the reversed function on the list of words, defining a space as the seperator
    return reverse_sentence # return the new sentence

# define the sentence
print(word_reverse('The quick brown fox jumps over the lazy dog'))
