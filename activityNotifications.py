def get_median(count, d):
    acc = 0
    if d % 2 == 1:
        mid = d // 2 + 1
        for i in range(201):
            acc += count[i]
            if acc >= mid:
                return i
    else:
        mid1 = d // 2
        mid2 = mid1 + 1
        m1 = m2 = None
        for i in range(201):
            acc += count[i]
            if m1 is None and acc >= mid1:
                m1 = i
            if acc >= mid2:
                m2 = i
                break
        return (m1 + m2) / 2

def activityNotifications(expenditure, d):
    count = [0] * 201
    for i in range(d):
        count[expenditure[i]] += 1

    notifications = 0
    for i in range(d, len(expenditure)):
        median_val = get_median(count, d)
        if expenditure[i] >= 2 * median_val:
            notifications += 1

        # slide window
        count[expenditure[i - d]] -= 1
        count[expenditure[i]] += 1

    return notifications