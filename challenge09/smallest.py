
# define the function
def second_smallest(numbers):
    # transform the array into an unordered list, then sort that list
    # [implied that it is sorted based on value]
    sorted_nums = sorted(set(numbers))

    # then return the second element in the unordered list
    # [which has been ordered by the sorted function]
    return sorted_nums[1]

# execute the function
print(second_smallest([29, 11, 13, 89, 42]))