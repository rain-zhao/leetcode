from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        self.res = None

        def dfs(idx: int, candidate: List[int]):
            # terminator
            if self.res:
                return
            if idx == n:
                if len(candidate) >= 3:
                    self.res = candidate
                return
            # process
            if len(candidate) < 2:
                if S[idx] == '0':
                    dfs(idx+1, candidate+[0])
                else:
                    for end in range(idx+1, n):
                        dfs(end, candidate+[int(S[idx:end])])
            else:
                target = candidate[-1] + candidate[-2]
                if target >= 2**31:
                    return
                targetStr = str(target)
                if S.startswith(targetStr, idx):
                    dfs(idx+len(targetStr), candidate+[target])
        dfs(0, [])
        return self.res


S = "123456579"
obj = Solution()
print(obj.splitIntoFibonacci(S))
