class Solution:
    def isAnagram(s: str, t: str) -> bool:
        s, t = sorted(s), sorted(t)
        return True if s == t else False