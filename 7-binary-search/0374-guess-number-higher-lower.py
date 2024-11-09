""" 
DIFFICULTY:  Easy
PROBLEM:     0374. Guess Number Higher or Lower
             https://leetcode.com/problems/guess-number-higher-or-lower
PATTERN:     Binary Search
"""

def guess(num: int) -> int:
    """
    @param num, your guess
    @return -1 if num is higher than the picked number
             1 if num is lower than the picked number
             otherwise return 0
    """
    return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        
        while lo <= hi:
            mid = (lo+hi) // 2
            res = guess(mid)

            if res == -1:
                hi = mid - 1
            elif res == 1:
                lo = mid + 1
            else: 
                return mid
        
