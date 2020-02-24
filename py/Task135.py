from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        candies = [1]*l
        for i in range(1, l):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
            else:
                for j in range(i, 0, -1):
                    if ratings[j] < ratings[j-1] and candies[j] >= candies[j-1]:
                        candies[j-1] = candies[j]+1
                    else:
                        break
        return sum(candies)

    def candy2(self, ratings: List[int]) -> int:
        l = len(ratings)
        candies = [1] * l
        for i in range(1, l):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        for i in range(l-1, 0, -1):
            if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i-1] = candies[i]+1
        return sum(candies)


so = Solution()
ratings = [1, 0, 2]
print(so.candy2(ratings))
