# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = 10**5

        def diff(node: TreeNode) -> List[int]:
            nmin, nmax = node.val, node.val
            if node.left:
                lmin, lmax = diff(node.left)
                self.res = min(self.res, node.val - lmax)
                nmin = lmin
            if node.right:
                rmin, rmax = diff(node.right)
                self.res = min(self.res, rmin - node.val)
                nmax = rmax
            return [nmin, nmax]
        diff(root)
        return self.res

    # in-order
    def minDiffInBST2(self, root: TreeNode) -> int:
        self.res = 10**5
        self.prev = -10**5

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            self.res = min(self.res, node.val-self.prev)
            self.prev = node.val
            dfs(node.right)
        dfs(root)
        return self.res


obj = Solution()
root = TreeNode(96)
root.left = TreeNode(12, None, TreeNode(
    13, None, TreeNode(52, TreeNode(29), None)))
print(obj.minDiffInBST2(root))
