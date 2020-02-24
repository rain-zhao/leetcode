class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def nextItm(self, x):
        self.next = ListNode(x)
        return self.next
