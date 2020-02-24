# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        def dfs(root: TreeNode, level: int) -> None:
            if not root:
                return
            if level > len(self.res)-1:
                self.res.append([])
            self.res[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        self.res = []
        dfs(root, 0)
        self.res.reverse()

        return self.res
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
print(solution.levelOrderBottom2(root))
