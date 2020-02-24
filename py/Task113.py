# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from TreeNode import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(root: TreeNode, sum: int, ans: List[int]) -> None:
            if not root.left and not root.right:
                if sum == root.val:
                    res.append(ans+[root.val])
                return

            sum -= root.val
            ans.append(root.val)
            if root.left:
                dfs(root.left, sum, ans)
            if root.right:
                dfs(root.right, sum, ans)
            ans.pop()

        dfs(root,sum,[])
        return res
