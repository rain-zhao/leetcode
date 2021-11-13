import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return not not re.match(r'[A-Z]+|[a-z]+|[A-Z][a-z]+',word)
