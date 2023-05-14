"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4] Output: [24,12,8,6]
For 1, it'll be 2*3*4=24, for 2- 1*3*4=12, for 3- 1*2*4=8, for 4- 1*2*3=6
Example 2:
Input: nums = [-1,1,0,-3,3] Output: [0,0,9,0,0]
"""


class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        # Create res output array. Give each position an initial value of 1 and want this to
        # be length of the input array
        # So we can multiply by the length of the nums.
        res = [1] * (len(nums))

        prefix = 1  # Assign the prefix as 1 as before 1st element there will not be anything present

        for i in range(len(nums)):
            # For each position in out res output array i we'll take the prefix and just put it in that position i
            res[i] = prefix

            # Then take input array value nums[i] and multiply it by whatever the prefix happens to be
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

s = Solution().product_except_self([1,2,3,4])
print(s)
