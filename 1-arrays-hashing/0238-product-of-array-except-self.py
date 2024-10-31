""" 
PROBLEM:     0238. Product of Array Except Self
             https://leetcode.com/problems/product-of-array-except-self
DIFFICULTY:  Medium 
PATTERN:     Arrays
"""

class Solution:

    """
    Think prefixSum:

        nums = [1, 2, 3, 4]
        ps = [sum(nums[:i+1]) for i in range(n)]
           = [1, 1 + 2, 3 + 3, 6 + 4]
           = [1, 3, 6, 10]

    Trace productExceptSelf:

        nums    = [1, 2, 3, 4]
        nums[0] = () * (2*3*4)
        nums[1] = (1) * (3*4)
        nums[2] = (1*2) * (4)
        nums[3] = (1*2*3) * ()

        L -> R: 1, 1, 2, 6 
        R -> L: 24, 12, 4, 1

        productExceptSelf = [24, 12, 8, 6]

    The solution requires to iterate the input array from left and right, 
    and then multiplying value at current index with value on the left/right.

    The previous value on the first iteration for either left/right defaults to
    1 since there isn't a previous position for that index.
    
        L -> R: 1, 1, 2, 6 
        R -> L: 24, 12, 4, 1
                24, 12, 8, 6
    """

    # SECOND SOLUTION (OPTIMISED)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        r = 1
        for j in range(n-1, -1, -1):
            result[j] *= r 
            r *= nums[j]
            
        return result

    # FIRST SOLUTION
    def _productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left, right = [1] * n, [1] * n 

        for i in range(0, n):
            if i == 0:
                continue

            j = (n - 1) - i
            left[i] = left[i - 1] * nums[i - 1] 
            right[j] = right[j + 1] * nums[j + 1]

        return [left[k] * right[k] for k in range(n)]