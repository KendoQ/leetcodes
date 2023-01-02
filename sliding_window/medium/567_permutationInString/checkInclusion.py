# Given two strings s1 and s2, return true if
# s1 is a permutation substring of s2. That is,
# if s2 contains a permutation of s1, otherwise false.

# Constraints: 1 <= len(s1) 
# len(s2) <= 10^4
# s2 and s1 consist of lowercase English letters.

# Example:
# Input: s1 = "bada", s2 = "eiidbaadaafad"
# Output: true
# Explanation: s2 contains one permutation of s1 ("baad").

# A permutation is a rearrangement of letters. then
# the substring in s2 that validates the check will
# have the same characters as s2. We can use a sliding
# window to check if the substring in s2 by comparing
# the characters. We can use and array for this, but
# since we know the characters are lowercase English
# letters, we can use a hash table instead.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, return false.
        if len(s1) > len(s2): return False

        # Use the lower case English letters as keys
        # and the number of times they appear as values.
        keys = "abcdefghijklmnopqrstuvwxyz"
        s1Count = {key: 0 for key in keys}
        s2Count = {key: 0 for key in keys}

        # Count the number of times each character appears
        # in s1 and s2.
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1

        # Check the number of times each string has
        # matching set of english letters
        matches = 0
        for k in keys:
            if s1Count[k] == s2Count[k]:
                matches += 1


        # Initialize left pointer
        L = 0

        # Loop over the right pointer
        for R in range(len(s1), len(s2)):
            # If we have a matching set, return true
            if matches == 26: return True

            # Update s2 hash add rightmost char
            s2Count[s2[R]] += 1

            # If the counts of this char match
            # add 1 to matches
            if s1Count[s2[R]] == s2Count[s2[R]]:
                matches += 1
            
            # If the counts just stopped matching
            # take away 1 from matchesl
            elif s1Count[s2[R]] == s2Count[s2[R]] - 1:
                matches -= 1

            # Update s2 hash take out left char
            s2Count[s2[L]] -= 1

            # Again update the matches count
            if s1Count[s2[L]] ==  s2Count[s2[L]]:
                matches += 1
            elif s1Count[s2[L]] == s2Count[s2[L]] + 1:
                matches -= 1

            # Remember to move left pointer
            L += 1

        # Return if permutation of s1 in s2
        return matches == 26
    # We pass over s2 one time to find a solution
    # creating two hashmaps of contstant size
    # Time: O(n), Space: O(52) => O(1)
