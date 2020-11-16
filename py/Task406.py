from typing import List
from operator import itemgetter


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        res = [None] * n
        for person in people:
            i, k = -1, person[1]
            while k >= 0:
                i += 1
                if not res[i]:
                    k -= 1
            res[i] = person
        return res

    # 从大到小排序后直接插入数组
    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for person in people:
            res.insert(person[1], person)
        return res


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
obj = Solution()
print(obj.reconstructQueue2(people))
