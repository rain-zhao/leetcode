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


head = ListNode(4)
head.nextItm(2).nextItm(1).nextItm(3)
so = Solution()
so.insertionSortList(head)
