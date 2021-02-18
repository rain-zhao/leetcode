from typing import List


class Solution:
    # brute force
    def minKBitFlips(self, A: List[int], K: int) -> int:
        if K == 1:
            return len(A) - sum(A)
        N = len(A)
        res = 0
        for i in range(N - K + 1):
            if A[i] == 0:
                for j in range(i, i+K):
                    A[j] ^= 1
                res += 1
        for i in range(N - K + 1, N):
            if A[i] == 0:
                return -1
        return res

    # silde window
    # 用队列记录翻转次数
    def minKBitFlips2(self, A: List[int], K: int) -> int:
        from collections import deque
        N = len(A)
        dq = deque()
        res = 0
        for i in range(N):
            if dq and dq[0] == i - K:
                dq.popleft()
            # 是偶数代表这个位置要翻转
            if not (len(dq) + A[i]) & 1:
                if i > N - K:
                    return -1
                dq.append(i)
                res += 1
        return res

    # 差分数组
    def minKBitFlips3(self, A: List[int], K: int) -> int:
        N = len(A)
        diffs = [0 for _ in range(N+1)]
        res = swapCnt = 0
        for i in range(N):
            swapCnt += diffs[i]
            if not (swapCnt + A[i]) & 1:
                if i > N - K:
                    return -1
                res += 1
                swapCnt += 1
                diffs[i + K] -= 1
        return res


A = [0, 0, 0, 1, 0, 1, 1, 0]
K = 3
obj = Solution()
print(obj.minKBitFlips3(A, K))
