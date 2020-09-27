# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # dfs
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p

        def dfs(root: TreeNode) -> TreeNode:
            if p.val <= root.val <= q.val:
                return root
            if root.val > q.val:
                return dfs(root.left)
            return dfs(root.right)
        return dfs(root)

    # iteration
    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        while 1:
            if p.val <= root.val <= q.val:
                return root
            if root.val > q.val:
                root = root.left
            else:
                root = root.right
        return None
