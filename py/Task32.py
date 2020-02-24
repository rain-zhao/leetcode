# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

# 示例 1:

# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:

# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"


class Solution:
    # stack
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0
        res = 0
        stack = [-1]
        for idx, c in enumerate(s):
            if c == '(':
                stack.append(idx)
            else:
                if len(stack) == 1:
                    stack[0] = idx
                else:
                    stack.pop()
                    res = max(res, idx - stack[-1])
        return res

    # dp
    def longestValidParentheses2(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0

        res = 0
        # define and init
        dp = [0] * (len(s)+1)

        for idx in range(1, len(s)):
            if s[idx] == ')':
                if s[idx-1] == '(':
                    dp[idx+1] = dp[idx-1]+2
                else:
                    if dp[idx] > 0:
                        prefix = idx - dp[idx]-1
                        if prefix >= 0 and s[prefix] == '(':
                            dp[idx+1] = dp[prefix] + idx - prefix + 1
            res = max(res, dp[idx+1])
        return res

    # left and right
    def longestValidParentheses3(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0
        res = 0

        def traversal(s: str):
            nonlocal res
            left = right = 0
            for c in s:
                if c == '(':
                    left += 1
                else:
                    right += 1
                if left == right:
                    res = max(res, right*2)
                elif left < right:
                    left = right = 0

        # left to right
        traversal(s)
        # right to left
        traversal(s[::-1].replace('(','{').replace(')','(').replace('{',')'))

        return res


s = "(()"
obj = Solution()
print(obj.longestValidParentheses3(s))
