# 1024专题。四个状态码加减乘除组合成1024

from typing import List


class Solution:
    def calcCode(self, codes: List[int]) -> str:
        def dfs(codes: List[int], target: int) -> List:
            if not codes:
                return [False, '']
            n = len(codes)
            if n == 1:
                return [codes[0] == target, str(target)]
            for i in range(n):
                code = codes[i]
                remains = codes[:i]+codes[i+1:]
                #  multi
                fit, res = dfs(remains, target / code)
                if fit:
                    return [True, str(code)+'*('+res+')']
                # divide
                fit, res = dfs(remains, code / target)
                if fit:
                    return [True, str(code)+'/('+res+')']
                # plus
                fit, res = dfs(remains, target - code)
                if fit:
                    return [True, str(code)+'+('+res+')']
                # minus
                fit, res = dfs(remains, target + code)
                if fit:
                    return [True, str(code)+'-('+res+')']
            return [False, '']

        _, res = dfs(codes, 1024)
        return res


obj = Solution()
codes = [304, 400, 200, 416]
print(obj.calcCode(codes))
