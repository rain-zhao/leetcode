# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # dfs 基于特征：最小公共祖先要么自己为p or q，要么p和q分布在左右子树
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root

    # 生成一个字典，dict = {子节点：父节点}
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root

        prevMap = {}

        def markPrev(node: 'TreeNode', prev: 'TreeNode' = None) -> None:
            if not node:
                return
            prevMap[node] = prev
            markPrev(node.left, node)
            markPrev(node.right, node)

        markPrev(root)

        pathSet = {p}
        while prevMap[p]:
            pathSet.add(prevMap[p])
            p = prevMap[p]

        while q:
            if q in pathSet:
                return q
            q = prevMap[q]

        return None
