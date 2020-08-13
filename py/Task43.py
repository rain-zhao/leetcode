class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        l1, l2 = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (l1 + l2)
        for i in range(l1):
            d1 = int(num1[i])
            for j in range(l2):
                d2 = int(num2[j])
                pos = i + j
                res[pos + 1] += (res[pos] + d1 * d2) // 10
                res[pos] = (res[pos] + d1 * d2) % 10
        # print to str
        if res[-1] == 0:
            res = res[:-1]
        res = ''.join([str(d) for d in res[::-1]])
        return res


num1 = "123"
num2 = "456"
obj = Solution()
print(obj.multiply(num1, num2))
