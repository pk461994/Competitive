"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum

Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4, -2, 2, 1] has the largest sum=6

We'll take one subarray and add to make curSum then we just need to add next element to curSum. O(n2)
Better approach is that negative numbers don't contribute in sum, so we can ignore that value
Like we ignore -2. Then 1+ -3 = -2. Again we can ignore that. If the prefix is negative we will ignore
If positive we'll continue the operation
"""

class Solution:
    def maxSubArray(self, nums):
        maxSub = nums[0]  # Initialize max sub-array to the 1st value in array
        curSum = 0

        for n in nums:
            if curSum < 0:   # If current sum is negative or less than 0, reset curSum to 0
                curSum = 0
            curSum += n     # If not negative add to curSum(always computing the max)
            maxSub = max(maxSub, curSum)    # Always compute max of itself maxSub and curSum, the sum we computed
        return maxSub

s = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(s)
