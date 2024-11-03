""" 
PROBLEM:     0268. Missing Number
             https://leetcode.com/problems/missing-number
DIFFICULTY:  Easy
PATTERN:     Arrays, Bit Manipulation
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums = sorted(nums)
        n = len(nums)

        if nums[0] != 0: return 0
        if nums[n-1] != n: return n

        for i in range(1, n):
            if nums[i-1] != nums[i] - 1:
                return nums[i] - 1 

        return n