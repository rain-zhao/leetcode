# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

# 你可以返回任何满足上述条件的数组作为答案。

#  

# 示例：

# 输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#  

# 提示：

# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000


from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        idxOdd, idxEven = 1, 0
        res = [None] * n
        for num in A:
            if num & 1:
                res[idxOdd] = num
                idxOdd += 2
            else:
                res[idxEven] = num
                idxEven += 2
        return res

    # swap in-place
    def sortArrayByParityII2(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] & 1:
                while A[j] & 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


A = [4, 2, 5, 7]
obj = Solution()
print(obj.sortArrayByParityII2(A))
