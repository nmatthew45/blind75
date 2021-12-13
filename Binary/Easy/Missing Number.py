from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)


print(Solution().missingNumber([3, 0, 1]))
print(Solution2().missingNumber([3, 0, 1]))

'''
Take the gauss's formula sum of the length of the array and subtract it by the sum of the array to find the missing 
number.
'''
