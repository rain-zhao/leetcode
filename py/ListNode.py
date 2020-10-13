class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def nextItm(self, x):
        self.next = ListNode(x)
        return self.next

    def __str__(self):
        return str(self.val) + '->' + str(self.next)


if __name__ == '__main__':
    head = ListNode(1)
    head.nextItm(2).nextItm(3).nextItm(4).nextItm(5)
    print(head)
