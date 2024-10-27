""" 
PROBLEM:     0015. 3Sum
             https://leetcode.com/problems/3sum
DIFFICULTY:  Medium 
PATTERN:     Two Pointers
"""

class Solution:

    """
    In a sorted version: the previous numbers cannot be in the triplet.

        numbers = = sorted([-1, 0, 1, 2, -1, -4]) = [-4, -1, -1, 0, 1, 2]

    For number at index i, only the partition nums[i...n-1] matters.

    Fixing x: find k such that sum(x, k) = 0 by inverting x i.e., -x,
              making nums[i+1...n-1] the partition of interest.

    nums[i+1...n-1] will be checked for the 2 numbers that add up to k.

    For example:

        x = nums[1] = -1, target = 1

    Then, search for 2 numbers in range nums[2...4] that add up to target (1).
    
        -4, -1, [-1, 0, 1, 2]

        -4, -1, [-1, [0], [1], 2]

           0         1
        nums[3] + nums[4] = 1 (target)

          -1         0         1
        nums[1] + nums[3] + nums[4] = 0 (valid triplet)
                    
    After fixing a single value, we end up with the 0167-two-sum problem. 
    """

    def threeSum(self, nums: list[int]) -> list[list[int]]:  
        nums.sort()

        n   = len(nums)
        res = []
        i   = 0

        while i < n - 1:
            vi     = nums[i]
            target = -vi
            j, k   = i + 1, n - 1

            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue  

            # modified 0167-two-sum
            while j < k:
                vj, vk   = nums[j], nums[k]
                curr_sum = vj + vk
                
                if curr_sum < target:
                    j = j + 1
                elif curr_sum > target:
                    k = k - 1
                else:
                    res.append([vi, vj, vk])

                    # skip duplicates on j, k pointers
                    while j < k and nums[j] == nums[j+1]:
                        j += 1  
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1  

                    # move pointers after finding a triplet
                    j += 1
                    k -= 1
    
            i += 1
   
        return res