# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

# 示例:

# s = "3[a]2[bc]", 返回 "aaabcbc".
# s = "3[a2[c]]", 返回 "accaccacc".
# s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".


class Solution:
    # state machine
    def decodeString(self, s: str) -> str:
        numSet = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.idx = 0

        def decodeNext() -> str:
            multi = 0
            res = ''
            while self.idx < len(s):
                c = s[self.idx]
                self.idx += 1
                if c in numSet:
                    multi = 10 * multi + int(c)
                elif c == '[':
                    res += multi * decodeNext()
                    multi = 0
                elif c == ']':
                    return res
                else:
                    res += c
            return res
        return decodeNext()

    # stack
    def decodeString2(self, s: str) -> str:
        numSet = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        stack = []
        idx = 0
        while idx < len(s):
            c = s[idx]
            idx += 1
            if c == ']':
                multi = 0
                ans = ''
                while stack[-1] != '[':
                    c = stack.pop()
                    ans = c + ans
                stack.pop()
                shift = 1
                while stack and stack[-1] in numSet:
                    c = stack.pop()
                    multi += shift * int(c)
                    shift *= 10

                ans = multi * ans

                stack.append(ans)
            else:
                stack.append(c)

        return ''.join(stack)


s = "3[a]2[bc]"
obj = Solution()
print(obj.decodeString2(s))
