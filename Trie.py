# https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/717239/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def searchPrefix(self, prefix):
        node = self
        for p in prefix:
            p = ord(p) - ord('a')
            if not node.children[p]:
                return None
            node = node.children[p]
        return node

    def insert(self, word: str) -> None:
        node = self
        for w in word:
            w = ord(w) - ord('a')
            if not node.children[w]:
                node.children[w] = Trie()
            node = node.children[w]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)