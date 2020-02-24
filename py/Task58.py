class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if not s:
            return 0
        return len(s.split()[-1])

solution = Solution()
print(solution.lengthOfLastWord("hello world "))