""" 
DIFFICULTY:  Medium
PROBLEM:     2487. Remove Nodes From Linked List
             https://leetcode.com/problems/remove-nodes-from-linked-list
PATTERN:     Linked List, Sentinel Node
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        curr, prev = head, None
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        last = prev
        curr, _max = last, last.val
        while curr.next:
            if curr.next.val >= _max:
                _max = curr.next.val
                curr = curr.next
            else:
                curr.next = curr.next.next

        curr, prev = last, None
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        return prev