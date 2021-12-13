class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

# Time Complexity: O(32)
# Space Complexity: O(1)

'''
We initialize a counter variable to keep track of how many ones there are. We go through each digit and mod it by 2
if the integer is 1, the remainder is 1 so that means a 1 exists so we can increment our counter variable. We shift the
integer right once to check the next digit. Do this for all digits and return our counter variable at the end.
'''