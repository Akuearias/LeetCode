import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.randomized_set = {}

    def insert(self, val: int) -> bool:
        if val in self.randomized_set:
            return False
        self.randomized_set[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomized_set:
            return False
        dummy = self.nums[-1]
        id_ = self.randomized_set[val]
        self.nums[id_] = dummy
        self.randomized_set[dummy] = id_

        self.nums.pop()
        del self.randomized_set[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()