""" 
PROBLEM:     0070. Climbing Stairs
             https://leetcode.com/problems/climbing-stairs
DIFFICULTY:  Easy
PATTERN:     Dynamic Programming
"""

class Solution:

    """
    Dynamic programming is a name given to a class of algorithms which remember solutions to previously computed subproblems in order to increase efficiency.

    https://www.hello-algo.com/en/chapter_dynamic_programming/intro_to_dynamic_programming
    https://cp-algorithms.com/dynamic_programming/intro-to-dp.html
    https://en.wikipedia.org/wiki/Dynamic_programming
    """

    def climbStairs(self, n: int) -> int:
        memo = dict()

        def helper(n: int) -> int:
            if n <= 1:
                return 1
        
            if n not in memo:
                memo[n] = helper(n - 1) + helper(n - 2)

            return memo[n]

        return helper(n)