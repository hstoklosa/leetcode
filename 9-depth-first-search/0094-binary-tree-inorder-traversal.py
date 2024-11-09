""" 
DIFFICULTY:  Easy
PROBLEM:     0094. Binary Tree Inorder Traversal
             https://leetcode.com/problems/binary-tree-inorder-traversal
PATTERN:     DFS (Stack)
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        
        def inorder(node: TreeNode | None):
            if node is None:
                return
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result 

    def _inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        curr = root
        stack, result = deque(), []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result