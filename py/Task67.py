class Solution:
    """     
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a),len(b))
        a = '0'*(maxlen - len(a))+a
        b = '0'*(maxlen - len(b))+b

        res = ''
        carry = 0
        for i in range(maxlen-1,-1,-1):
            res = str((int(a[i])+int(b[i])+carry) % 2)+res
            carry = int(a[i])+int(b[i])+carry >> 1

        if carry:
            res = '1'+res
        return res 
    """

    def addBinary(self, a: str, b: str) -> str:
        diff = len(a) - len(b)
        a = '0' * -diff + a
        b = '0' * diff + b
        res, carry = '', 0
        for i, j in zip(a[::-1], b[::-1]):
            sum = int(i) + int(j) + carry
            res = str(sum % 2) + res
            carry = sum >> 1
        if carry:
            res = '1'+res
        return res

    def addBinary2(self, a: str, b: str) -> str:
        diff = len(a) - len(b)
        a = '0' * -diff + a
        b = '0' * diff + b
        carry = 0
        res = ''
        for i, j in zip(a[::-1], b[::-1]):
            sum = int(i) + int(j) + carry
            res = str(sum & 1) + res
            carry = sum >> 1
        if carry:
            res = '1' + res
        return res


solution = Solution()
a = "111"
b = "11"
print(solution.addBinary2(a, b))
