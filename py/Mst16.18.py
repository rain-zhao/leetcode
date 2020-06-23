import re


class Solution:
    # using reg-exps
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not pattern:
            return not value
        if len(pattern) == 1:
            return True   
        if pattern[0] == 'a':
            ga ,gb= '\\1','\\2'
        else:
            ga ,gb= '\\2','\\1'
        pattern = pattern.\
            replace('a', ga).\
            replace('b', gb).\
            replace('\\1', '(\\w*)', 1).\
            replace('\\2', '(\\w*)', 1) +\
            '$'
        match = re.match(pattern, value)
        if not match:
            return False
        groups = match.groups()
        return len(groups) == 1 or groups[0] != groups[1]


pattern = "bbb"
value = "xxxxxx"
obj = Solution()
print(obj.patternMatching(pattern, value))
