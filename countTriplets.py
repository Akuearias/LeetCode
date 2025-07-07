from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    n = len(arr)
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1

    total = 0
    left = defaultdict(int)  #
    right = freq.copy()

    for mid in arr:
        right[mid] -= 1

        if mid % r == 0:
            left_val = mid // r
            right_val = mid * r
            total += left[left_val] * right[right_val]

        left[mid] += 1

    return total