class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]


obj = Solution()
x = 123454321
print(obj.isPalindrome(x))
