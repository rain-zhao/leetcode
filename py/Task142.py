# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # floyd
    def detectCycle(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        if not p2 or not p2.next:
            return None
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    # hash
    def detectCycle2(self, head: ListNode) -> ListNode:
        hash = set()
        p = head
        while p:
            if p in head:
                return p
            hash.add(p)
            p = p.next
        return None
