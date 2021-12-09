class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        for char in s:
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 1
        for char in t:
            if char in map2:
                map2[char] += 1
            else:
                map2[char] = 1

        return map1 == map2


'''
We can use the dictionary data structure and make the key each character of the string and the value each occurrence
We do this for both strings and compare them. If equal, they are valid anagrams.
'''

# Time Complexity: O(s+t)
# Space Complexity: O(n)

# Steps to solve

# Initialize two empty dictionaries
# Loop through first string. Add char as key and occurrence as val
# Repeat for second string
# Return their comparison
