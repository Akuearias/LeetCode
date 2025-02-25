from selectors import SelectSelector


class MyCalendar:

    def __init__(self, booked=None):
        if booked is None:
            booked = []
        self.booked = booked

    def overlap(self, Time1: tuple, Time2: tuple) -> bool:
        return bool(set(range(Time1[0], Time1[1])) & set(range(Time2[0], Time2[1])))

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.booked:
            self.booked.append((startTime, endTime))
            self.booked.sort()
            return True

        L = 0
        R = len(self.booked) - 1
        while L <= R:
            i = (L + R) // 2
            if not self.overlap(self.booked[i], (startTime, endTime)):
                if endTime <= self.booked[i][0]:
                    R = i - 1
                elif endTime >= self.booked[i][1]:
                    L = i + 1
            else:
                return False

        self.booked.append((startTime, endTime))
        self.booked.sort()
        return True

myCalendar = MyCalendar()
print(myCalendar.book(10, 20))
print(myCalendar.book(15, 25))
print(myCalendar.book(20, 30))
print(myCalendar.book(30, 40))