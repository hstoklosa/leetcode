""" 
DIFFICULTY:  Easy
PROBLEM:     0617. Merge Two Binary Trees
             https://leetcode.com/problems/merge-two-binary-trees
PATTERN:     BFS
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        def dfs(p: TreeNode | None, q: TreeNode | None):
            if not p:
                return q
            if not q:
                return p
            if not p and not q:
                return None
                        
            r = TreeNode(p.val + q.val)
            r.left = dfs(p.left, q.left)
            r.right = dfs(p.right, q.right)

            return r
            
        return dfs(root1, root2)