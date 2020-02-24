# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0

        def dfs(node: TreeNode, val: int) -> None:
            if not node.left and not node.right:
                self.res += val
                return
            if node.left:
                dfs(node.left, val*10+node.left.val)
            if node.right:
                dfs(node.right, val*10+node.right.val)

        dfs(root, root.val)
        return self.res
