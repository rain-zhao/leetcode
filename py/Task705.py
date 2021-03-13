from collections import defaultdict
from typing import DefaultDict


class MyHashSet:

    def __init__(self):
        # init size is 8
        self.length = 0
        self.table = [[] for _ in range(8)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.length += 1
        if self.length / len(self.table) > 0.75:
            self.rehash()
        self.table[key % len(self.table)].append(key)

    def remove(self, key: int) -> None:
        idx = key % len(self.table)
        for i, ii in enumerate(self.table[idx]):
            if ii == key:
                del self.table[idx][i]
                return

    def contains(self, key: int) -> bool:
        idx = key % len(self.table)
        for ii in self.table[idx]:
            if ii == key:
                return True
        return False

    def rehash(self):
        size = len(self.table) << 1
        tmpTable = [[] for _ in range(size)]
        for ll in self.table:
            for ii in ll:
                tmpTable[ii % size].append(ii)
        self.table = tmpTable


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(9)
obj.remove(9)
param_3 = obj.contains(9)
