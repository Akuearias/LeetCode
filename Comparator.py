from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f'{self.name}, {self.score}'

    @staticmethod
    def comparator(a, b):
        if a.score != b.score:
            return b.score - a.score

        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0