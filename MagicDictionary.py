from typing import List


class MagicDictionary:

    def __init__(self):
        self.wordlist = []

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.wordlist.append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.wordlist:
            if len(word) == len(searchWord):
                S = 0
                for i in range(len(word)):
                    if word[i] != searchWord[i]:
                        S += 1
                if S == 1:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)