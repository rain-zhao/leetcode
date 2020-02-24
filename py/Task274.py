from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort(reverse=True)
        idx = 0
        while idx < len(citations) and citations[idx] > idx:
            idx += 1
        return idx

    def hIndex2(self, citations: List[int]) -> int:
        import heapq
        if not citations:
            return 0
        res = 0
        heap = []
        for item in citations:
            heapq.heappush(heap, item)
            if heap[0] >= len(heap):
                res += 1
            else:
                heapq.heappop(heap)
        return res

    def hIndex3(self, citations: List[int]) -> int:
        if not citations:
            return 0
        l = len(citations)
        cnts = [0]*(l+1)
        for i in citations:
            cnts[min(l, i)] += 1
        k = l
        cnt = cnts[l]
        while k > cnt:
            k -= 1
            cnt += cnts[k]
        return k
