from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        peaks = []
        n = len(arr)
        for i in range(1, n - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                peaks.append(i)

        S = 0
        for peak in peaks:
            curr = 1
            L, R = peak, peak
            while L > 0 and arr[L] > arr[L - 1]:
                L -= 1
                curr += 1
            while R < n - 1 and arr[R] > arr[R + 1]:
                R += 1
                curr += 1
            S = max(S, curr)

        return S

