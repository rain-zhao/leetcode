# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

#  

# 示例：

# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]

from typing import List


class Solution:
    # dfs
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def _dfs(left: int, right: int, str: str) -> None:
            # ternimate
            if not left and not right:
                res.append(str)
                return
            if left:
                _dfs(left-1, right, str+'(')
            if right > left:
                _dfs(left, right-1, str+')')
        _dfs(n, n, '')
        return res


obj = Solution()
n = 3
print(obj.generateParenthesis(n))
