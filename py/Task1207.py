from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        s = set()
        for num in counter:
            if counter[num] in s:
                return False
            s.add(counter[num])
        return True


arr = [1,2]
obj = Solution()
print(obj.uniqueOccurrences(arr))
