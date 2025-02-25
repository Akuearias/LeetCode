from collections import Counter
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

    def q(self, t: int) -> int:
        if t not in self.times:
            t = self.find_nearest(self.times, t)
        selected_votes = self.persons[0:self.times.index(t) + 1]
        vote_count = list(Counter(selected_votes).values())
        if vote_count.count(max(vote_count)) != 1:
            members = []
            for i in range(len(vote_count)):
                if vote_count[i] == max(vote_count):
                    members.append(i)
            n = 0
            for i in range(0, self.times.index(t) + 1):
                if self.persons[i] in members:
                    n = max(n, i)
            return self.persons[n]
        else:
            return vote_count.index(max(vote_count))

    def find_nearest(self, times: List[int], t: int) -> int:
        if t > max(times):
            return times[-1]
        for i in range(len(times)):
            diff = times[i] - t
            if diff > 0:
                return times[i - 1]
            else:
                continue

if __name__ == '__main__':
    topVotedCandidate = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(topVotedCandidate.q(27))