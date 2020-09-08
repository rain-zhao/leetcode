from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(nn: int, candidate: [int]):
            if len(candidate) == k:
                res.append(candidate)
                return
            for i in range(nn + 1, n-k+len(candidate)+2):
                dfs(i + 1, candidate + [i])
        dfs(1, [])
        return res

    def combine2(self, n, k):
        ans = []
        nums = [i for i in range(1, k + 1)] + [n+1]
        j = 0
        while(j < k):
            ans.append(nums[:k])
            j = 0
            while(j < k and nums[j+1] == nums[j] + 1):
                nums[j] = j+1
                j += 1
            nums[j] += 1
        return ans

    # dfs
    def combine3(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(nn: int, candidate: List[int]):
            # terminator
            if len(candidate) == k:
                res.append(candidate[:])
                return
            # 剩余可操作数量少于还需要数
            if n - nn + 1 < k - len(candidate):
                return
            # no choose
            dfs(nn + 1, candidate)
            # choose
            candidate.append(nn)
            dfs(nn + 1, candidate)
            candidate.pop()
        dfs(1, [])
        return res


n = 4
k = 2
so = Solution()
print(so.combine2(n, k))
