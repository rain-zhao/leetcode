class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def translate(S: str) -> str:
            stack = []
            for c in S:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return translate(S) == translate(T)


S = "ab#c"
T = "ad#c"
obj = Solution()
print(obj.backspaceCompare(S, T))
