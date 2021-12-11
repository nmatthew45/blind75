from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for x, y in enumerate(nums):
            diff = target - y
            if diff not in hmap:
                hmap[y] = x
            else:
                return [hmap[diff], x]


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))

'''
We know if a pair in the list adds up to target if (target - one of those numbers) = the other number
ie. if target = 9 and num[0] = 2, other num = 7. So, check if 7 exists and return their indices
'''

# Time Complexity: O(n)
# Space Complexity: O(n)

# Steps to solve

# Create empty dictionary to store seen values and indexes
# Enumerate nums in order to make a list of tuples containing values and indices
# Calculate diff by subtracting target integer by current val in nums
# Check if diff exists in dictionary
# If it does not exist, add diff + it's index to dictionary
# If it exists, return index of diff located in dictionary and index of current value in nums
