from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([5, 4, -1, 7, 8]))
print(Solution().maxSubArray([1]))

'''
We can solve this problem in one pass by creating a current sum variable and adding each number to it. If the current
sum is negative before we add the next number, we start the current sum over at 0. In each iteration, we check the 
max() between the max subarray which was set to the first num initially, to the current sum that we are calculating.
'''

# Time Complexity: O(n)
# Space Complexity: O(1)

# Steps to solve

# Initialze var for maxSubarray = first num, cant be 0. current Sum = 0
# Loop through nums
# if current sum is a negative num, ignore prefix up to that point and set current sum to 0 again
# add current num to current sum
# use max() on maxsub and currentsum to keep track of current maxsubarray
# return maxsub after loop
