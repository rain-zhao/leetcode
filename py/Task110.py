# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode
from queue import Queue


class Solution:
    # dfs
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                return -1
            if not -1 <= left - right <= 1:
                return -1
            return max(left, right)+1
        return dfs(root) != -1


root = TreeNode(3)
root.left, root.right = TreeNode(9), TreeNode(20)
root.right.left, root.right.right = TreeNode(15), TreeNode(7)
solution = Solution()
print(solution.isBalanced(root))
