from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        maxP = 0
        for price in prices:
            if price < minP:
                minP = price
            elif (price - minP) > maxP:
                maxP = price - minP
        return maxP


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))

'''
We can just iterate through the list in one pass while constantly setting the new minimum price and 
calculating + keeping track of the max profit in each iteration. We return the max profit at the end of the loop.
'''

# Steps to solve
# Initialize min price and max profit
# Loop through list of prices while comparing current price.
# Update minimum price if current price is lower than what we had in the last iteration
# Calculate max profit and update if current max profit is higher than what we had in the last iteration
# Return max profit at the end of the loop
