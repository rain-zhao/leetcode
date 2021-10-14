from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr)-2
        while l <= r:
            mid = (l+r) >> 1
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        return l
