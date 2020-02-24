from typing import List
import sys


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        min_val = None
        max_val = None
        mode, mode_cnt = 0, 0
        total_cnt = 0
        sum = 0
        for idx, cnt in enumerate(count):
            if cnt:
                if min_val == None:
                    min_val = idx
                max_val = idx
                if cnt > mode_cnt:
                    mode_cnt = cnt
                    mode = idx
                total_cnt += cnt
                sum += idx*cnt
        avg = sum / total_cnt
        # mid:
        cur_cnt = 0
        mid = 0
        for idx, cnt in enumerate(count):
            cur_cnt += cnt
            if cur_cnt << 1 > total_cnt:
                mid = idx
                break
            elif not total_cnt & 1 and cur_cnt << 1 == total_cnt:
                idx2 = idx+1
                while not count[idx2]:
                    idx2 += 1
                mid = (idx+idx2)/2
                break
        return [min_val, max_val, avg, mid, mode]
        # return [float(min_val), float(max_val), avg, float(mid), float(mode)]
count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
so = Solution()
print(so.sampleStats(count))