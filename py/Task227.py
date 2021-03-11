class Solution:
    def calculate(self, s: str) -> int:
        i, n = 0, len(s)
        stack = []
        sign = '+'
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] in ('+', '-', '/', '*'):
                sign = s[i]
                i += 1
            else:
                j = i+1
                while j < n and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                elif sign == '*':
                    stack[-1] *= num
                i = j
        return sum(stack)


s = "14-3/2"
obj = Solution()
print(obj.calculate(s))
