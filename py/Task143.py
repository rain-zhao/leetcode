# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        arr = []
        # put into list
        while head:
            arr.append(head)
            head = head.next
        # reorder
        size = len(arr)
        dummy = ListNode(-1)
        pre = dummy
        for i, j in zip(arr[:size//2], arr[-1:(size-1)//2:-1]):
            pre.next, i.next, pre = i, j, j
        if size & 1:
            pre.next, pre = arr[size//2], arr[size//2]
        pre.next = None

    def reorderList2(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        # find mid pos
        p1 = p2 = head
        while p2.next and p2.next.next:
            p1, p2 = p1.next, p2.next.next
        # p1 is mid pos
        # reverse link list after p1
        pre, cur, p1.next = None, p1.next, None
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        # pre is the reverse list's head
        dummy = ListNode(-1)
        p1, p2, pre = head, pre, dummy
        while p2:
            pre.next, p1.next, p1, p2, pre = p1, p2, p1.next, p2.next, p2

        if p1:
            pre.next = p1

        return dummy.next


head = ListNode(1)
head.nextItm(2).nextItm(3).nextItm(4)
so = Solution()
so.reorderList2(head)
