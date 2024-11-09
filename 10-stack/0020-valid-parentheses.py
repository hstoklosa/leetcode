""" 
DIFFICULTY:  Easy
PROBLEM:     0020. Valid Parentheses
             https://leetcode.com/problems/valid-parentheses
PATTERN:     Stack
"""

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = deque()
    
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                continue

            if not stack:
                return False
            
            if (char == ")" and stack[-1] == "(" or 
                char == "}" and stack[-1] == "{" or
                char == "]" and stack[-1] == "["):
                stack.pop()
            else:
                return False

        if stack:
            return False
            
        return True