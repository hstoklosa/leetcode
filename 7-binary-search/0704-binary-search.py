""" 
DIFFICULTY:  Easy
PROBLEM:     0704. Binary Search
             https://leetcode.com/problems/binary-search
PATTERN:     Array, Binary Search
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            middle = nums[mid]

            if middle == target:
                return mid

            if middle > target:
                hi = mid - 1

            if middle < target:
                lo = mid + 1

        return -1