# Given two string s and t of lengths m and n, return the
# minimum window in s which will contain all the characters
# in t (including duplicates). If there is no such window
# return the empty string ""

# Constraints:
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# answer is unique

# Example:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes
# 'A', 'B', and 'C' from string t.

# Tempting to attemt a brute force solution, but that would
# involve checking for every character in t each time the 
# window of s is changed in O(mn)^2 time. We can do much
# better using a slinding window technique
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Handle the edge cases first
        if len(s) < len(t) or t == "":
            return ""

        # Initialize the result. We use a left and
        # right pointer and keep track of the length
        # for convenience
        res, resLen = [-1, -1], float("infinity") #minimization

        # Initialize two hashmaps to count the characters
        # in t and in the current window of s
        win, tCount = {}, {}

        # Initialize left pointer
        L = 0

        # Count the chars in t
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        # We track the matches between window and t characters
        # We care about how many char counts match now and
        # how many we need
        have, need = 0, len(tCount) #len(t) doesn't handle duplicates

        # Iterate over s using right pointer
        for R in range(len(s)):
            # Add current char to window
            win[s[R]] = 1 + win.get(s[R], 0)

            # Update match count if char of interest
            if s[R] in t and win[s[R]] == tCount[s[R]]:
                have += 1

            # While we have all the matches we need
            while have == need:
                # Update the result
                if R - L + 1 < resLen:
                    res, resLen = [L, R], R - L + 1

                # Minimize window length
                win[s[L]] -= 1

                # Check if we lost a match
                if s[L] in tCount and win[s[L]] < tCount[s[L]]:
                    have -= 1

                # Move left pointer right
                L += 1

        # Return the updated result
        if resLen != float("infinity"):
            return s[res[0] : res[1] + 1]
        else:
            return ""
    # We pass over s and t once only and create
    # two hashmaps to count the characters
    # Time: O(m+n), Space: O(m+n)