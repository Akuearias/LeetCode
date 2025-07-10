from collections import Counter


def checkMagazine(magazine, note):
    magazine_hash, note_hash = Counter(magazine), Counter(note)
    for word in magazine_hash:
        if magazine_hash[word] < note_hash.get(word, 0):
            print('No')
            return

    for word in note_hash:
        if word not in magazine_hash:
            print('No')
            return

    print('Yes')