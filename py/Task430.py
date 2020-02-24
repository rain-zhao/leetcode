# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        def recur(head):
            prev, cur = None, head
            while cur:
                if cur.child:
                    next = cur.next
                    cur.next, cur.child.prev = cur.child, cur
                    last = recur(cur.child)
                    cur.child = None
                    if next:
                        last.next, next.prev = next, last
                    prev, cur = last, next
                else:
                    prev, cur = cur, cur.next
            return prev
        recur(head)
        return head


head = Node(8, None, None, None)
head.next = Node(9, None, None, None)
head.child = Node(10, None, None, None)

so = Solution()
so.flatten(head)
