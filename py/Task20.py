class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(ord(c))
            elif not stack or ord(c) - stack.pop() not in (1, 2):
                return False
        return not stack


s = "()[]{}"
obj = Solution()
print(obj.isValid(s))
