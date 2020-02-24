# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        l = int(len(nums) / 2)
        root = TreeNode(nums[l])
        # print(nums,nums[0:l], nums[l+1:None])
        root.left = self.sortedArrayToBST(nums[:l])
        root.right = self.sortedArrayToBST(nums[l + 1:])
        return root
