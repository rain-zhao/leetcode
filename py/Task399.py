from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # hash
        n = 0
        map = {}
        for equation in equations:
            if equation[0] not in map:
                map[equation[0]] = n
                n += 1
            if equation[1] not in map:
                map[equation[1]] = n
                n += 1
        # define the dest table
        dests = [[-1] * n for _ in range(n)]
        # init
        for i in range(n):
            dests[i][i] = 1.0
        for equation, value in zip(equations, values):
            i, j = map[equation[0]], map[equation[1]]
            dests[i][j] = value
            dests[j][i] = 1/value

        # loop
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dests[i][k] != -1 and dests[k][j] != -1 and dests[i][j] == -1:
                        dests[i][j] = dests[i][k] * dests[k][j]

        # get res
        res = []
        for query in queries:
            if query[0] not in map or query[1] not in map:
                res.append(-1.0)
                continue
            i, j = map[query[0]], map[query[1]]
            res.append(dests[i][j])
        return res


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
obj = Solution()
print(obj.calcEquation(equations, values, queries))
