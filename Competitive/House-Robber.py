"""
Give a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob, You can't rob adjacent house

Input:[1,2,3,1] Output: 4
Explanation: Rob house 1 (money=1) and then rob house 3 (money=3). Total amount= 1+3 = 4
"""

class Solution:
    def rob(self, nums):
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ....]
        for n in nums:
             temp = max(n + rob1, rob2)
             rob1 = rob2
             rob2 = temp
        return rob2
s = Solution().rob([1,2,3,1])
print(s)
