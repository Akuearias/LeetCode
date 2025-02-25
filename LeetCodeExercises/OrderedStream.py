from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.pointer = 1
        self.streamList = ['Dummy'] + [None] * n


    def insert(self, idKey: int, value: str) -> List[str]:
        self.streamList[idKey] = value
        if not self.streamList[self.pointer]:
            return []
        else:
            streams = []
            while self.pointer <= self.n:
                if self.streamList[self.pointer]:
                    streams.append(self.streamList[self.pointer])
                    self.pointer += 1
                else:
                    break
            return streams


if __name__ == "__main__":
    stream = OrderedStream(5)
    print(stream.insert(3, 'ccccc'))
    print(stream.insert(1, 'aaaaa'))
    print(stream.insert(2, 'bbbbb'))
    print(stream.insert(5, 'eeeee'))
    print(stream.insert(4, 'ddddd'))
