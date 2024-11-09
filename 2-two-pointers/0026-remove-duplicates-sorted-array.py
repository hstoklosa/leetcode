""" 
DIFFICULTY:  Easy
PROBLEM:     0026. Remove Duplicates from Sorted Array
             https://leetcode.com/problems/remove-duplicates-from-sorted-array
PATTERN:     Array, Two Pointers
"""

class Solution:

    """
    Some steps:
      1. j keeps track where unique value should be placed
      2. compare current value i with previous value i-1, which 
         says whether we're dealing with a new unique value
      3. if i == i-1 then the iteration continues
      4. if i != i-1 then it will overwrite the duplicate

    Example:
    
        i,j                   j    i                   
      0, 0, 1, 1, 1, 2 -> 0, [0], [1], 1, 1, 2 

                                           j  i
      --> n[j] = n[i]; j++; i++ -> 0, [1], 1, 1, 1, 2

            j     i             j     i               j          i
      0, 1, 1, 1, 1, 2 -> 0, 1, 1, 1, 1, 2 --> 0, 1, [1], 1, 1, [2]

                                              j        i
      --> n[j] = n[i]; j++; i++ -> 0, 1, [2], 1, 1, 2 
    """

    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i, j = 1, 1

        while i < n:
            if nums[i-1] != nums[i]:
                nums[j] = nums[i]
                j += 1

            i+=1

        return len(nums)