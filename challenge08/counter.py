
# define the function
def string_sorter(strings):
    # utilzing the sorted() function in order to rank
    # each string by its length
    return sorted(strings, key=len)

# define the variable passed in and return value
print(string_sorter(['dog', 'kitten', 'elephant', 'horse', 'penguin']))