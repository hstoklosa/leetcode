""" 
DIFFICULTY:  Easy
PROBLEM:     0637. Average of Levels in Binary Tree
             https://leetcode.com/problems/average-of-levels-in-binary-tree
PATTERN:     Binary Tree, BFS, Queue
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        queue = deque([root])
        level, level_size = 0, 1
        result = []
        
        while len(queue) != 0:
            _sum = 0

            for _ in range(level_size):
                node = queue.popleft()

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                
                _sum += node.val

            result.append(round(_sum / level_size, 5))
            level, level_size = level + 1, len(queue)

        return result