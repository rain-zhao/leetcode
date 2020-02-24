class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ''

        def gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        return str1[0:gcd(len(str1), len(str2))]
