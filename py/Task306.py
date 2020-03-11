# 累加数是一个字符串，组成它的数字可以形成累加序列。

# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

# 示例 1:

# 输入: "112358"
# 输出: true
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 示例 2:

# 输入: "199100199"
# 输出: true
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
# 进阶:
# 你如何处理一个溢出的过大的整数输入?


class Solution:
    # 迭代
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False

        def check(fst: int, sed: int, start: int) -> bool:
            while start != len(num):
                # 不可能出现0开头，不用检查
                thrd = fst + sed
                thrdStr = str(thrd)
                if num.startswith(thrdStr, start):
                    start += len(thrdStr)
                    fst, sed = sed, thrd
                else:
                    return False
            return True
        # 第一个数字位数最小为1位，最大为(len(num)-1)//2
        for i in range(1, (len(num)+1)//2):
            fst = num[:i]
            # 检查0开头
            if len(fst) > 1 and fst[0] == '0':
                continue 
            # 第二个数字位数最小为1位，最大为(len(num)-i)//2
            for j in range(i+1, (len(num)-i)//2+i+1):
                sed = num[i:j]
                # 检查0开头
                if len(sed) > 1 and sed[0] == '0':
                    continue 
                if check(int(fst), int(sed), j):
                    return True
        return False


num = "123"
obj = Solution()
print(obj.isAdditiveNumber(num))
