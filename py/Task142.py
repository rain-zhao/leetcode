# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # floyd
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                break
        if p1 != p2:
            return None
        p1 = head
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1
