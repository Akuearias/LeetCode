class MyCalendarTwo:
    def __init__(self, booked=None, overlap=None):
        if not booked:
            booked = []
        if not overlap:
            overlap = []
        self.booked = booked
        self.overlap = overlap

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.booked:
            self.booked.append((startTime, endTime))
            return True

        self.booked.sort()
        L = 0
        R = len(self.booked) - 1
        while L <= R:
            i = (L + R) // 2
            if not set(self.booked[i]) & range(startTime, endTime):
                if endTime <= self.booked[i][0]:
                    R = i - 1
                elif endTime >= self.booked[i][1]:
                    L = i + 1

            else:
                if set(self.booked[i] & range(startTime, endTime)) not in self.overlap:
                    self.booked.append((startTime, endTime))
                    self.overlap.append(set(self.booked[i] & range(startTime, endTime)))
                    return True
                else:
                    return False

        self.booked.append((startTime, endTime))
        self.booked.sort()
        return True
