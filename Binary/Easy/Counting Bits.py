from typing import List


# O(n^2) solution
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for curNum in range(n + 1):
            numOnes = 0
            while curNum:
                if curNum % 2 == 1:
                    numOnes += 1
                curNum = curNum >> 1
            res.append(numOnes)
        return res


# Time Complexity: O(n^2)
# Space Complexity: O(1)


'''
We initialize the result list that we will return at the end. We iterate through a loop n+1 times. We create a counter
variable to keep track of how many 1's appear in the binary representation of the current num.
'''


# O(n) solution (Dynamic Programming)
class Solution2:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

# Time Complexity: O(n)
# Space Complexity: O(n)
