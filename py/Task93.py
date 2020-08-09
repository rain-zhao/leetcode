class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        l = len(s)
        res = []

        def dfs(list, idx):
            # terminator
            if idx == l or len(list) == 4:
                if l == idx and len(list) == 4:
                    res.append('.'.join(list))
                return
            # 1 bit
            list.append(s[idx])
            dfs(list, idx+1)
            list.pop()
            if '0' != s[idx]:
                # 2 bit
                if l > idx+1:
                    list.append(s[idx:idx+2])
                    dfs(list, idx+2)
                    list.pop()
                # 3 bit
                if l > idx+2 and int(s[idx:idx+3]) <= 255:
                    list.append(s[idx:idx+3])
                    dfs(list, idx+3)
                    list.pop()
        dfs([], 0)
        return res

    def restoreIpAddresses2(self, s: str) -> [str]:
        l = len(s)
        res = []

        def dfs(list, idx):
                # terminator
            if idx == l or len(list) == 4:
                if l == idx and len(list) == 4:
                    res.append('.'.join(list))
                return
            # back track
            list.append(s[idx])
            dfs(list, idx+1)
            list.pop()
            if '0' != s[idx]:
                for i in (idx+2, idx+3):
                    if i <= l and int(s[idx:i]) <= 255:
                        list.append(s[idx:i])
                        dfs(list, i)
                        list.pop()
        dfs([], 0)
        return res

    # dfs 2020m-08-09
    def restoreIpAddresses3(self, s: str) -> [str]:
        l = len(s)
        res = []

        def dfs(idx: int, sList: list):
            # terminator
            if idx == l and len(sList) == 4:
                res.append('.'.join(sList))
                return
            if idx == l or len(sList) == 4:
                return

            # 1 bit
            sList.append(s[idx])
            dfs(idx+1, sList)
            sList.pop()
            # 2 or 3 bit
            if s[idx] == '0':
                return
            for i in (idx + 2, idx + 3):
                if i <= l and int(s[idx:i]) <= 255:
                    sList.append(s[idx:i])
                    dfs(i, sList)
                    sList.pop()
        dfs(0, [])
        return res


s = "25525511135"
obj = Solution()
print(obj.restoreIpAddresses3(s))
