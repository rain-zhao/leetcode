class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        l = max(l1, l2)
        num1 = '0' * (l2 - l1) + num1
        num2 = '0' * (l1 - l2) + num2

        array = [0] * (l + 1)
        for i in range(l-1, -1, -1):
            d1, d2 = int(num1[i]), int(num2[i])
            result = d1 + d2 + array[i + 1]
            array[i] = result // 10
            array[i + 1] = result % 10

        startIdx = 0 if array[0] == 1 else 1
        return ''.join([str(array[i]) for i in range(startIdx, l + 1)])

    # 优化
    def addStrings2(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        l = max(l1, l2)
        num1 = '0' * (l2 - l1) + num1
        num2 = '0' * (l1 - l2) + num2
        array = []
        carry = 0
        for i in range(l-1, -1, -1):
            result = int(num1[i]) + int(num2[i]) + carry
            carry = result // 10
            array.append(str(result % 10))
        if carry:
            array.append('1')
        array.reverse()
        return ''.join(array)


num1 = '99'
num2 = '9'
obj = Solution()
print(obj.addStrings2(num1, num2))
