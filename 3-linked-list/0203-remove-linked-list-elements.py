""" 
DIFFICULTY:  Easy
PROBLEM:     0203. Remove Linked List Elements
             https://leetcode.com/problems/remove-linked-list-elements
PATTERN:     Linked List, Sentinel Node
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    # OPTIMISED SOLUTION USING DUMMY NODES
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
    
    def _removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        curr, prv = head, None

        while curr:
            if curr is None or curr.val != val:
                prv, curr = curr, curr.next
                continue
                
            nxt = curr.next
                
            if prv:
                prv.next = nxt
                curr.next = None
                curr = prv

            if not prv and nxt:
                curr.next = None
                head = curr = nxt

            if not prv and not nxt:
                curr = head = None

        return head