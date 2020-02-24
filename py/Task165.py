class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        versions1, versions2 = version1.split('.'), version2.split('.')
        versions1, versions2 = \
            versions1 + [0]*(len(versions2)-len(versions1)),\
            versions2 + [0]*(len(versions1)-len(versions2))
        for i, j in zip(versions1, versions2):
            if int(i) > int(j):
                return 1
            elif int(i) < int(j):
                return -1

        return 0


version1 = "7.5.3.0"
version2 = "7.5.3"
so = Solution()
print(so.compareVersion(version1, version2))
