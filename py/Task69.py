# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根，其中 x 是非负整数。

# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 示例 1:

# 输入: 4
# 输出: 2
# 示例 2:

# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。


class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        left, right = 0, x
        while left <= right:
            mid = (left + right) >> 1
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


x = 8
obj = Solution()
print(obj.mySqrt(x))
