class Solution(object):

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while (left < right):
            if left < right and not s[left].isalnum():
                left += 1
                continue

            if right > left and not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False 

            left += 1
            right -= 1
                
        return True
