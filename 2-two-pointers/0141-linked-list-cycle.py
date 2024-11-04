""" 
PROBLEM:     0141. Linked List Cycle
             https://leetcode.com/problems/linked-list-cycle
DIFFICULTY:  Easy
PATTERN:     Two Pointers (Fast & Slow)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    """
    https://www.hellointerview.com/learn/code/linked-list/overview

    In the example, pointers overlap at node 4, hence a cycle. 
    Also, note that F has moved twice as many steps as S when they meet.

    Example:                                              Iterations:

       F,S                                     S,F        F1, S1  
      +---+---+---+---+           +---+---+---+---+       -> F3, S2
      | 1 | 2 | 3 | 4 |   ---->   | 1 | 2 | 3 | 4 |       -> F2, S3
      +---+---+---+---+           +---+---+---+---+       -> F4, S4
            |       |                   |       |       
            +-------+                   +-------+

    """

    def hasCycle(self, head: ListNode | None) -> bool:
        if head is None:
            return False

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
    
def create_linked_list(arr, pos=-1):
    if not arr:
        return None
        
    # Create nodes
    nodes = [ListNode(val) for val in arr]
    
    # Link nodes
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
        
    # Create cycle if pos is valid
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
        
    return nodes[0]