class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def addWord(self, word: str) -> None:
        head = self
        for w in word:
            if not head.children[ord(w) - ord('a')]:
                head.children[ord(w) - ord('a')] = WordDictionary()
            head = head.children[ord(w) - ord('a')]
        head.end = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            if j == len(word):
                return node.end
            ch = word[j]
            if ch == ".":
                for child in node.children:
                    if child and dfs(j + 1, child):
                        return True
                return False
            else:
                idx = ord(ch) - ord('a')
                child = node.children[idx]
                if not child:
                    return False
                return dfs(j + 1, child)

        return dfs(0, self)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)