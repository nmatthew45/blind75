class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in valid:
                if stack and stack[-1] == valid[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


print(Solution().isValid('()'))
print(Solution().isValid('[(])'))
print(Solution().isValid('('))

'''
We can use a stack data structure implemented using a list to append each character in the input string.
We check each current character to see if it is a closing character and if its matching pair is at the top of the stack.
If they match, we can pop the top of the stack, if not keep appending. 
'''

# Time Complexity: O(n)
# Space Complexity: O(n)

# Steps to solve

# Initialize dictionary of closing/opening pairs and an empty stack
# Check for each character, if character is a key in the dictionary, if stack is not empty and top of the stack
# is equal to the key's value in the dictionary, pop the top of the stack
# If stack = empty and current char is a closing symbol of the pair, return False b/c only char cannot be a closing sym
# If char not in dictionary, append it to stack
# After loop, if stack = empty, return True, else False
