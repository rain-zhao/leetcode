# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tail = head
        while tail.next:
            next = tail.next
            pre, cur = dummy, dummy.next
            while cur.val < next.val:
                pre, cur = cur, cur.next
            if cur == next:
                tail = next
            else:
                tail.next = next.next
                pre.next = next
                next.next = cur
        return dummy.next

    def insertionSortList2(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tail = head
        while tail.next:
            # max
            if tail.val < tail.next.val:
                tail = tail.next
                continue
            cur = tail.next
            tail.next = cur.next
            p = dummy
            while p.next.val < cur.val:
                p = p.next
            # insert
            p.next, cur.next = cur, p.next
        return dummy.next


head = ListNode(-1)
head.nextItm(5).nextItm(3).nextItm(4).nextItm(0)
so = Solution()
so.insertionSortList2(head)
