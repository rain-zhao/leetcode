
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs using recursion
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        def flatten(root: TreeNode) -> TreeNode:
            tail = root
            # left
            if root.left:
                tail = flatten(root.left)
                root.left, root.right, tail.right = None, root.left, root.right
            # right
            if tail.right:
                tail = flatten(tail.right)
            return tail
        flatten(root)


obj = Solution()
root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(5)
root.left.left, root.left.right = TreeNode(3), TreeNode(4)
root.right.right = TreeNode(6)
obj.flatten(root)
