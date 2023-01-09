# Given a string containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if 
# the input string is valid. The brackets must
# close in the correct order, "()" and "()[]{}"
# Every close bracket must have a corresponding
# open bracket.

# Constraints:
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.

# Example:
# Input: s = "[{()}]"
# Output: true

# We can use a stack to keep track of the open
# brackets. If we encounter a close bracket, we
# pop from the stack afterchecking if the popped
# bracket matches the current bracket. We can match
# an open bracket to the proper closing bracket using
# a hashmap
class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize the stack
        stack = []

        # Initialize the hashmap
        charMap = {"}": "{", "]": "[", ")": "("}

        # Iterate over the string
        for c in s:
            # If stack is non empty and current
            # char is closing bracket
            if stack and c in charMap:
                # If the top of the stack is the 
                # correct opening bracket
                if stack[-1] == charMap[c]:
                    # Pop from the stack
                    stack.pop()

                # Otherwise the close bracket is
                # not a match with top, return false
                else:
                    return False

            # If current char is an open bracket,
            # add it to stack
            else:
                stack.append(c)

        # If the stack is empty, it was valid
        return True if not stack else False
    # We iterate over the string one time and use
    # a stack which could at worst be size of n
    # Time: O(n), Space: O(n)