# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:

# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:

# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# 输出:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# 示例 2:

# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# 输出: []

# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
from typing import List
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        # 预处理
        L = len(beginWord)
        comboDict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                comboDict[word[:i]+'*'+word[i+1:]].append(word)

        res = []

        def dfs(visited: set, candidate: List[str]):
            # last word is the transfer word
            currWord = candidate[-1]
            # terminator
            if res:
                if len(res[0]) < len(candidate):
                    return
                if currWord == endWord:
                    if len(res[0]) > len(candidate):
                        res.clear()
                    res.append(candidate[:])
                    return
            if currWord == endWord:
                res.append(candidate[:])
                return

            for i in range(L):
                interWord = currWord[:i]+'*'+currWord[i+1:]
                for word in comboDict[interWord]:
                    if word not in visited:
                        # add word to list
                        visited.add(word)
                        candidate.append(word)
                        # drill down
                        dfs(visited, candidate)
                        # reverse
                        visited.remove(word)
                        candidate.pop()

        dfs(set([beginWord]), [beginWord])
        return res

    # bfs
    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        # 预处理
        L = len(beginWord)
        comboDict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                comboDict[word[:i]+'*'+word[i+1:]].append(word)

        res = []
        candidate = [[beginWord]]
        while not res and candidate:
            tmpList = []
            for wordList in candidate:
                currWord = wordList[-1]
                for i in range(L):
                    interWord = currWord[:i]+'*'+currWord[i+1:]
                    for word in comboDict[interWord]:
                        if word == endWord:
                            res.append(wordList+[word])
                            continue
                        if word not in wordList:
                            tmpList.append(wordList+[word])
            candidate = tmpList

        return res


beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]
obj = Solution()
print(obj.findLadders2(beginWord, endWord, wordList))
