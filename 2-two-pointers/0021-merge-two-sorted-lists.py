""" 
DIFFICULTY:  Easy
PROBLEM:     0021. Merge Two Sorted Lists
             https://leetcode.com/problems/merge-two-sorted-lists
PATTERN:     Two Pointers, Dummy Node
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        fp, sp = list1, list2

        head = ListNode(0)
        curr = head

        # Approach: node x letting
        #           node y through
        while fp and sp:
            if fp.val < sp.val:                
                curr.next = fp
                fp = fp.next
            else:
                curr.next = sp
                sp = sp.next

            curr = curr.next

        # attach remaining nodes
        if fp: curr.next = fp
        if sp: curr.next = sp

        return head.next # skip dummy node