class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        self.idx = n-1

        def getWord() -> int:
            word = 0
            multi = 1
            while self.idx >= 0 and s[self.idx].isdigit():
                word += int(s[self.idx]) * multi
                multi *= 10
                self.idx -= 1
            return word

        def getStat() -> int:
            if self.idx == -1:
                return 0
            if s[self.idx] == ')':
                self.idx -= 1
                word = getStat()
            else:
                # if s[self.idx].isdigit():
                word = getWord()
            if self.idx == -1:
                return word
            if s[self.idx] == '(':
                self.idx -= 1
                return word
            if s[self.idx] == '-':
                self.idx -= 1
                return getStat() - word
            if s[self.idx] == '+':
                self.idx -= 1
                return getStat() + word
            return None
        return getStat()

    def calculate2(self, s: str) -> int:
        ops = [1]
        sign = 1
        i, n = 0, len(s)
        res = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                j = i+1
                while j < n and s[j].isdigit():
                    j += 1
                res += sign * int(s[i:j])
                i = j
        return res


s = "(1+(4+5+2)-3)+(6+8)"
obj = Solution()
print(obj.calculate2(s))
