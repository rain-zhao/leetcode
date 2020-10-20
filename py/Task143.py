# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        arr = []
        # put into list
        while head:
            arr.append(head)
            head = head.next
        # reorder
        size = len(arr)
        pre = dummy = ListNode(-1)
        for i in range(size >> 1):
            pre.next, arr[i].next, pre = arr[i], arr[-i-1], arr[-i-1]
        # odd
        if size & 1:
            pre.next, pre = arr[size >> 1], arr[size >> 1]
        pre.next = None

    def reorderList2(self, head: ListNode) -> None:
        if not head:
            return
        # find mid
        p1 = p2 = head
        while p2.next and p2.next.next:
            p1, p2 = p1.next, p2.next.next
        # p1 is mid
        # reverse the second sequence
        pre, p, p1.next = None, p1.next, None
        while p:
            p.next, pre, p = pre, p, p.next
        dummy = ListNode(-1)
        pre, p1, p2 = dummy, head, pre
        while p2:
            pre.next, p1.next, pre, p1, p2 = p1, p2, p2, p1.next, p2.next
        if p1:
            pre.next = p1


head = ListNode(1)
head.nextItm(2).nextItm(3).nextItm(4).nextItm(5)
so = Solution()
so.reorderList3(head)
