""" 
DIFFICULTY:  Easy
PROBLEM:     0104. Maximum Depth of Binary Tree
             https://leetcode.com/problems/maximum-depth-of-binary-tree
PATTERN:     DFS (Recursion)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        self._max = 0

        def dfs(node: TreeNode | None, depth: int):
            if node is None:
                if depth > self._max:
                    self._max = depth
                return

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            
        dfs(root, 0)
        return self._max