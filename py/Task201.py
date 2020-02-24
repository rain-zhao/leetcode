class Solution:
    # 基本 O(n)
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = m
        for i in range(m, n+1):
            res = res & i
        return res

    # 位运算 最低位
    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        res = m
        while res > 0:
            # 最低位0
            lowbit = res & -res
            if res + lowbit <= n:
                res = res & (res + lowbit)
            else:
                return res
        return res

    # 位运算
    def rangeBitwiseAnd3(self, m: int, n: int) -> int:
        while m < n:
            n = n & (n-1)
        return n


obj = Solution()
m = 5
n = 8
print(obj.rangeBitwiseAnd(m, n))
