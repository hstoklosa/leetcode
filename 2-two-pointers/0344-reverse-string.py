""" 
DIFFICULTY:  Easy
PROBLEM:     0344. Reverse String
             https://leetcode.com/problems/reverse-string
PATTERN:     Array, Two Pointers
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        i, j = 0, len(s) - 1

        while i < j:
            tmp = s[i]
            s[i], s[j] = s[j], tmp
            i, j = i + 1, j - 1