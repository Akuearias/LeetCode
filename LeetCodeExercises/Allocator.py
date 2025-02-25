class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.memoryList = ["_"] * n

    def allocate(self, size: int, mID: int) -> int:
        count, l = 0, 0
        for r in range(self.n):
            if self.memoryList[r] == '_':
                count += 1
                if count == size:
                    for i in range(l, l + size):
                        self.memoryList[i] = mID
                    return l
            else:
                count = 0
                l = r + 1
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(len(self.memoryList)):
            if self.memoryList[i] == mID:
                self.memoryList[i] = "_"
                freed += 1
        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)

if __name__ == "__main__":
    allocator = Allocator(10)
    print(allocator.allocate(1, 1))
    print(allocator.allocate(1, 2))