import heapq
# https://leetcode.cn/problems/find-median-from-data-stream/solutions/961062/shu-ju-liu-de-zhong-wei-shu-by-leetcode-ktkst


class MedianFinder:
    def __init__(self):
        self.min_ = []
        self.max_ = []

    def addNum(self, num: int) -> None:
        if not self.min_ or num <= -self.min_[0]:
            heapq.heappush(self.min_, -num)
            if len(self.max_) + 1 < len(self.min_):
                heapq.heappush(self.max_, -heapq.heappop(self.min_))

        else:
            heapq.heappush(self.max_, num)
            if len(self.max_) > len(self.min_):
                heapq.heappush(self.min_, -heapq.heappop(self.max_))

    def findMedian(self) -> float:
        if len(self.min_) > len(self.max_):
            return -self.min_[0]
        return (-self.min_[0] + self.max_[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()