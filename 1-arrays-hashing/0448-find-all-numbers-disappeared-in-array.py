""" 
DIFFICULTY:  Easy
PROBLEM:     0448. Find All Numbers Disappeared in an Array
             https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
PATTERN:     Arrays, Hash Table
"""

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        set_nums = set(nums)
        result = []

        for n in range(1, n+1):
            if n not in set_nums:
                result.append(n)

        return result