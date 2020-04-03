import re


class Solution:
    # fsm
    def myAtoi(self, str: str) -> int:
        class STATE:
            # trim space
            TRIM_SPACE = 0
            # sign
            SIGN = 1
            # number
            NUMBER = 2
            # terminal
            TERMINAL = 3

        state = STATE.TRIM_SPACE
        number = ''
        sign = ''
        idx = 0
        while idx < len(str):
            if state == STATE.TRIM_SPACE:
                if str[idx] == ' ':
                    idx += 1
                else:
                    state += 1
                continue
            elif state == STATE.SIGN:
                if str[idx] in ('-', '+'):
                    sign = str[idx]
                    idx += 1
                state += 1
                continue
            elif state == STATE.NUMBER:
                if 48 <= ord(str[idx]) <= 57:
                    number += str[idx]
                    idx += 1
                else:
                    state += 1
                continue
            elif state == STATE.TERMINAL:
                break
        if not number:
            number = '0'
        res = int(sign+number)
        if res < -2147483648:
            res = -2147483648
        if res > 2147483647:
            res = 2147483647
        return res

    # 内置函数
    def myAtoi2(self, str: str) -> int:
        match = re.match(r' *([+-]?\d+)', str)
        if not match:
            return 0
        return max(min(int(match.group(1)), 2147483647), -2147483648)

    def myAtoi3(self, str: str) -> int:
        return max(min(int(*re.findall(r'^ *([+-]?\d+)', str)), 2147483647), -2147483648)


obj = Solution()
str = "   -42 aaa"
print(obj.myAtoi(str))
