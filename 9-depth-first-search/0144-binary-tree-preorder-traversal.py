""" 
DIFFICULTY:  Easy
PROBLEM:     144. Binary Tree Preorder Traversal
             https://leetcode.com/problems/binary-tree-preorder-traversal
PATTERN:     DFS (Stack)
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def preorder(node: TreeNode | None) -> TreeNode | None:
            if node is None:
                return

            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return result

    def _preorderTraversal(self, root: TreeNode | None) -> list[int]:
        stack, result = deque([root]), []

        while stack and root:
            root = stack.pop()
            result.append(root.val)
            
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        
        return result