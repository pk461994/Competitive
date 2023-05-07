"""
Given an array of integers that is already sorted in ascending order, find the two numbers
such that they add up to specific target number.
Function twoSum should return indices of the two numbers such that they add up to target,
where index1 must be less than index2

Input: [1,3,4,5,7,10,11] Target: 9

We'll keep 2 pointers one left and right. If the sum of left+right > target we'll shift right pointer to left once
If left+right < target, we'll shift left pointer to right and then add left and right pointer
Time complexity will be O(n)
"""

class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:               # If curSum is equal to target
                print(f'The numbers add up to target are: [{numbers[left]}, {numbers[right]}]')
                return [left, right]
        return []

s = Solution().twoSum([1,3,4,5,7,10,11], 8)
print(s)
