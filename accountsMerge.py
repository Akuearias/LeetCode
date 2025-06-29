import collections
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_dict = dict()
        mail_name = dict()
        for account in accounts:
            username = account[0]
            emails = account[1:]
            for email in emails:
                if email not in mail_dict:
                    mail_dict[email] = len(mail_dict)
                    mail_name[email] = username

        UF = UnionFind(len(mail_dict))
        for account in accounts:
            id_ = mail_dict[account[1]]
            for email in account[2:]:
                UF.union(id_, mail_dict[email])

        id_to_email = collections.defaultdict(list)
        for email, id_ in mail_dict.items():
            id_ = UF.find(id_)
            id_to_email[id_].append(email)

        S = list()
        for emails in id_to_email.values():
            S.append([mail_name[emails[0]]] + sorted(emails))

        return S

# https://leetcode.cn/problems/accounts-merge/solutions/564305/zhang-hu-he-bing-by-leetcode-solution-3dyq
