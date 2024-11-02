""" 
PROBLEM:     0128. Longest Consecutive Sequence
             https://leetcode.com/problems/longest-consecutive-sequence
DIFFICULTY:  Medium 
PATTERN:     Arrays, Hashing (Set)
"""

class Solution:

    # Example test case: [100, 4, 200, 1, 3, 2, 50, 5]
    # 
    # Edge cases:
    #   1. reveresed seq: [1, 0, -1]
    #   2. single item: [0]

    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums)
        max_seq = 0

        for n in numbers:
            prv = n - 1

            if prv in numbers:
                continue

            nxt = n + 1
            curr_seq = 1

            while nxt in numbers:
                curr_seq += 1
                nxt += 1

            if curr_seq > max_seq:
                max_seq = curr_seq

        return max_seq