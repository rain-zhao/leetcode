# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode
from collections import deque


class Solution:
    # dfs
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        res = []

        def dfs(lev: int, node: TreeNode):
                # terminator
            if not node:
                return
            if lev == len(res):
                res.append([])
            res[lev].append(node.val)
            dfs(lev+1, node.left)
            dfs(lev+1, node.right)
        dfs(0, root)
        return res[:: -1]

    def levelOrderBottom2(self, root: TreeNode) -> [[int]]:
        res = []
        dq = deque([root])
        while dq:
            l = []
            for _ in range(len(dq)):
                node = dq.popleft()
                l.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(l)
        res.reverse()
        return res


root = TreeNode(3)
root.left, root.right = TreeNode(9), TreeNode(20)
root.right.left, root.right.right = TreeNode(15), TreeNode(7)
solution = Solution()
print(solution.levelOrderBottom(root))
