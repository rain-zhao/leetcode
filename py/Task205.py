class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i, j in zip(s, t):
            if i not in dict1 and j not in dict2:
                dict1[i], dict2[j] = j, i
            elif i in dict1 and j in dict2 and dict1[i] == j and dict2[j] == i:
                # match
                continue
            else:
                #not match
                return False
        return True
