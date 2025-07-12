def find_slots(grid):
    slots = []

    # Horizontal
    for r in range(10):
        c = 0
        while c < 10:
            if grid[r][c] == '-':
                start = c
                while c < 10 and grid[r][c] == '-':
                    c += 1
                length = c - start
                if length >= 2:
                    slots.append((r, start, 'H', length))
            else:
                c += 1

    # Vertical
    for c in range(10):
        r = 0
        while r < 10:
            if grid[r][c] == '-':
                start = r
                while r < 10 and grid[r][c] == '-':
                    r += 1
                length = r - start
                if length >= 2:
                    slots.append((start, c, 'V', length))
            else:
                r += 1

    return slots

def can_place(grid, word, slot):
    r, c, direction, length = slot
    if len(word) != length:
        return False
    for i in range(length):
        rr = r + (i if direction == 'V' else 0)
        cc = c + (i if direction == 'H' else 0)
        if grid[rr][cc] != '-' and grid[rr][cc] != word[i]:
            return False
    return True

def place_word(grid, word, slot):
    r, c, direction, length = slot
    placed_positions = []
    for i in range(length):
        rr = r + (i if direction == 'V' else 0)
        cc = c + (i if direction == 'H' else 0)
        if grid[rr][cc] == '-':
            grid[rr][cc] = word[i]
            placed_positions.append((rr, cc))
    return placed_positions

def remove_word(grid, placed_positions):
    for rr, cc in placed_positions:
        grid[rr][cc] = '-'

def backtrack(grid, slots, words, used, index=0):
    if index == len(words):
        return True

    word = words[index]
    for i, slot in enumerate(slots):
        if used[i]:
            continue
        if can_place(grid, word, slot):
            placed_positions = place_word(grid, word, slot)
            used[i] = True
            if backtrack(grid, slots, words, used, index + 1):
                return True
            remove_word(grid, placed_positions)
            used[i] = False
    return False

def crosswordPuzzle(crossword, words):
    grid = [list(row) for row in crossword]
    words = words.split(';')
    words.sort(key=lambda w: -len(w))
    slots = find_slots(grid)
    used = [False] * len(slots)
    backtrack(grid, slots, words, used)
    return [''.join(row) for row in grid]