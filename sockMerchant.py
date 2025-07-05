#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
import collections


def sockMerchant(n, ar):
    S = 0
    socks_count = dict(collections.Counter(ar))
    for count in socks_count.values():
        S += count // 2
    return S