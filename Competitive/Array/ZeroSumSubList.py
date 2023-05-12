"""
Given an integer array, check if it contains a subarray having zero-sum.
Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
Output: Subarray with zero-sum exists
The subarrays with a sum of 0 are:
{ 3, 4, -7 }
{ 4, -7, 3 }
{ -7, 3, 1, 3 }
{ 3, 1, -4 }
{ 3, 1, 3, 1, -4, -2, -2 }
{ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
"""


def has_zero_sum_sub_list(nums):
    # create an empty set to store the sum of elements of each
    # sublist `nums[0…i]`, where `0 <= i < len(nums)`
    s = set()

    # insert 0 into the set to handle the case when sublist with
    # zero-sum starts from index 0
    s.add(0)

    total = 0

    for i in nums:
        total += i

        if total in s:
            return True
        s.add(total)
    return False


if __name__ == '__main__':

    nums = [4, -6, 3, -1, 4, 2, 7]

    if has_zero_sum_sub_list(nums):
        print('Sublist exists')
    else:
        print('Sublist does not exist')
