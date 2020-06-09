# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

#  

# 示例 1:

# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
#  

# 提示：

# 0 <= num < 231


class Solution:
    def translateNum(self, num: int) -> str:
        if num < 10:
            return 1
        num = str(num)
        # define and init
        dp = [0] * len(num)
        dp[0] = 1
        dp[1] = 2 if int(num[:2]) < 26 else 1
        # loop
        for i in range(2,len(num)):
            dp[i] = dp[i-1]
            if num[i-1] != '0' and int(num[i-1:i+1]) < 26:
                dp[i] += dp[i-2]
        return dp[-1]


obj = Solution()
num = 12258
print(obj.translateNum(num))
