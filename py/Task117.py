"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from Node import Node
from collections import deque


class Solution:
    # bfs: optimize at 2020-09-28
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        queue = deque([root])

        while queue:
            size = len(queue)
            array = []
            for _ in range(size):
                itm = queue.popleft()
                array.append(itm)
                if itm.left:
                    queue.append(itm.left)
                if itm.right:
                    queue.append(itm.right)
            for i, j in zip(array, array[i]):
                i.next = j
        return root

    def connect2(self, root: Node) -> Node:
        if not root:
            return root
        dummy = Node(1, None, None, root)
        while dummy.next:
            pre, cur = dummy, dummy.next
            pre.next = None
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
        return root
