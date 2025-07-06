def whatFlavors(cost, money):
    map_ = {}
    for i, c in enumerate(cost):
        dummy = money - c
        if dummy in map_:
            print(map_[dummy] + 1, i + 1)
            break
        map_[c] = map_.get(c, 0) + i
        