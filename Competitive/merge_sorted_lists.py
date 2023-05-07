"""
Given 2 sorted arrays num1 and num2 merge num2 into num1 as one sorted array
input:
num1 = [1,2,3,0,0,0], m = 3
num2 = [2,5,6], n = 3
output: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, num1: list[int], m: int, num2: list[int], n: int) -> list[int]:
        """
        m is index of last value in nums1 n is index of last value in nums2
        First we will Get the last index of num1
        """
        last = m + n - 1

        # Merge them in reverse order, we'll keep going while there are elements left in both arrays
        while m > 0 and n > 0:
            if num1[m - 1] > num2[n - 1]:
                num1[last] = num1[m - 1]
                m -= 1
            else:
                num1[last] = num2[n - 1]
                n -= 1
            last -= 1

        # Fill num1 with leftover num2 elements
        while n > 0:
            num1[last] = num2[n - 1]
            n, last = n-1, last-1
        return num1

res = Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(res)
