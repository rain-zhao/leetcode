class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        for i in s.split():
            res = i+' '+res

        return res[:-1]

    def reverseWords2(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
