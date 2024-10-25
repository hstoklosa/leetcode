class Solution:

    """

    OPTIMISED SOLUTION
      Better space utilisation by transforming the input straight 
      into a string instead of using a list as an intermediary.
    
    """
    def isPalindrome(self, s: str) -> bool:
        s, ns = s.lower(), ''
        i, j = 0, len(s) - 1
        while i < len(s):
            if s[i].isalnum(): 
                ns += s[i]
                
            i += 1

        i, j = 0, len(ns) - 1
        while i < j:
            if ns[i] != ns[j]:
                return False
            
            i += 1
            j -= 1
            
        return True

    def isPalindrome2(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower() 
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
            
        return True
