"""
Given an integer array, find the minimum index of a repeating element
in linear time and doing just a single traversal of the array.

Input:  [5, 6, 3, 4, 3, 6, 4]
Output: The minimum index of the repeating element is 1
Input:  [1, 2, 3, 4, 5, 6]
Output: Invalid Input
"""


def find_min_index(nums):
    s = set()

    for i in nums:
        if i in s:
            print(nums.index(i))
            return

        else:
            s.add(i)

find_min_index([5, 6, 3, 4, 3, 6, 4])
