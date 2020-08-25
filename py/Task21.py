# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        p1, p2 = l1, l2
        dummy = ListNode()
        prev = dummy

        while p1 and p2:
            if p1.val > p2.val:
                prev.next = p2
                p2 = p2.next
            else:
                prev.next = p1
                p1 = p1.next
            prev = prev.next

        if p1:
            prev.next = p1
        if p2:
            prev.next = p2

        return dummy.next

    # recursion
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

    # recursion 2
    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        def dfs(prev: ListNode, l1: ListNode, l2: ListNode) -> None:
            if not l1:
                prev.next = l2
                return
            if not l2:
                prev.next = l1
                return
            if l1.val <= l2.val:
                prev.next = l1
                dfs(prev.next, l1.next, l2)
            else:
                prev.next = l2
                dfs(prev.next, l1, l2.next)
        dummy = ListNode()
        prev = dummy
        dfs(prev, l1, l2)
        return dummy.next
