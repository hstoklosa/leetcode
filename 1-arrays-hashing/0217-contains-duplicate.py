from typing import List

class Solution:

    def containsDuplicate(nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                return True

        return False

    def containsDuplicate2(nums: List[int]) -> bool:
        numsSet = set()

        for n in nums:
            if (n in numsSet):
                return True
            
            numsSet.add(n)

        return False