from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenVals = set()
        for num in nums:
            if num in seenVals:
                return True
            else:
                seenVals.add(num)
        return False


print(Solution().containsDuplicate([1, 2, 3, 1]))
print(Solution().containsDuplicate([1, 2, 3, 4]))
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

'''
We can solve this problem in one pass by creating an empty set and checking each value in the list if it appears in the
set. If it does not, we add it to the set and keep checking. We use a set because sets 
'''

# Time Complexity: O(n)
# Space Complexity: O(n)

# Steps to solve

# Initialize an empty set
# Iterate through list of nums
# If current num is in the set, duplicate found. return True
# If current num is not in the set, add it to the set
# If current num is never found in set, no duplicates found. return False.
