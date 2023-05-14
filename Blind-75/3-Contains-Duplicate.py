"""
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct

Input: nums=[1,2,3,1] Output: true
Input: nums=[1,2,3,4] Output: false
Input: nums=[1,1,1,3,3,4,3,2,4,2] Output: true
"""


class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        # Create a set
        hashset = set()

        for val in nums:
            if val in hashset:
                return True
            hashset.add(val)
        return False

s= Solution().contains_duplicate([1,2,3,1])
print(s)
