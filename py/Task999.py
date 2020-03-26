from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find rook
        rook = (-1, -1)
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook = (i, j)
                    break

        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))
        res = 0
        for x, y in direct:
            dx, dy = rook[0]+x, rook[1]+y
            while 0 <= dx < 8 and 0 <= dy < 8:
                if board[dx][dy] == 'B':
                    break
                if board[dx][dy] == 'p':
                    res += 1
                    break
                dx, dy = dx + x, dy + y

        return res


board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."], [
    ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
obj = Solution()
print(obj.numRookCaptures(board))
