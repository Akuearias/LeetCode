nodes = {}


def treeNodes(root, code=""):
    if not root:
        return

    if root and not root.left and not root.right:
        nodes[code] = root.data

    else:
        treeNodes(root.left, code + "0")
        treeNodes(root.right, code + "1")


def decodeHuff(root, s):
    treeNodes(root, "")
    i = 0
    j = 1
    S = ""
    while i < len(s):
        while s[i:j] not in nodes:
            j += 1
        S += nodes[s[i:j]]
        i += j - i
        j = i + 1

    print(S)