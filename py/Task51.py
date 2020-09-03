from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(H: int, P: int, N: int, cnt: int, candidate: List[int]):
            # terminator
            if cnt == n:
                res.append(formatRes(candidate))
                return
            for i in range(n):
                p = 1 << i
                if p & (H | P | N):
                    continue
                # put i
                candidate.append(i)
                dfs(H | p, (P | p) << 1, (N | p) >> 1, cnt+1, candidate)
                # reverse
                candidate.pop()

        def formatRes(match: List[int]) -> List[str]:
            res = []
            for num in match:
                res.append('.' * num + 'Q' + '.' * (n - 1 - num))
            return res

        dfs(0, 0, 0, 0, [])
        return res

    # optimize code
    def solveNQueens2(self, n: int) -> List[List[str]]:
        res = []
        mask = (1 << n) - 1

        def dfs(H: int, P: int, N: int, row: int, candidate: List[int]):
            if row == n:
                res.append(format(candidate))
                return
            avaliables = mask & ~(H | P | N)
            while avaliables:
                pos = avaliables & -avaliables
                avaliables &= (avaliables-1)
                # drill down
                candidate.append(pos)
                dfs(H | pos, (P | pos) << 1, (N | pos) >> 1, row + 1, candidate)
                # reverse
                candidate.pop()

        def format(match: List[int]):
            res = []
            add = 1 << n
            for pos in match:
                res.append(bin(add | pos)[3:].replace(
                    '0', '.').replace('1', 'Q'))
            return res
        dfs(0, 0, 0, 0, [])

        return res


n = 4
obj = Solution()
print(obj.solveNQueens2(n))
