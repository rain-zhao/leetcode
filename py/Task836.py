# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。

# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

# 给出两个矩形，判断它们是否重叠并返回结果。

# 示例 1：

# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# 输出：true
# 示例 2：

# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# 输出：false
# 说明：

# 两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
# 矩形中的所有坐标都处于 -10^9 和 10^9 之间。
from typing import List


class Solution:
    # 判断边界
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[3] <= rec2[1] or rec1[1] >= rec2[3])
    # 判断区域
    def isRectangleOverlap2(self, rec1: List[int], rec2: List[int]) -> bool:
        return max(rec1[0],rec2[0]) < min(rec1[2],rec2[2]) and max(rec1[1],rec2[1]) < min(rec1[3],rec2[3])
    

obj = Solution()
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(obj.isRectangleOverlap2(rec1,rec2))