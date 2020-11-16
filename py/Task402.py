class Solution:
    # dp (not ac)
    def removeKdigits(self, num: str, k: int) -> str:
        # dp[i][j] = 以第i个数字结尾的去掉了j个数字的数字最小值
        if not num or not k:
            return num
        n = len(num)
        # define
        dp = [[0] * (k+1) for _ in range(n+1)]
        # init
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0] * 10 + int(num[i-1])
        # loop
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = min(dp[i-1][j] * 10 + int(num[i-1]), dp[i-1][j-1])
        return str(dp[n][k])

    # dp 压缩空间 (not ac)
    def removeKdigits2(self, num: str, k: int) -> str:
        if not num or not k:
            return num
        n = len(num)
        dp = [0] * (k+1)
        for i in range(1, n+1):
            for j in range(k, 0, -1):
                dp[j] = min(dp[j] * 10 + int(num[i-1]), dp[j-1])
            dp[0] = dp[0] * 10 + int(num[i-1])
        return str(dp[k])

    # 单调数组 (ac)
    def removeKdigits3(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # pop last of stack
        for _ in range(k):
            stack.pop()
        # pop '0''s prefix
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        return '0' if i == len(stack) else ''.join(stack[i:])


num = "10"
k = 2
obj = Solution()
print(obj.removeKdigits3(num, k))
