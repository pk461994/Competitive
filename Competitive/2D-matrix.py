'''
Algo to search for value in an m x m matrix. Matrix is
1- Integers in each row are sorted from left to right
2- The 1st integer of each row is greater than the last integer of the previous row

Input = [[1,3,5,7], [10,11,16,20], [23,30,34,60]], target = 3
Output = true
'''

class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1
        while top <= bot:
            row = (top + bot) // 2    # To get middle row for binary search
            if target > matrix[row][-1]:    # To check if the target is greater than the largest value in this row
                top = row + 1
            elif target < matrix[row][0]:   # To check if the target is smaller than the smallest value in this row
                bot = row - 1
            else:                           # Target falls within this current row
                break
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        left, right = 0, COLS - 1
        while left <= right:
            middle = (left+right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        return False

matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
target = 3
res = Solution().searchMatrix(matrix, target)
print(res)
