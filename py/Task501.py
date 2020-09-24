# Definition for a binary tree node.
from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        counts = defaultdict(int)

        def dfs(root: TreeNode):
            if not root:
                return
            counts[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res = []
        maxCnt = 0
        for itm in counts:
            if counts[itm] == maxCnt:
                res.append(itm)
            elif counts[itm] > maxCnt:
                res = [itm]
                maxCnt = counts[itm]
        return res

    # in-order
    def findMode2(self, root: TreeNode) -> List[int]:
        self.pre, self.cnt, self.maxCnt = None, -1, 0
        self.res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if root.val == self.pre:
                self.cnt += 1
            else:
                if self.cnt == self.maxCnt:
                    self.res.append(self.pre)
                elif self.cnt > self.maxCnt:
                    self.res = [self.pre]
                    self.maxCnt = self.cnt
                self.pre, self.cnt = root.val, 1
            dfs(root.right)

        dfs(root)
        if self.cnt == self.maxCnt:
            self.res.append(self.pre)
        elif self.cnt > self.maxCnt:
            self.res = [self.pre]

        return self.res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

obj = Solution()
print(obj.findMode2(root))
