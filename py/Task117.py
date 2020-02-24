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
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        queue = deque([root])
        while queue:
            l = len(queue)
            for _ in range(l-1):
                item = queue.popleft()
                item.next = queue[0]
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)

            item = queue.popleft()
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)

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
