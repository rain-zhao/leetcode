class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        t = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        chrs = list(s)
        while left < right:
            while left < right and chrs[left] not in t:
                left += 1
            while left < right and chrs[right] not in t:
                right -= 1
            if left < right:
                chrs[left], chrs[right] = chrs[right], chrs[left]
                left += 1
                right -= 1

        return ''.join(chrs)

    def reverseVowels2(self, s: str) -> str:
        left, right = 0, len(s)-1
        t = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        chrs = list(s)
        while left < right:
            if chrs[left] not in t:
                left += 1
                continue
            if chrs[right] not in t:
                right -= 1
                continue
            chrs[left], chrs[right] = chrs[right], chrs[left]
            left += 1
            right -= 1

        return ''.join(chrs)


s = "hello"
so = Solution()
print(so.reverseVowels(s))
