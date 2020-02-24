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
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect2(root.left)
            self.connect2(root.right)

        return root


root = Node(1, None, None, None)
root.left, root.right = Node(2, None, None, None), Node(9, None, None, None)
left, right = root.left, root.right
left.left, left.right = Node(3, None, None, None), Node(6, None, None, None)
right.left, right.right = Node(
    10, None, None, None), Node(13, None, None, None)
left, right = root.left.left, root.left.right
left.left, left.right = Node(4, None, None, None), Node(5, None, None, None)
right.left, right.right = Node(7, None, None, None), Node(8, None, None, None)
left, right = root.right.left, root.right.right
left.left, left.right = Node(11, None, None, None), Node(12, None, None, None)
right.left, right.right = Node(
    14, None, None, None), Node(15, None, None, None)

so = Solution()
so.connect2(root)
