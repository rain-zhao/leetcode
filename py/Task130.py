from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def color(i: int, j: int) -> None:
            # terminator
            if not (0 <= i < m and 0 <= j < n) or board[i][j] in ('X', 'T'):
                return
            board[i][j] = 'T'
            for x, y in direct:
                color(i+x, j+y)

        for i in range(n):
            color(0, i)
            color(m-1, i)

        for i in range(1, m-1):
            color(i, 0)
            color(i, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


obj = Solution()
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
print(board)
obj.solve(board)
print(board)
