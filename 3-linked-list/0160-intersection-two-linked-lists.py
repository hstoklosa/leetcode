""" 
DIFFICULTY:  Easy
PROBLEM:     0160. Intersection of Two Linked Lists
             https://leetcode.com/problems/intersection-of-two-linked-lists
PATTERN:     Linked List
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        _set = set()
        
        m = headA
        while m:
            _set.add(m)
            m = m.next

        n = headB
        while n:
            if n in _set:
                return n
            
            n = n.next

        return None