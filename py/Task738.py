# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

# （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

# 示例 1:

# 输入: N = 10
# 输出: 9
# 示例 2:

# 输入: N = 1234
# 输出: 1234
# 示例 3:

# 输入: N = 332
# 输出: 299
# 说明: N 是在 [0, 10^9] 范围内的一个整数。

import heapq


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        arr = [int(c) for c in str(N)]
        LEN = len(arr)
        i = 0
        while i < LEN-1 and arr[i] <= arr[i+1]:
            i += 1
        if i == LEN-1:
            return N
        while i > 0 and arr[i] == arr[i-1]:
            i -= 1
        return int(str(N)[:i]+str(arr[i]-1) + '9'*(LEN-i-1))

    def monotoneIncreasingDigits2(self, N: int) -> int:
        arr = [int(c) for c in str(N)]
        LEN = len(arr)
        idx = LEN
        for i in range(LEN-1, 0, -1):
            if arr[i] < arr[i-1]:
                arr[i-1] -= 1
                idx = i
        for i in range(idx, LEN):
            arr[i] = 9
        return int(''.join(str(i) for i in arr))


N = 120
obj = Solution()
print(obj.monotoneIncreasingDigits2(N))
