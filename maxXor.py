class TrieNode:
    def __init__(self):
        self.children = {}


def insert(root, num):
    node = root
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        if bit not in node.children:
            node.children[bit] = TrieNode()
        node = node.children[bit]


def findMaxXor(root, num):
    node = root
    maxXor = 0
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        toggled = 1 - bit
        if toggled in node.children:
            maxXor |= (1 << i)
            node = node.children[toggled]
        else:
            node = node.children.get(bit, node)  # fallback
    return maxXor


def maxXor(arr, queries):
    root = TrieNode()
    for num in arr:
        insert(root, num)

    result = []
    for q in queries:
        result.append(findMaxXor(root, q))
    return result