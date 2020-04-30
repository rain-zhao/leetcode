# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """


class MountainArray:
    def __init__(self, array):
        self.array = array
        super().__init__()

    def get(self, index: int) -> int:
        return self.array[index]

    def length(self) -> int:
        return len(self.array)


class Solution:
    # 直接二分比较，递归
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        def find(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = (left+right) >> 1
            if mid == left or mountain_arr.get(mid) > mountain_arr.get(mid-1):
                res = findAsc(left, mid)
                if res != -1:
                    return res
                return find(mid+1, right)
            else:
                res = find(left, mid)
                if res != -1:
                    return res
                return findDesc(mid+1, right)

        def findAsc(left: int, right: int) -> int:
            if mountain_arr.get(right) < target:
                return -1
            while left <= right:
                mid = (left+right) >> 1

                midVal = mountain_arr.get(mid)
                if midVal == target:
                    return mid
                elif midVal < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def findDesc(left: int, right: int) -> int:
            if mountain_arr.get(left) < target:
                return -1
            while left <= right:
                mid = (left+right) >> 1
                midVal = mountain_arr.get(mid)
                if midVal == target:
                    return mid
                elif midVal > target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        return find(0, mountain_arr.length()-1)

    # 先找出peak，再分成两part
    def findInMountainArray2(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binarySearch(left: int, right: int, compartor=lambda x, y: x < y) -> int:
            while left <= right:
                mid = (left+right) >> 1
                midVal = mountain_arr.get(mid)
                if midVal == target:
                    return mid
                elif compartor(midVal, target):
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        # find peak
        left, right = 1, mountain_arr.length()-2
        while left <= right:
            mid = (left+right) >> 1
            if mountain_arr.get(mid) > mountain_arr.get(mid-1):
                left = mid + 1
            else:
                right = mid - 1

        peak = right

        res = binarySearch(0, peak)
        if res != -1:
            return res
        return binarySearch(peak+1, mountain_arr.length()-1, lambda x, y: x > y)


array = [1, 2, 3, 4, 5, 3, 1]
target = 3
obj = Solution()
mountain_arr = MountainArray(array)
print(obj.findInMountainArray2(target, mountain_arr))
