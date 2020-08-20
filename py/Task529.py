from typing import List


class Solution:
    # dfs
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        m, n = len(board), len(board[0])
        direct = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]

        def dfs(x: int, y: int):
            res = 0
            queue = []
            for dx, dy in direct:
                xx, yy = x+dx, y+dy
                if not 0 <= xx < m or not 0 <= yy < n:
                    continue
                if board[xx][yy] == 'M':
                    res += 1
                    continue
                if board[xx][yy] != 'E':
                    continue
                queue.append((xx, yy))

            if res == 0:
                board[x][y] = 'B'
                for xx, yy in queue:
                    dfs(xx, yy)
            else:
                board[x][y] = str(res)
        dfs(click[0], click[1])
        return board

    # dfs 简化代码
    def updateBoard2(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        m, n = len(board), len(board[0])
        direct = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]

        def check(x, y, c):
            return 0 <= x < m and 0 <= y < n and board[x][y] == c

        def dfs(x: int, y: int):
            cnt = sum(check(x+dx, y+dy, 'M') for dx, dy in direct)
            if cnt > 0:
                board[x][y] = str(cnt)
            else:
                board[x][y] = 'B'
                for dx, dy in direct:
                    xx, yy = x+dx, y+dy
                    if check(xx, yy, 'E'):
                        dfs(xx, yy)

        dfs(*click)
        return board


# board = [
#     ["B", "1", "E", "1", "B"],
#     ["B", "1", "M", "1", "B"],
#     ["B", "1", "1", "1", "B"],
#     ["B", "B", "B", "B", "B"]
# ]
# click = [1, 2]
board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"],
         ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
click = [3, 0]
obj = Solution()
print(obj.updateBoard2(board, click))
