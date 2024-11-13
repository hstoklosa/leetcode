""" 
DIFFICULTY:  Easy
PROBLEM:     0572. Subtree of Another Tree
             https://leetcode.com/problems/subtree-of-another-tree
PATTERN:     DFS (Recursion)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root and not subRoot:
            return False
        if not root:
            return False

        def is_identical(p: TreeNode | None, q: TreeNode | None):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False            

            return is_identical(p.left, q.left) and is_identical(p.right, q.right)
        
        if is_identical(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) 
                or self.isSubtree(root.right, subRoot))          