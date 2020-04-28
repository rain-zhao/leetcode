# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

#  

# 示例 1：

# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
# 示例 2：

# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]
#  

# 限制：

# 2 <= nums <= 10000

from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return list(s)

    def singleNumbers2(self, nums: List[int]) -> List[int]:
        bits = 0
        for num in nums:
            bits ^= num

        bit = bits & -bits

        a = b = 0
        for num in nums:
            if num & bit:
                a ^= num
            else:
                b ^= num

        return [a, b]


nums = [1, 2, 10, 4, 1, 4, 3, 3]
obj = Solution()
print(obj.singleNumbers2(nums))
