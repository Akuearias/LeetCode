from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]
        else:
            teams = sorted(votes[0])

            for i in range(len(votes)):
                votes[i] = list(votes[i])

            ranks = [list(row) for row in zip(*votes)]
            rank_counts = []
            for i in range(len(teams)):
                counts = []
                for team in teams:
                    counts.append(ranks[i].count(team))
                rank_counts.append(counts)
            ranks_dict = {}
            for team, rank in zip(list(teams), rank_counts):
                ranks_dict[team] = rank
            ranks_list = list(ranks_dict.items())
            ranks_list.sort(key=lambda x: (x[1], -ord(x[0])), reverse=True)
            print(ranks_list)
            return "".join(ranks for ranks, scores in ranks_list)


if __name__ == '__main__':
    solution = Solution()
    votes = ["WXYZ", "XYZW"]
    print(solution.rankTeams(votes))


