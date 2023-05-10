"""
Given an unsorted integer array, find a pair with the given sum in it.

Input:
nums = [8, 7, 2, 5, 3, 1]
target = 10 
Output:
Pair found (8, 2)
or
Pair found (7, 3)

Input:
nums = [5, 2, 6, 8, 1, 9]
target = 12
Output: Pair not found
"""

def findPair(nums, target):
    d = {}

    for i, val in enumerate(nums):
        # check if pair (e, target - e) exists

        # if the difference is seen before, print the pair
        if target-val in d:
            print(d.get(target - val))
            print(f'Pair found', (nums[d.get(target-val)], nums[i]))
            return
        # store index of the current element in the dictionary
        d[val] = i
    print('Pair not found')


if __name__ == '__main__':
    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    findPair(nums, target)
