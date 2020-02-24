# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode
from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def preorder(root: TreeNode) -> None:
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if root.right:
                stack.append(node.right)
            if root.left:
                stack.append(node.left)
        return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
so = Solution()
print(so.preorderTraversal2(root))
