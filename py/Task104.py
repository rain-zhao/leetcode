from queue import SimpleQueue
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # dfs
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # bfs
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = SimpleQueue()
        q.put(root)
        dept = 0
        while not q.empty():
            levelSize = q.qsize()
            dept += 1
            for _ in range(levelSize):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return dept

    # bfs using collections.deque
    def maxDepth3(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([root,])
        dept = 0
        while q:
            levelSize = len(q)
            dept += 1
            for _ in range(levelSize):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return dept
