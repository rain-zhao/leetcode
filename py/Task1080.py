# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return root
        if not root.left and not root.right:
            return None if limit-root.val > 0 else root
        root.left = self.sufficientSubset(root.left, limit-root.val)
        root.right = self.sufficientSubset(root.right, limit-root.val)
        if not root.left and not root.right:
            return None if limit-root.val > 0 else root
        return root


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(-99)
# root.right.left = TreeNode(-99)
# root.right.right = TreeNode(7)
# root.left.left.left = TreeNode(8)
# root.left.left.right = TreeNode(9)
# root.left.right.left = TreeNode(-99)
# root.left.right.right = TreeNode(-99)
# root.right.left.left = TreeNode(12)
# root.right.left.right = TreeNode(13)
# root.right.right.left = TreeNode(-99)
# root.right.right.right = TreeNode(14)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(-3)
root.left.left = TreeNode(-5)
root.right.left = TreeNode(4)


so = Solution()
so.sufficientSubset(root, -1)
