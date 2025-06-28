class SORTracker:

    def __init__(self):
        self.spot_list = SortedList()
        self.dummy = 0

    def add(self, name: str, score: int) -> None:
        self.spot_list.add((-score, name))

    def get(self) -> str:
        self.dummy += 1
        return self.spot_list[self.dummy - 1][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()

# https://leetcode.cn/problems/sequentially-ordinal-rank-tracker/solutions/1152448/qiao-miao-li-yong-cha-xun-de-te-shu-xing-7eyg


if __name__ == "__main__":
    sortracker = SORTracker()
    sortracker.add('bradford', 2)
    sortracker.add('branford', 3)
    print(sortracker.get())
    sortracker.add('alps', 2)
    print(sortracker.get())
    sortracker.add('orland', 2)
    print(sortracker.get())
    sortracker.add('orlando', 3)
    print(sortracker.get())
    sortracker.add('alpine', 2)
    print(sortracker.get())
    print(sortracker.get())