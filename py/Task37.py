from typing import List
from collections import defaultdict


class Solution:
    # dfs
    def solveSudoku(self, board: List[List[str]]) -> None:
        # init
        rowMap = defaultdict(lambda: 1)
        colMap = defaultdict(lambda: 1)
        blockMap = defaultdict(lambda: 1)
        transferMap = {2: '1', 4: '2', 8: '3', 16: '4',
                       32: '5', 64: '6', 128: '7', 256: '8', 512: '9'}

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                block = row // 3 * 3 + col // 3
                rowMap[row] |= 1 << int(board[row][col])
                colMap[col] |= 1 << int(board[row][col])
                blockMap[block] |= 1 << int(board[row][col])

        def dfs(i: int) -> bool:
            if i == 81:
                return True
            row = i // 9
            col = i % 9
            if board[row][col] != '.':
                return dfs(i+1)
            block = row // 3 * 3 + col // 3
            avals = 1023 & ~ (rowMap[row] | colMap[col] | blockMap[block])
            while avals:
                aval = avals & - avals
                avals &= avals - 1
                # process
                rowMap[row] |= aval
                colMap[col] |= aval
                blockMap[block] |= aval
                board[row][col] = transferMap[aval]
                # drill down
                if dfs(i+1):
                    return True
                # reverse
                rowMap[row] ^= aval
                colMap[col] ^= aval
                blockMap[block] ^= aval
                board[row][col] = '.'
            return False
        dfs(0)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

obj = Solution()
print(obj.solveSudoku(board))
