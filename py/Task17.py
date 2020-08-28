from typing import List


class Solution:
    # dfs
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        n = len(digits)

        def dfs(cur: int, candidate: str):
            # terminator
            if cur == n:
                res.append(candidate)
                return
            for c in mapping[digits[cur]]:
                dfs(cur + 1, candidate + c)
        dfs(0, '')
        return res


digits = "23"
obj = Solution()
print(obj.letterCombinations(digits))
