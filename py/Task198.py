class Solution:
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # init
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [0, nums[0]]

        for i, num in enumerate(nums[1:], 1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0]+num

        return max(dp[-1][0], dp[-1][1])

    def rob2(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # init
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i, num in enumerate(nums[2:], 2):
            dp[i] = max(dp[i-2]+num, dp[i-1])

        return dp[-1]

    def rob3(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # init
        do = nums[0]
        nodo = 0

        # loop
        for num in nums[1:]:
            do, nodo = nodo + num, max(do, nodo)

        return max(do, nodo)

    def rob4(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # init
        fst = nums[0]
        sed = max(nums[0], nums[1])

        # loop
        for num in nums[2:]:
            fst, sed = sed, max(fst + num, sed)

        return sed
