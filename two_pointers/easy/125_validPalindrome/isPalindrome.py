# A phrase is a palindrome if, after converting all uppercase
# letters into lowercase letters and removing all 
# non-alphanumeric characters, it reads the same forward and
# backward. Alphanumeric characters include letters and numbers.

# Given a string s, return True if it is a palindrome, else False.

# Example
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Constraints:
# 1 <= len(s) <= 2E5

# The intuitive solution is to remove non alpha nums and
# compare the string to its reverse, however, in some
# environments reversing the string may not be optimal, so
# we consider the two-pointer solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Place left and right pointers
        left, right = 0, len(s) - 1

        # Move the pointers toward the other, stop if they meet
        while left < right:

            # Skip non alpanums by moving pointers
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare chars and return false if not isPalindrome
            if s[left].lower() != s[right].lower():
                return False

            # Move pointers toward each other
            left += 1
            right -= 1

        return True 
    # We pass over string one time and use 2 pointers
    # Time complexity: O(n)
    # Space complexits: O(1)