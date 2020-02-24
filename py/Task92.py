# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = None, dummy

        for _ in range(m):
            pre, cur = cur, cur.next

        pos = pre
        pre, cur = cur, cur.next

        for _ in range(m, n):
            cur.next, pre, cur = pre, cur, cur.next

        pos.next.next = cur
        pos.next = pre

        return dummy.next


head = ListNode(1)

head = ListNode(1)
head.nextItm(2).nextItm(3).nextItm(4).nextItm(5)
solution = Solution()
solution.reverseBetween(head, 2, 4)
