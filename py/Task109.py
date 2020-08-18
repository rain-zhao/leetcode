# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from ListNode import ListNode
from TreeNode import TreeNode


class Solution:
    # fast & slow cursor
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def recur(beg: ListNode, end: ListNode) -> TreeNode:
            if beg == end:
                return None
            p1 = p2 = beg
            while p2.next != end and p2.next.next != end:
                p1, p2 = p1.next, p2.next.next
            root = TreeNode(p1.val)
            root.left = recur(beg, p1)
            root.right = recur(p1.next, end)
            return root
        return recur(head, None)

    # put val into array
    def sortedListToBST2(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        # put linked list into array
        array = []
        pos = head
        while pos:
            array.append(pos.val)
            pos = pos.next

        def transfer(beg: int, end: int) -> TreeNode:
            if beg > end:
                return None
            mid = (beg + end) >> 1
            root = TreeNode(array[mid])
            root.left = transfer(beg, mid-1)
            root.right = transfer(mid+1, end)
            return root
        return transfer(0, len(array)-1)


head = ListNode(-10)
head.nextItm(-3).nextItm(0).nextItm(5).nextItm(9)
so = Solution()
so.sortedListToBST3(head)
