from typing import List


class Solution:
    # brute force
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        res = [-1] * len(requirements)
        total = [0, 0, 0]
        for jidx, j in enumerate(requirements):
            if j[0] <= total[0] and j[1] <= total[1] and j[2] <= total[2]:
                res[jidx] = 0
        for iidx, i in enumerate(increase):
            total[0] += i[0]
            total[1] += i[1]
            total[2] += i[2]
            for jidx, j in enumerate(requirements):
                if res[jidx] != -1:
                    continue
                if j[0] <= total[0] and j[1] <= total[1] and j[2] <= total[2]:
                    res[jidx] = iidx + 1
        return res

    # requirements分别排序
    def getTriggerTime2(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        res = [-1] * len(requirements)
        total = [(0, 0, 0)]
        c_sort = []
        r_sort = []
        h_sort = []
        sub_res = [[-1, -1, -1] for _ in range(len(requirements))]
        for i in increase:
            cur = (total[-1][0]+i[0], total[-1][1]+i[1], total[-1][2]+i[2])
            total.append(cur)
        for idx, j in enumerate(requirements):
            c_sort.append((j[0], idx))
            r_sort.append((j[1], idx))
            h_sort.append((j[2], idx))
        c_sort.sort()
        r_sort.sort()
        h_sort.sort()
        pc = pr = ph = 0
        for i in range(len(total)):
            while pc < len(requirements) and c_sort[pc][0] <= total[i][0]:
                sub_res[c_sort[pc][1]][0] = i
                pc += 1
            while pr < len(requirements) and r_sort[pr][0] <= total[i][1]:
                sub_res[r_sort[pr][1]][1] = i
                pr += 1
            while ph < len(requirements) and h_sort[ph][0] <= total[i][2]:
                sub_res[h_sort[ph][1]][2] = i
                ph += 1
        for i in range(len(requirements)):
            if sub_res[i][0] == -1 or sub_res[i][1] == -1 or sub_res[i][2] == -1:
                continue
            res[i] = max(sub_res[i][0], sub_res[i][1], sub_res[i][2])

        return res

    # requirements二分法
    def getTriggerTime3(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        n, k = len(increase), len(requirements)
        res = [-1] * len(requirements)
        total = [[0, 0, 0]]
        for i in range(n):
            sub_total = total[-1][:]
            for j in range(3):
                sub_total[j] += increase[i][j]
            total.append(sub_total)
        for i in range(k):
            req = requirements[i]
            left, right = 0, n
            while left <= right:
                mid = (left + right) >> 1
                day_total = total[mid]
                trigger = sum([1 for p, q in zip(req, day_total) if p <= q])
                if trigger == 3:
                    right = mid - 1
                else:
                    left = mid + 1
            if left != n + 1:
                res[i] = left
        return res


increase = [[2, 8, 4], [2, 5, 0], [10, 9, 8]]
requirements = [[2, 11, 3], [15, 10, 7], [9, 17, 12], [8, 1, 14]]
obj = Solution()
print(obj.getTriggerTime3(increase, requirements))
