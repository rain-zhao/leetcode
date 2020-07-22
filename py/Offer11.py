# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

# 示例 1：

# 输入：[3,4,5,1,2]
# 输出：1
# 示例 2：

# 输入：[2,2,2,0,1]
# 输出：0


from typing import List


class Solution:
    # binary-search
    def minArray(self, numbers: List[int]) -> int:
        if numbers[0] < numbers[-1]:
            return numbers[0]
        if (l:=len(numbers)) == 1:
            return numbers[0]
        left, right = 0, l - 1
        while left <= right:
            mid = (left + right) >> 1
            if numbers[mid] < numbers[mid - 1]:
                return numbers[mid]
            elif numbers[mid] == numbers[right]:
                right -= 1
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid - 1
        return numbers[right]

    # 线性搜索第一个为止小于前一位置
    def minArray2(self, numbers: List[int]) -> int:
        for num1, num2 in zip(numbers, numbers[1:]):
            if num1 > num2:
                return num2
        return numbers[0]


obj = Solution()
numbers = [10, 1, 10, 10, 10]
print(obj.minArray(numbers))
