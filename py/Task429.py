
# Definition for a Node.

from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    # dfs
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(root, level):
            if len(res) == level:
                res.append([root.val])
            else:
                res[level].append(root.val)
            for child in root.children:
                dfs(child, level+1)
        dfs(root, 0)
        return res
    # bfs

    def levelOrder2(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            size = len(q)
            res.append([])
            for _ in range(size):
                node = q.popleft()
                res[-1].append(node.val)
                q.extend(node.children)
        return res
