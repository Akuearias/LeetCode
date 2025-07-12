""" Node is defined as """
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# I don't know why this is incorrect. The test cases in the original page are too tricky.
def checkBST(root):
    def isBST(node, min_val, max_val):
        if node is None:
            return True
        if node.data <= min_val or node.data >= max_val:
            return False
        return isBST(node.left, min_val, node.data) and isBST(node.right, node.data, max_val)

    return 'Yes' if isBST(root, float('-inf'), float('inf')) else 'No'