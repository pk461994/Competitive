"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much 
as every other number in the array. If it is, return the index of the largest element, 
or return -1 otherwise.

Input: nums = [3,6,1,0]
Output: 1
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
"""


class Solution:
    def twice_large(self, nums):

        a = sorted(nums)

        if a[-1]>=a[-2]*2:

            return nums.index(a[-1])
        else: return -1

sol = Solution().twice_large([3,6,1,0])
print(sol)
