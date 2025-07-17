from collections import Counter


def reverseShuffleMerge(s):
    stack = []
    char_count = Counter(s)
    required = {c: count // 2 for c, count in char_count.items()}
    s_dic = {c: 0 for c in s}
    remain = Counter(s)

    for c in reversed(s):
        if s_dic[c] < required[c]:
            while stack and c < stack[-1] and s_dic[stack[-1]] + remain[stack[-1]] - 1 >= required[stack[-1]]:
                removed = stack.pop()
                s_dic[removed] -= 1
            stack.append(c)
            s_dic[c] += 1
        remain[c] -= 1

    return ''.join(stack)