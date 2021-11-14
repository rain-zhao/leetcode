from collections import defaultdict


class MapSum:

    def __init__(self):
        self.root = [None] * 26 + [0]
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map[key]
        self.map[key] = val
        if not delta:
            return
        cur = self.root
        for c in key:
            idx = ord(c) - 97
            if not cur[idx]:
                cur[idx] = [None] * 26 + [0]
            cur = cur[idx]
            cur[-1] += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            idx = ord(c) - 97
            if not cur[idx]:
                return 0
            cur = cur[idx]
        return cur[-1]


# Your MapSum object will be instantiated and called as such:
obj = MapSum()

obj.insert("apple", 3)
print(obj.sum("ap"))
obj.insert("app", 2)
obj.insert("apple", 2)
print(obj.sum("ap"))
