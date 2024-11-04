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

    """
    The solution has been improved by:
      1. finding the middle of the linked list and splitting it 
      2. reversing the second half for comparison with the first half
    
    Optimised version runs in O(n) time and uses O(1) space.
    """
    
    def isPalindrome(self, head: ListNode | None) -> bool:
        fast, slow = head, head
        slow_prv   = None

        # Find the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow_prv = slow
            slow = slow.next

        # Decide whether to ignore middle value
        if slow.next is not None and fast is not None:
            slow = slow.next

        # Split the list
        if slow_prv and slow_prv.next is not None:
            slow_prv.next = None

        # Reverse the 2nd half of the list   
        curr, prv = slow, None
        while curr:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt

        # Compare values in the lists
        start, mid = head, prv
        while start and mid:
            if start.val != mid.val:
                return False
            
            start = start.next
            mid = mid.next

        # Check for leftover nodes
        if start or mid:
            return False

        return True

    def _isPalindrome(self, head: ListNode | None) -> bool:
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