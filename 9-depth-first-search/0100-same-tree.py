""" 
DIFFICULTY:  Easy
PROBLEM:     0100. Same Tree
             https://leetcode.com/problems/same-tree
PATTERN:     Binary Tree, [DFS], Stack
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right        

class Solution:

    """
    Think subtrees and recursion
       +-------------+
       |      1      |
       |     / \     |
      +-------++---+ |
      ||  2   || 3 | |
      |+-/-\--|+---+-+
      | 4   5 |     
      +-------+    
    """

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False 
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)