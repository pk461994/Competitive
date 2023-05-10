"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

class Solution:
    def pivotIndex(self, nums):

        # Initialize leftSum & rightSum to store the sum of all the numbers strictly to the index's left & right respectively...
        leftsum, rightsum = 0, sum(nums)

        # Traverse elements through the loop...
        for i, val in enumerate(nums):
            rightsum -= val

            # If the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right...
            if leftsum == rightsum:
                return i        # Return the pivot index...
            leftsum += val
        return -1       # If there is no index that satisfies the conditions in the problem statement...
        
res = Solution().pivotIndex([1,7,3,6,5,6])
print(res)