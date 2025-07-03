import collections

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    s_counter = dict(collections.Counter(s))
    s_counts = list(s_counter.values())
    if len(set(s_counts)) == 1:
        return 'YES'
    else:
        s_counts_2 = list(set(s_counts))
        s_counts_2.sort()
        if len(set(s_counts_2)) > 2:
            return 'NO'
        else:
            max_, min_ = s_counts_2[-1], s_counts_2[0]
            s_counts_counter = dict(collections.Counter(s_counts))
            if s_counts_counter[max_] > 1 and s_counts_counter[min_] > 1:
                return 'NO'
            else:
                if max_ - min_ > 1:
                    return 'NO'
                else:
                    return 'YES'