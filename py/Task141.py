class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # floyd
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    

