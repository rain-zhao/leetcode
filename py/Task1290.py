# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        cur = head
        while cur:
            res = (res << 1) + cur.val
            cur = cur.next
        return res
