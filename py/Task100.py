# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode
from collections import deque

class Solution:
    """
        def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
            if p and q:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return not p and not q
    """

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        dq = deque([(p, q)])
        while deque:
            p, q = dq.popleft()
            if p and q:
                if p.val != q.val:
                    return False
                dq.append((p.left, q.left))
                dq.append((p.right, q.right))
            elif p or q:
                return False
        return True
