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

    def countNodes2(self, root: TreeNode) -> int:
        count = 0

        def dfs(root: TreeNode):
            if not root:
                return
            nonlocal count
            count += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return count

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

    def countNodes4(self, root: TreeNode) -> int:
        if not root:
            return 0
        cnt = 0
        levll, levlr = self.cntLevel(root.left), None
        while root:
            levlr = self.cntLevel(root.right)
            if levll == levlr:
                cnt += 2**levll
                root = root.right
                levll = levlr-1
            else:
                cnt += 2**levlr
                root = root.left
                levll = levll-1
        return cnt
