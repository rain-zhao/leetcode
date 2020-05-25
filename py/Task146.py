
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            val = self.map[key]
            del self.map[key]
            self.map[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            del self.map[key]
        self.map[key] = value
        if len(self.map) > self.capacity:
            it = iter(self.map)
            del self.map[next(it)]

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
