from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([4, 3, 2, 1, 4]))
print(Solution().maxArea([1, 2, 1]))

# Time Complexity: O(n)
# Space Complexity: O(n)


'''
We can solve this in one pass by keeping hold of a left and right pointer. We initialize a result variable. In each 
iteration, we compute the area of the "container of water" using length x width. length = right ptr - left pointer.
width = min(height[l], height[r]. If we use max, the water would spill over the shorter end. We increment the pointer
based on which side is shorter in case the next value ends up being greater/taller. Continue while left ptr < right ptr.
Return result at the end.
'''
