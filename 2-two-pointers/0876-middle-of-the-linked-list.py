""" 
PROBLEM:     0876. Middle of the Linked List
             https://leetcode.com/problems/middle-of-the-linked-list
DIFFICULTY:  Easy
PATTERN:     Two Pointers (Fast & Slow)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    """
    Maintaining 2 (fast and slow) pointers will result in the slow pointer
    to be at the middle of the LinkedList by the time the fast pointer
    reaches the end of the LinkedList.

    Example I:                                                  Iterations:

       F,S                                      S       F       F1, S1  
      +---+---+---+---+---+           +---+---+---+---+---+      -> F3, S2
      | 1 | 2 | 3 | 4 | 5 |   ---->   | 1 | 2 | 3 | 4 | 5 |      -> F5, S3
      +---+---+---+---+---+           +---+---+---+---+---+      


    Example II:                                              Iterations:

       F,S                                  S        F       F1, S1  
      +---+---+---+---+           +---+---+---+---+           -> F3, S2
      | 1 | 2 | 3 | 4 |   ---->   | 1 | 2 | 3 | 4 |           -> X, S3
      +---+---+---+---+           +---+---+---+---+      

    """

    def middleNode(self, head: ListNode | None) -> ListNode | None:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

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