"""
Given an array of integers, return indices of the two numbers such that they add up to specific target.
Assume that each input will have exactly one solution
Given nums = [2,7,11,15], Target=9
"""

class Solution:
    def twoSum(self, nums, target):
        prevMap = {}     # val: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i  # To check if num is not in prevMap add the num
        return

s = Solution().twoSum([2,11,15,7], 9)
print(s)
