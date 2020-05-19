class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str) -> bool:
            mid = len(s) >> 1
            return s[mid:][::-1].startswith(s[:mid])
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
        return True


obj = Solution()
s = "abca"
print(obj.validPalindrome(s))
