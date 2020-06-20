class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        left, right = 0, len(s)-1

        while left < right:
            # valid left:
            cl = s[left]
            if not cl.isdigit() and not cl.isalpha():
                left += 1
                continue
            cr = s[right]
            if not cr.isdigit() and not cr.isalpha():
                right -= 1
                continue
            if cr != cl:
                return False
            left += 1
            right -= 1
        return True


obj = Solution()
s = "A man, a plan, a canal: Panama"
print(obj.isPalindrome(s))
