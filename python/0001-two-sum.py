class Solution(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def twoSum(self, nums, target):
        numIdxMap = {}

        for i in range(len(nums)):
            
            if (target - nums[i] in numIdxMap):
                return [numIdxMap[target - nums[i]], i]

            numIdxMap[nums[i]] = i

        return []
