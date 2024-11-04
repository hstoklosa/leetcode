""" 
DIFFICULTY:  Easy
PROBLEM:     0141. Linked List Cycle
             https://leetcode.com/problems/linked-list-cycle
PATTERN:     Two Pointers (Fast & Slow)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    """
    In the following examole pointers overlap at node 4, hence a cycle. 
    Also, note that F has moved twice as many steps as S when they meet.

    Example:                                              Iterations:

       F,S                                     S,F        F1, S1  
      +---+---+---+---+           +---+---+---+---+        -> F3, S2
      | 1 | 2 | 3 | 4 |   ---->   | 1 | 2 | 3 | 4 |        -> F2, S3
      +---+---+---+---+           +---+---+---+---+        -> F4, S4
            |       |                   |       |       
            +-------+                   +-------+

    """

    def hasCycle(self, head: ListNode | None) -> bool:
        if head is None:
            return False

        fast = head 
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False