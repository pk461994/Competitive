"""
Anagram. Using all exact characters in once string we can create other string
Input: s='anagram', t= 'nagaram'
Output: true

Input: s='rat', t='car'
Output: false

We can think of doing this with dictionary but time complexity is O(S+T) where S is 1st dict T is 2nd dict to match
both strings. This will lead to memory issue.
"""

class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:

        # Check the length of both strings is same
        if len(str1) != len(str2):
            return False

        # Define counter for both strings as dictionaries key will be char and value will be total number
        countStr1, countStr2 = {}, {}

        # Iterate through
        for i in range(len(str1)):
            countStr1[str1[i]] = countStr1.get(str1[i], 0) + 1
            countStr2[str2[i]] = countStr2.get(str2[i], 0) + 1

        # Check if key in string 1 equals to key in string 2
        for c in countStr1:
            if countStr1[c] != countStr2.get(c, 0):
                return False
        return True

s = Solution().isAnagram('anagram', 'nagaram')
print(s)
