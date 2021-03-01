from collections import Counter


class Solution:
    # dfs 分治
    def longestSubstring(self, s: str, k: int) -> int:
        counter = Counter(s)
        for c in counter:
            if counter[c] < k:
                return max(self.longestSubstring(ss, k) for ss in s.split(c))
        return len(s)


s = "ababbc"
k = 2
obj = Solution()
print(obj.longestSubstring(s, k))
