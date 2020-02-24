# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode
import random


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.arr = []
        while head:
            self.arr.append(head)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.arr).val
