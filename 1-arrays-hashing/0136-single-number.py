""" 
PROBLEM:     0136. Single Number
             https://leetcode.com/problems/single-number
DIFFICULTY:  Easy
PATTERN:     Arrays, Bit Manipulation
"""

class Solution:

    """
    XOR Properties:
      1. Commutative:       a^b = b^a
      2. Associative:       a^(b^c) = (a^b)^c
      3. Identity element:  a^0 = a
      4. Self-inverse:      a^a = 0

    References:
      - https://leetcode.com/discuss/interview-question/3695233
      - https://en.wikipedia.org/wiki/Exclusive_or#Computer_science
    """

    def singleNumber(self, nums: list[int]) -> int:
        n, num = len(nums), nums[0]

        for i in range(1, n): 
            num ^= nums[i]
             
        return num
