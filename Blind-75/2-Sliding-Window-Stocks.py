"""
Say you have an array for which the ith element is the price of a given stock on day i
If you were only permitted to complete at most one transaction(i.e, buy one stock and sell one share of the stock),
design an algorithm to find the maximum profit.
Note, You cannot sell a stock before you buy one

Input: [7,1,5,3,6,4] Output: 5
Explanation: Buy on day2(price=1) and sell on day5(price=6), profit=6-1=5. Not 7-1=6,
as selling price needs to be larger than buying price

We will use Two pointers, left and right. We will assign left to 0th and right to 1st index
and search for minimum price initially. Then shift the right pointer until we get the highest price
If right pointer is lesser than left pointer we will assign the right pointer to the left pointer
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1  # left=buy and right=sell
        max_profit = 0      # Define maximum profit as 0

        while right < len(prices):
            # Check if profitable transaction?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]  # Get the profit

                # Check the max of the current max_profit and the profit we computed above and assign to max_profit
                max_profit = max(max_profit, profit)
            else:       # If not a profitable transaction, assign left to right pointer
                left = right
            right += 1  # Regardless of the conditions we need to update right pointer
        return max_profit

s = Solution().maxProfit([7,1,5,3,6,4])
print(s)
