# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.pre = -1 << 10
        self.res = 1 << 10

        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            self.res = min(self.res, root.val - self.pre)
            self.pre = root.val
            dfs(root.right)
        dfs(root)
        return self.res


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
obj = Solution()
print(obj.getMinimumDifference(root))
