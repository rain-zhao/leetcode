# Definition for a binary tree node.
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # dfs
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def isSymmetric(l: TreeNode, r: TreeNode) -> bool:
            if not l:
                return not r
            if not r:
                return False
            if l.val != r.val:
                return False

            return isSymmetric(l.left, r.right) and isSymmetric(l.right, r.left)

        return isSymmetric(root.left, root.right)

    # iter
    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = Queue()
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            l = q.get()
            r = q.get()
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            q.put(l.right)
            q.put(r.left)
            q.put(l.left)
            q.put(r.right)
        return True


obj = Solution()
root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(2)
root.left.left, root.left.right = TreeNode(3), TreeNode(4)
root.right.left, root.right.right = TreeNode(4), TreeNode(3)
print(obj.isSymmetric2(root))
