# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from TreeNode import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        def dfs(root: TreeNode, s: str):
            if not root.left and not root.right:
                res.append(s+str(root.val))
                return
            s += str(root.val)+'->'
            if root.left:
                dfs(root.left, s)
            if root.right:
                dfs(root.right, s)
        dfs(root, '')
        return res
