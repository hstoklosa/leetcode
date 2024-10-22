from typing import List

class Solution:
    
    # Time-Efficient Solution (0ms, Beats 100.00%)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = dict()

        for i, v in enumerate(nums):
            jv = target - v

            if jv in numsMap:
                return [i, numsMap[jv]]

            numsMap.update({v:i})
        
    # Space-Efficient Solution
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if (nums[i] + nums[j] == target and i != j):
                    return [i, j]

print(Solution.twoSum([2,7,11,15], 9))
print(Solution.twoSum2([2,7,11,15], 9))

