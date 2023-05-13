"""
Given an array of integers, return indices of the two numbers such that they add up to specific target.
Assume that each input will have exactly one solution
Given nums = [2,11,15,7], Target=9
"""


class Solution:
    def twoSum(self, nums, target):
        prev_map = {}  # Mapping the value to index of value val : index

        for index, val in enumerate(nums):
            # Check if the difference of target and value is present in prev_map dict
            diff = target - val

            if diff in prev_map:
                return [prev_map[diff], index]  # return the index of diff element and current element

            prev_map[val] = index

        return "The two sum doesn't exist"

s = Solution().twoSum([2,11,15,7], 9)
print(s)
