class Solution:

    def judgeCircle(self, moves: str) -> bool:
        mapping = {'U': (1, 0), 'D': (-1, 0), 'R': (0, -1), 'L': (0, 1)}
        x = y = 0
        for move in moves:
            dx, dy = mapping[move]
            x += dx
            y += dy
        return x == 0 and y == 0


moves = 'UD'
obj = Solution()
print(obj.judgeCircle(moves))
