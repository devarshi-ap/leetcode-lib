import random

class RandomizedSet:

    def __init__(self):
        self.nums = [] # for reading
        self.pos_map = {} # for O(1) random [same state as nums] [element -> index]

    def insert(self, val: int) -> bool:
        # Insert value (add to nums + update pos_map).
        # Returns True if it was new, False if already present.
        if val in self.pos_map:
            return False
        
        self.pos_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        # Remove value (get idx of val from pos_map, swap with last element, pop from both).
        # Returns True if it was new, False otherwise.
        if val not in self.pos_map:
            return False

        # 1. Locate the item to delete and the item currently at the end
        idx_to_remove = self.pos_map[val]
        last_element = self.nums[-1]
        
        # 2. Move the last element into the gap of the deleted item
        self.nums[idx_to_remove] = last_element
        self.pos_map[last_element] = idx_to_remove
        
        # 3. Clean up the duplicate trailing item from list and remove from dict
        self.nums.pop()
        del self.pos_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()