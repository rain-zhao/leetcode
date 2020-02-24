from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        tmp = arr[:]
        l = len(tmp)
        i, j = 0, 0
        while i < l:
            arr[i] = tmp[j]
            i += 1
            if tmp[j] == 0 and i < l:
                arr[i] = 0
                i += 1
            j += 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
so = Solution()
so.duplicateZeros(arr)
