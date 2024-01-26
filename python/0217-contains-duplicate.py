class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        
        for idx, number in enumerate(nums):
            if (idx == len(nums) - 1):
                continue
                
            if (number == nums[idx + 1]):
                return True
            
        return False
