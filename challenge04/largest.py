
# define the function
def largest(all_numbers):
    # init the placeholder
    greatest_value = all_numbers[0]

    # iterate through all indexes/values
    for num in all_numbers:
        if num > greatest_value:
            greatest_value = num

    # return the results
    return greatest_value

# define values
all_values = [1, 4, 5, 19, 22, 2, 4, 27]
largest_num = largest(all_values)
print('The largest value: ' + str(largest_num))