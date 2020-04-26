# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 示例:

# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6


from ListNode import ListNode
from typing import List
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        heap = [(head.val, idx, head) for idx, head in enumerate(lists) if head]
        heapq.heapify(heap)

        while heap:
            _, idx, node = heap[0]
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heapreplace(heap, (node.next.val, idx, node.next))
            else:
                heapq.heappop(heap)

        cur.next = None
        return dummy.next


lists = []
node1 = ListNode(1)
node1.nextItm(4).nextItm(5)
lists.append(node1)
node2 = ListNode(1)
node2.nextItm(3).nextItm(4)
lists.append(node2)
node3 = ListNode(2)
node3.nextItm(6)
lists.append(node3)

obj = Solution()
print(obj.mergeKLists(lists))
