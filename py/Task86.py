# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        lo, hi = ListNode(-1), ListNode(-1)
        curLo, curHi, cur = lo, hi, head

        while cur:
            if cur.val < x:
                curLo.next = cur
                curLo = curLo.next
            else:
                curHi.next = cur
                curHi = curHi.next
            cur = cur.next

        curLo.next, curHi.next = hi.next, None

        return lo.next


head = ListNode(1)
head.nextItm(4).nextItm(3).nextItm(2).nextItm(5).nextItm(2)
so = Solution()
so.partition(head, 3)
