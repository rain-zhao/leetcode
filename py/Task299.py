class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        buckets = [0]*10
        for i, j in zip(secret, guess):
            if i == j:
                bull += 1
            else:
                buckets[ord(i)-48] += 1
                buckets[ord(j)-48] -= 1
        cow = len(secret) - sum((i for i in buckets if i > 0)) - bull
        return '{}A{}B'.format(bull, cow)


secret = "1807"
guess = "7810"
so = Solution()
print(so.getHint(secret, guess))
