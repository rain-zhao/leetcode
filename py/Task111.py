class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def leftTree(self, x):
        self.left = x
        return self

    def rightTree(self, x):
        self.right = x
        return self


class Solution:
    # dfs
    def minDept(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.md = 2 << 32

        def dfs(root: TreeNode, dept: int):
            if not root.left and not root.right:
                self.md = min(self.md, dept)
                return
            if root.left:
                dfs(root.left, dept+1)
            if root.right:
                dfs(root.right, dept+1)
        dfs(root, 1)
        return self.md

    # dfs 优化代码
    def minDept2(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDept2(root.left)
        right = self.minDept2(root.right)
        if not left or not right:
            return left + right + 1
        return min(left, right) + 1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20).leftTree(TreeNode(15)).rightTree(TreeNode(7))

obj = Solution()
print(obj.minDept(root))
