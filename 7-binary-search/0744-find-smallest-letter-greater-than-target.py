""" 
DIFFICULTY:  Easy
PROBLEM:     0744. Find Smallest Letter Greater Than Target
             https://leetcode.com/problems/find-smallest-letter-greater-than-target
PATTERN:     Array, Binary Search
"""

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        lo, hi = 0, len(letters) - 1
        
        if target >= letters[hi]:
            return letters[lo]

        while lo <= hi:
            mid = (lo + hi) // 2
            let = letters[mid]

            # Comparing chars == comparing ord(...)s
            if let <= target:
                lo = mid + 1 
            else:
                hi = mid - 1

        return letters[lo]
    
t1 = Solution.nextGreatestLetter(Solution, ["c", "f", "j"], "a"); print(t1)
t2 = Solution.nextGreatestLetter(Solution, ["c", "f", "j"], "c"); print(t2)
t3 = Solution.nextGreatestLetter(Solution, ["x", "x", "y", "y"], "z"); print(t3)