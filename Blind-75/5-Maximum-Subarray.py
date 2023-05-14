"""
Given an integer array nums, find the
subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4] Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1] Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8] Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""


class Solution:
    def max_sub_array(self, nums: list[int]) -> int:
        max_subarray = nums[0]   # Assign to first element

        cur_sum = 0     # Initialize current sum as 0

        for val in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += val
            max_subarray = max(max_subarray, cur_sum)
        return max_subarray

s = Solution().max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
print(s)
