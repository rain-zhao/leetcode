# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:

# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:

# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# 输出: 5

# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
# 示例 2:

# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# 输出: 0

# 解释: endWord "cog" 不在字典中，所以无法进行转换。

from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    # bfs
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def similar(src, target):
            return sum([1 for a, b in zip(src, target) if a != b]) == 1

        wordSet = set(wordList)
        queue = [beginWord]
        cnt = 1
        beg = end = 0
        while end < len(queue):
            beg, end = end, len(queue)
            cnt += 1
            for i in range(beg, end):
                for word in set(wordSet):
                    if similar(queue[i], word):
                        if word == endWord:
                            return cnt
                        queue.append(word)
                        wordSet.remove(word)
        return 0

    # copy
    def ladderLength2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

    # bfs 预处理
    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)
        comboDict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                comboDict[word[:i]+'*'+word[i+1:]].append(word)
        queue = [beginWord]
        cnt = 1
        beg = end = 0
        visited = {beginWord}
        while end < len(queue):
            beg, end = end, len(queue)
            cnt += 1
            for i in range(beg, end):
                currWord = queue[i]
                for k in range(L):
                    interWord = currWord[:k]+'*'+currWord[k+1:]
                    for word in comboDict[interWord]:
                        if word == endWord:
                            return cnt
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)
        return 0

    # bfs 预处理 双向
    def ladderLength4(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        def _helper(queue, visited, visited_other):
            currWord, level = queue.popleft()
            for i in range(L):
                interWord = currWord[:i]+'*'+currWord[i+1:]
                for word in comboDict[interWord]:
                    if word in visited_other:
                        return level + visited_other[word]
                    if word not in visited:
                        queue.append((word, level+1))
                        visited[word] = level+1
            return 0
        L = len(beginWord)
        comboDict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                comboDict[word[:i]+'*'+word[i+1:]].append(word)

        queue_begin = deque([(beginWord, 1)])  # BFS starting from beginWord
        queue_end = deque([(endWord, 1)])  # BFS starting from endWord

        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        while queue_begin and queue_end:
            ans1 = _helper(queue_begin, visited_begin, visited_end)
            if ans1:
                return ans1
            ans2 = _helper(queue_end, visited_end, visited_begin)
            if ans2:
                return ans2

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
obj = Solution()
print(obj.ladderLength4(beginWord, endWord, wordList))
