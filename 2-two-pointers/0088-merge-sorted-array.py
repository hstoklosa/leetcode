""" 
DIFFICULTY:  Easy
PROBLEM:     0088. Merge Sorted Array
             https://leetcode.com/problems/merge-sorted-array
PATTERN:     Array, Two Pointers
"""

class Solution:

    """
    Notes: 
      - shifting elements e.g., [1,2,0,0] -> [1,2,0,0] can easily 
        cause overwriting values incorrectly
      - consider space the extra space in the array to avoid shifting
      - still requires pointers in the array, but way more manageable

    Logic:
      1. compare elements from the end of both arrays
      2. take the larger element and place it at the end of nums1
      3. move the corresponding pointer backwards
      4. continue until all all elements from nums2 are processes
    
    Example:
    
          m     l       n              l       n
      [1, 2, 0, 0], [2, 3]  ->  [1, 2, 0, 4], [3, 4] 
      
             m     l    n              m  l       n
      -> [1, 2, 0, 4], [3, 4]  ->  [1, 2, 3, 4], [3, 4]

    """

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last = m + n - 1
        m, n = m - 1, n - 1

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            
            last -= 1