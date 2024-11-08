""" 
DIFFICULTY:  Easy
PROBLEM:     0100. Same Tree
             https://leetcode.com/problems/same-tree
PATTERN:     Binary Tree, DFS, Stack
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right        

class Solution:
    """
    Think subtrees and recursion:

        +----------------+
        |         1      |
        |        / \     |
        | +-------++---+ |
        | |   2   || 3 | |
        +-|--/-\--|+---+-+
          | 4   5 |     
          +-------+     
    """
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        print(p, q)
        if not p and not q:
            return True
        if not p or not q:
            return False 
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])

    i = 1
    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

test_cases = [
    [[1, 2, 3], [1, 2, 3]],
    [[1,2], [1, None, 2]],
    [[1, 2, 1], [1, 1, 2]],
]

solution = Solution()

for i, case in enumerate(test_cases, 1):
    root1 = build_tree(case[0])
    root2 = build_tree(case[1])
    result = solution.isSameTree(root1, root2)
    print(f"Test case {i}:")
    print(f"Input: {case}")
    print(f"Output: {result}")
    print()