class Solution:
    def bin(self, d: int) -> int:
        binary = ""
        while d > 0:
            binary += str(d % 2)
            d //= 2
        binary = binary[::-1]
        b = int(binary)
        return b

    def convertDateToBinary(self, date: str) -> str:
        date = date.split('-')
        new_date = ""
        for d in range(len(date)):
            num_d = int(date[d])
            b = self.bin(num_d)
            new_date += str(b)
            if d != len(date) - 1:
                new_date += "-"
        return new_date
