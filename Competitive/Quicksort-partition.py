'''
Given array of nums with n objects colored red, white or blue, sort them in place so that objects of the same color
are adjacent, with the colors in the order red, white and blue
We'll use the color 0,1,2 to represent the color red, white and blue

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

class Solution:
    def sortColors(self, nums):
        left, right = 0, len(nums)-1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1

            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1
            i += 1
        return nums

s = Solution().sortColors([2, 0, 2, 1, 1, 0])
print(s)
