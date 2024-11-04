""" 
DIFFICULTY:  Easy
PROBLEM:     0083. Remove Duplicates from Sorted List
             https://leetcode.com/problems/remove-duplicates-from-sorted-list
PATTERN:     Linked List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head