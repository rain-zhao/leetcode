from typing import List


class Solution:
    # dp
    def findLength(self, A: List[int], B: List[int]) -> int:
        # if not A or not B:
        #     return 0
        m = len(A)
        n = len(B)

        # define and init
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
        return res

    # dp & 空间压缩
    def findLength2(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)

        dp = [0] * n
        res = 0

        for i in range(m):
            pre = 0
            for j in range(n):
                tmp = dp[j]
                if A[i] == B[j]:
                    dp[j] = pre + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
                pre = tmp

        return res

    # slide window
    def findLength3(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        res = 0
        # 对齐B
        for i in range(n):
            k = 0
            for j in range(i, min(n, m + i)):
                if A[j - i] == B[j]:
                    k += 1
                    res = max(res, k)
                else:
                    k = 0
        # 对齐A
        for i in range(1, m):
            k = 0
            for j in range(i, min(m, n + i)):
                if A[j] == B[j - i]:
                    k += 1
                    res = max(res, k)
                else:
                    k = 0
        return res

    # slide window 优化写法
    def findLength4(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        res = 0

        def findMax(shiftA: int, shiftB: int, l: int) -> int:
            res = 0
            k = 0
            for i in range(l):
                if A[shiftA + i] == B[shiftB + i]:
                    k += 1
                    res = max(res, k)
                else:
                    k = 0
            return res
        # 对齐B
        for i in range(n):
            res = max(res, findMax(0, i, min(m, n - i)))
        # 对齐A
        for i in range(1, m):
            res = max(res, findMax(i, 0, min(m - i, n)))
        return res


A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
obj = Solution()
print(obj.findLength3(A, B))
