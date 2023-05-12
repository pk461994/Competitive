"""
Given a non-empty integer array, find the index of the maximum occurring element with an equal probability.
For example, consider the input: [4, 3, 6, 8, 4, 6, 2, 4, 5, 9, 7, 4]
The maximum occurring element, 4, occurs at index 0, 4, 7, and 11.
The solution should return any one of these indices with an equal probability.
If there are two maximum occurring elements in the array, the solution should
consider the first occurring maximum element.
"""


import random


def max_index_ele(arr):
    max_count = 0
    max_index = []

    # Find the maximum occurring element and its count
    count_dict = {}
    for i, num in enumerate(arr):
        if num not in count_dict:
            count_dict[num] = 0
        count_dict[num] += 1

        if count_dict[num] > max_count:
            max_count = count_dict[num]
            max_index = [i]
        elif count_dict[num] == max_count:
            max_index.append(i)

    # Randomly choose an index from the maximum occurring elements
    return random.choice(max_index)

array = [4, 3, 6, 8, 4, 6, 2, 4, 5, 9, 7, 4]
index = max_index_ele(array)
print(f"The index of the maximum occurring element is: {index}")
