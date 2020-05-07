
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode
import sys


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root: TreeNode, min: int, max: int) -> bool:
            if not root:
                return True
            if not (min < root.val < max):
                return False
            return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)

        return dfs(root, -sys.maxsize, sys.maxsize)

    def isValidBST2(self, root: TreeNode) -> bool:
        self.pre = -100000000000

        def inorder(root: TreeNode) -> bool:
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.pre:
                return False
            self.pre = root.val
            return inorder(root.right)
        return inorder(root)

    # inorder 2020-05-05
    def isValidBST3(self, root: TreeNode) -> bool:
        self.pre = -99999999999

        def inorder(node: TreeNode) -> bool:
            if not node:
                return True
            # left
            if not inorder(node.left):
                return False
            # cur node
            elif node.val <= self.pre:
                return False

            self.pre = node.val
            # right
            return inorder(node.right)

        return inorder(root)
