"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""


class Solution(object):
    def plusOne(self, digits):
        # Adjusting an array of digits into an integer
        digits_integer = int(''.join(map(str,digits)))
        digits_integer +=1
        # Adjusting back an integer into an array of digits after plus 1
        return [int(x) for x in str(digits_integer)]
    
sol = Solution().plusOne([1,2,3])
print(sol)
