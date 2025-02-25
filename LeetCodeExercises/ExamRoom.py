class ExamRoom:
    seats = []

    def __init__(self, n: int):
        self.n = n
        for _ in range(n):
            self.seats.append(False)

    def seat(self) -> int:
        if not self.seats.__contains__(True):
            self.seats[0] = True
            return 0
        else:
            occupied_list = []
            for i in range(len(self.seats)):
                if self.seats[i]:
                    occupied_list.append(i)
            



    def leave(self, p: int) -> None:
        if self.seats[p]:
            self.seats[p] = False
        else:
            return


# Your ExamRoom object will be instantiated and called as such:
n = 10
obj = ExamRoom(n)
param_1 = obj.seat()
obj.leave(1)
