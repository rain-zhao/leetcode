# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = dummy = ListNode(-1, head)
        while pre.next and pre.next.next:
            # tmp = pre.next
            # pre.next = pre.next.next
            # tmp.next = pre.next.next
            # pre.next.next = tmp
            # pre = tmp
            pre.next, pre.next.next, pre.next.next.next, pre =\
                pre.next.next, pre.next, pre.next.next.next, pre.next
        return dummy.next


head = ListNode(1)
head.nextItm(2).nextItm(3).nextItm(4)
obj = Solution()

print(obj.swapPairs(head))


head
