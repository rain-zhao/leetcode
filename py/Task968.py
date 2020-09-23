# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def minCover(root: TreeNode) -> List[int]:
            if not root:
                return [10**3, 0, 0]
            l, r = minCover(root.left), minCover(root.right)
            a = l[2]+r[2]+1
            b = min(a, min(l[0]+r[1], l[1]+r[0]))
            c = min(a, l[1]+r[1])
            return [a, b, c]
        return minCover(root)[1]

