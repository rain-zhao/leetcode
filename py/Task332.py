from typing import List
from collections import defaultdict
from collections import _heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        vec = defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            _heapq.heapify(vec[key])
        stack = []

        def dfs(curr: str):
            while vec[curr]:
                arrive = _heapq.heappop(vec[curr])
                dfs(arrive)
            stack.append(curr)
        dfs("JFK")
        return stack[::-1]


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = [["A", "D"], ["A", "B"], ["B", "A"], ["B", "C"], ["C", "B"]]
obj = Solution()
print(obj.findItinerary(tickets))
