# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode


class Solution:
    # dfs
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left)+self.countNodes(root.right)+1

    def countNodes3(self, root: TreeNode) -> int:
        if not root:
            return 0

        levll, levlr = self.cntLevel(root.left), self.cntLevel(root.right)
        if levll == levlr:
            return 2**levll+self.countNodes3(root.right)
        else:
            return 2**levlr+self.countNodes3(root.left)

    def cntLevel(self, root: TreeNode) -> int:
        cnt = 0
        while root:
            cnt += 1
            root = root.left
        return cnt

    def countNodes5(self, root: TreeNode) -> int:
        def level(root: TreeNode) -> int:
            lev = 0
            while root:
                lev += 1
                root = root.left
            return lev

        if not root:
            return 0
        cnt = 0
        left = level(root.left)
        while root:
            right = level(root.right)
            if left == right:
                # left full
                cnt += 2 ** left
                root = root.right
            else:
                # right full
                cnt += 2 ** right
                root = root.left
            left -= 1
        return cnt
