# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # using array and space complexity O(n)
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]

    # slow-fast cursor and space complexity o(1)
    def isPalindrome2(self, head: ListNode) -> bool:
        # if not head or not head.next:
        #     return True
        pre, p1, p2 = None, head, head
        while p2 and p2.next:
            p2 = p2.next.next
            p1.next, pre, p1 = pre, p1, p1.next
        if p2:
            # odd
            p1 = p1.next
        p1, p2 = pre, p1
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(0)
# head.next.next.next = ListNode(1)
obj = Solution()
print(obj.isPalindrome2(head))
