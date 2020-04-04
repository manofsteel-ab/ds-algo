# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.
"""


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return 0
        else:
            ans = 0
            sum = sum - root.val
            if sum == 0 and not root.left and not root.right:
                return 1
            if root.left:
                ans = ans or self.hasPathSum(root.left, sum)
            if root.right:
                ans = ans or self.hasPathSum(root.right, sum)

            return ans
