class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        if not nums:
            return []
        cnts = {}
        for i in nums:
            cnts[i] = cnts.get(i, 0)+1
        items = tuple(cnts.items())
        res = []

        def dfs(seq, items, idx):
            if idx == len(items):
                res.append(seq)
                return
            key, val = items[idx]
            for i in range(val+1):
                dfs(seq+i*[key], items, idx+1)

        dfs([], items, 0)
        return res


nums = [1, 2, 2]
so = Solution()
print(so.subsetsWithDup(nums))
