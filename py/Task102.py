# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def _dfs(node: TreeNode, level: int) -> None:
            if not node:
                return
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            _dfs(node.left, level+1) or _dfs(node.right, level+1)

        _dfs(root, 0)
        return res


obj = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.levelOrder(root))
