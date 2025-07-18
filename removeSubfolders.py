import collections
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        dq = collections.deque(folder)
        S = []
        while dq:
            dummy = dq.popleft()
            S.append(dummy)
            while dq and dummy in dq[0]:
                if dq[0][len(dummy)] == '/' and dq[0][:len(dummy)] == dummy:
                    dq.popleft()
                else:
                    break

        return S
