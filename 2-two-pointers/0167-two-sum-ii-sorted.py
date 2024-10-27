""" 
PROBLEM:     0167. Two Sum II - Input Array Is Sorted [MEDIUM]
             https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
DIFFICULTY:  Medium 
PATTERN:     Two Pointers
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lo, hi = 0, len(numbers) - 1

        while lo <= hi:
            curr_sum = numbers[lo] + numbers[hi]
            
            if curr_sum < target:
                lo = lo + 1
            if curr_sum > target:
                hi = hi - 1
            if curr_sum == target:
                return [lo + 1, hi + 1]

        return []