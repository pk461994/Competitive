"""
You're climbing a staircase. Takes n steps to reach the top
Each time you can either climb 1 or 2 steps.
How many distinct ways you can climb to the top.

Input: n=2, Output: 2

Explaination: There are two ways to climb to the top:
1. 1 step + 1 step 
2. 2 steps
"""

class Solution:
    def climbStairs(self, n:int):
        one, two = 1, 1

        for i in range(n - 1):
            temp = one # Store value of one
            one = one + two  # We're adding two previous values to get new result
            two = temp
        
        return one

res = Solution().climbStairs(5)
print(res)
