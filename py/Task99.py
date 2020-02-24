# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.fst = None
        self.sed = None
        self.pre = TreeNode(-100000000000)

        def inorder(root: TreeNode) -> None:
            if not root:
                return
            inorder(root.left)
            if self.pre.val > root.val:
                if not self.fst:
                    self.fst = self.pre
                    self.sed = root
                else:
                    self.sed = root
            self.pre = root
            inorder(root.right)

        inorder(root)
        self.fst.val, self.sed.val = self.sed.val, self.fst.val


so = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
so.recoverTree(root)
