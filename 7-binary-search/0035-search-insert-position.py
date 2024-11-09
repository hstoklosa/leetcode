""" 
DIFFICULTY:  Easy
PROBLEM:     0035. Search Insert Position
             https://leetcode.com/problems/search-insert-position
PATTERN:     Binary Search
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            
            if mid_value > target:
                hi = mid - 1

            if mid_value < target:
                lo = mid + 1
    
            
        return lo