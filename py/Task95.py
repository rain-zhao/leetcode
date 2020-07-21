# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode
from typing import List


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return None

        def dfs(beg: int, end: int) -> List[TreeNode]:
            if beg == end:
                return [None]
            res = []
            for i in range(beg, end):
                lefts = dfs(beg, i)
                rights = dfs(i+1, end)

                for l in lefts:
                    for r in rights:
                        root = TreeNode(i)
                        root.left, root.right = l, r
                        res.append(root)
            return res

        return dfs(1, n+1)

    # dfs + memo
    def generateTrees2(self, n: int) -> List[TreeNode]:
        if not n:
            return []

        def index(beg: int, end: int) -> int:
            return beg * n + end

        memo = {}

        def dfs(beg: int, end: int) -> List[TreeNode]:
            if beg > end:
                return [None]
            idx = index(beg, end)
            if idx in memo:
                return memo[idx]
            res = []
            for i in range(beg, end + 1):
                lefts = dfs(beg, i - 1)
                rights = dfs(i + 1, end)
                for l in lefts:
                    for r in rights:
                        root = TreeNode(i)
                        root.left, root.right = l, r
                        res.append(root)
            memo[idx] = res
            return res
        return dfs(1, n)


n = 3
obj = Solution()
print(obj.generateTrees2(n))
