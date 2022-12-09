# Given two strings s and t, return true if s is an anagram of t, else false

# Constraints:
# s and t consist of lowercase English letters

# There are several solutions. We can trade space for time and vv
import collections
class Solution:
    # One method is to use two hashmaps to store the frequency of each letter
    def isAnagram(self, s:str, t:str) -> bool:
        # If the lengths are not equal it is not an anagram
        if len(s) != len(t):
            return False

        smap, tmap = collections.defaultdict(int), collections.defaultdict(int)

        # Iterate over s and t and count letters
        for c in s:
            smap[c] += 1
        for c in t:
            tmap[c] += 1

        # We have to iterate one more time to check if the maps are equal
        for c in smap:
            if smap[c] != tmap[c]:
                return False
        return True
    # We are iterating over both strings 1-2 times and creating two hashmaps
    # Time complexity is O(n) and space is O(n)

    # Maybe we can save a bit of time and space by using a single hashmap
    def isAnagram2(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False

        cmap = collections.defaultdict(int)

        # Iterate over s and count letters
        for c in s:
            cmap[c] += 1
        
        # Iterate over t and count backwards
        for c in t:
            cmap[c] -= 1

            # If letter is not in s, return False
            if cmap[c] < 0:
                return False

        return True
        # We pass over each string max 1 time and use 1 hashmap
        # Time complexity is O(n) and space is O(n)

    # We can trade time for extra space by sorting
    def isAnagram3(self, s:str, t:str) -> bool:

        return sorted(s) == sorted(t)
    # Sorting each string is slower but additional space is constant
    # Time complexity is O(nlogn) and space is O(1)