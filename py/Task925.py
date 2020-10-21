import re


class Solution:
    # regex
    def isLongPressedName(self, name: str, typed: str) -> bool:
        return not not re.fullmatch('+'.join(name)+'+', typed)

    # 双指针 判断每个字母的连续出现的次数，if c1 > c2，则不符合
    def isLongPressedName2(self, name: str, typed: str) -> bool:
        m, n = len(name), len(typed)
        i = j = 0
        while i < m and j < n:
            chr1, chr2 = name[i], typed[j]
            if chr1 != chr2:
                return False
            c1 = 0
            while i < m and name[i] == chr1:
                i += 1
                c1 += 1
            c2 = 0
            while j < n and typed[j] == chr2:
                j += 1
                c2 += 1
            if c1 > c2:
                return False
        if i < m or j < n:
            return False
        return True

    # 双指针 optimize code typed 字母要么跟name字母相等，要么是长按（跟typed前一个字母相等）
    def isLongPressedName3(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]:
            return False
        i = j = 1
        m, n = len(name), len(typed)
        while j < n:
            if i < m and name[i] == typed[j]:
                i += 1
                j += 1
            elif typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        return i == m


name = "alex"
typed = "alexxr"
obj = Solution()
print(obj.isLongPressedName3(name, typed))
