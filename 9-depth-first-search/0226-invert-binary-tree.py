""" 
DIFFICULTY:  Easy
PROBLEM:     0226. Invert Binary Tree
             https://leetcode.com/problems/invert-binary-tree
PATTERN:     DFS (Recursion)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode| None:
        if root is None:
            return
        
        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp
        return root