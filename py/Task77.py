class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        def dfs(res: [[int]], l: [int]) -> None:
            if len(l) == k:
                res.append(l)
                return
            start = 1 if not l else l[-1]+1
            for i in range(start, n-k+len(l)+2):
                dfs(res,l+[i])
        
        res = []
        dfs(res,[])
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

n = 4
k=2
so = Solution()
print(so.combine(n,k))
            
