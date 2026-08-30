# class Node:
#     def __init__(self, next=None, prev=None, data=None):
#         self.next = next
#         self.prev = prev
#         self.data = data

class LRUCache:
    # Optimized Approach = Dict for Cache + Doubly-LL to allow LRU
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # dict, since get/put must run in O(1)


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)   # remove & reinsert -> marks as most recently used
        self.cache[key] = val
        return val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key) # remove first so reinsertion refreshes recency
            self.cache[key] = value  # key exists, update value
        else:
            # key DNE, add (evict LRU if exceeds capacity)
            if len(self.cache) >= self.capacity:
                lru_key = next(iter(self.cache))
                self.cache.pop(lru_key) # evict
                # print(f"capacity {self.capacity} exceeded for PUT:{key}-{value}")
                # print(f"removed: {removedItem}")
            self.cache[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)