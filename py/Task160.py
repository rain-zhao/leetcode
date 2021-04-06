# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def nextItm(self, x):
        self.next = ListNode(x)
        return self.next


class Solution:

    # hash
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur = headA
        sset = set()
        while cur:
            sset.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in sset:
                return cur
            cur = cur.next
        return None

    # fast-slow cursor
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        # 1.find A's tail
        cur = headA
        while cur.next:
            cur = cur.next
        tail = cur

        # 2.link A's tail to B's head
        tail.next = headB

        # 3.fast-slow cursor
        fast = slow = headA
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if not fast.next or not fast.next.next:
            # resume A tail's next
            tail.next = None
            return None

        slow = headA
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # resume A tail's next
        tail.next = None
        return slow

    # double cursor
    def getIntersectionNode3(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


obj = Solution()
# headA = ListNode(4)
# headA.nextItm(1).nextItm(8).nextItm(4).nextItm(5)
# headB = ListNode(5)
# headB.nextItm(0).nextItm(1).next = headA.next.next
headA = ListNode(2)
headA.nextItm(4).nextItm(6)
headB = ListNode(1)
headB.nextItm(5)

obj.getIntersectionNode3(headA, headB)
