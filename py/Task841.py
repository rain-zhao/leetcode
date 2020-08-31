from typing import List
from collections import deque


class Solution:
    # dfs
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        def dfs(room: int):
            if visited[room]:
                return
            visited[room] = True
            for toRoom in rooms[room]:
                dfs(toRoom)
        dfs(0)
        return sum(visited) == n

    # bfs
    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        queue = deque([0])
        while queue:
            room = queue.popleft()
            if visited[room]:
                continue
            visited[room] = True
            for toRoom in rooms[room]:
                queue.append(toRoom)
        return sum(visited) == n


rooms = [[1, 3], [3, 0, 1], [2], [0]]
obj = Solution()
print(obj.canVisitAllRooms(rooms))
