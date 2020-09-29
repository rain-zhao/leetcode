# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode
from typing import List


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        res.reverse()
        return res

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root.left)
                root = root.right
            else:
                root = stack.pop()
        return reversed(res)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
so = Solution()
print(so.postorderTraversal2(root))
