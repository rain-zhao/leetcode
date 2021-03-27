# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # fast-slow cursor
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        n = 1
        while cur.next:
            cur = cur.next
            n += 1
        k %= n
        if not k:
            return head
        fast = slow = head
        # fast cursor is k step faster then slow cursor
        for _ in range(k):
            fast = fast.next
        # iter the fast cursor to the tail
        while fast.next:
            fast = fast.next
            slow = slow.next
        newHead = slow.next
        fast.next = head
        slow.next = None

        return newHead

    # using tempory array
    def rotateRight2(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        n = len(arr)
        k %= n
        if k == 0:
            return head
        newHead = arr[-k]
        arr[-1].next = arr[0]
        arr[-k-1].next = None
        return newHead


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(5)
k = 2
obj = Solution()
print(obj.rotateRight(head, k))
