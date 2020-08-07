# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode
from collections import deque


class Solution:
    """
        def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
            if p and q:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return not p and not q
    """

    # bfs
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        dq = deque([(p, q)])
        while deque:
            p, q = dq.popleft()
            if p and q:
                if p.val != q.val:
                    return False
                dq.append((p.left, q.left))
                dq.append((p.right, q.right))
            elif p or q:
                return False
        return True

    # dfs
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if not p:
            return not q
        if not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # print tree
    def isSameTree3(self, p: TreeNode, q: TreeNode) -> bool:
        def printTree(root: TreeNode) -> str:
            if not root:
                return 'N'
            return str(root.val) + '->' + printTree(root.left) + '->' + printTree(root.right)
        return printTree(p) == printTree(q)


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

obj = Solution()
print(obj.isSameTree3(p, q))
