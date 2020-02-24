# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        preVal = None
        pre, cur = dummy, head
        while cur:
            next = cur.next
            if cur.val == preVal or next and cur.val == next.val:
                pre.next, preVal, cur = next, cur.val, next
            else:
                preVal, pre, cur = cur.val, cur, next
        return dummy.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head

        while cur:
            if not cur.next or cur.val != cur.next.val:
                pre, cur = cur, cur.next
            else:
                cur = cur.next
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = pre.next = cur.next

        return dummy.next
