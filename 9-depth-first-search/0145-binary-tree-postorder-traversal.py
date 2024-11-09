""" 
DIFFICULTY:  Easy
PROBLEM:     0145. Binary Tree Postorder Traversal
             https://leetcode.com/problems/binary-tree-postorder-traversal
PATTERN:     DFS (Stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def postorder(node: TreeNode | None) -> TreeNode | None:
            if node is None:
                return

            postorder(node.left)
            postorder(node.right)

            result.append(node.val)
        
        postorder(root)
        return result
