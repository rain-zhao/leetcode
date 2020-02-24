class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        if not rowIndex:
            return [1]
        res = [1]
        for _ in range(rowIndex):
            # res = [1] + list(map(lambda pair: pair[0] +
            #                      pair[1], zip(res, res[1:]))) + [1]
            res = [1] + [i+j for (i, j) in zip(res, res[1:])] + [1]
        return res

    def getRow2(self, rowIndex: int) -> [int]:
        if not rowIndex:
            return [1]
        res = [1]+[0]*rowIndex
        for i in range(1, rowIndex+1):
            for k in range(i, 0, -1):
                res[k] = res[k]+res[k-1]
        return res


solution = Solution()
print(solution.getRow(3))
