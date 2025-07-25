from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_ = max(nums)
        max_id = nums.index(max_)
        S = TreeNode(max_)
        S.left = self.constructMaximumBinaryTree(nums[:max_id])
        S.right = self.constructMaximumBinaryTree(nums[max_id + 1:])
        return S

