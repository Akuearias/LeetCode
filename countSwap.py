def countSwaps(a):
    S = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                S += 1

    print(f'Array is sorted in {S} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    