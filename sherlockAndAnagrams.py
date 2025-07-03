import collections

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    freq = collections.defaultdict(int)
    for start in range(len(s)):
        count = [0] * 26
        for end in range(start, len(s)):
            count[ord(s[end]) - ord('a')] += 1
            key = tuple(count)
            freq[key] += 1
    return sum(v * (v - 1) // 2 for v in freq.values())