""" 
DIFFICULTY:  Easy
PROBLEM:     0206. Reverse Linked List
             https://leetcode.com/problems/reverse-linked-list
PATTERN:     In-place Reversal of a LinkedList
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    """
    Tracing of recursive solution:

     +---+     +---+     +---+
     | 1 | --> | 2 | --> | 3 |
     +---+     +---+     +---+
      
     reverseList([1])
     |   newhead = reverseList([1].next)
     + - head.next.next = [1]     # Makes [2] point to [1]
         |      V
         | :reverseList([2])
         |   newhead = reverseList([2].next)
         + - head.next.next = [2]    # Makes [3] point to [2]
             |       V
             | :reverseList([3])
             + - [3].next == None     # Base case, returns [3]
    """

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        
        nxt = head.next
        curr = self.reverseList(nxt)
        head.next.next = head
        head.next = None

        return curr

    def _reverseList(self, head: ListNode | None) -> ListNode | None:
        prv, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt

        return prv

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

def print_linked_list(head):
    while head: 
        print(head.val, end=" -> ")
        head = head.next
    print("None")