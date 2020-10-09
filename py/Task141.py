class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # floyd
    def hasCycle(self, head: ListNode) -> bool:
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

    # hash
    def hasCycle2(self, head: ListNode) -> bool:
        p = head
        hash = set()
        while p:
            if p in hash:
                return True
            hash.add(p)
            p = p.next
        return False
