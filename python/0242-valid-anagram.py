class Solution(object):
    def isAnagram(self, s, t):
        return True if (sorted(s) == sorted(t)) else False 
