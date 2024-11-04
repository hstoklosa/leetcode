""" 
DIFFICULTY:  Easy
PROBLEM:     0234. Palindrome Linked List
             https://leetcode.com/problems/palindrome-linked-list
PATTERN:     Two Pointers (Fast & Slow)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        stack = list()
        fast, slow = head, head

        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next 

        if fast is not None:
            slow = slow.next
 
        while slow is not None:
            if slow.val != stack.pop():
                return False
            
            slow = slow.next
        
        return True