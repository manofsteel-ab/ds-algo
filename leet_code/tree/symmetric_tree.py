"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def _isMirror(self, t1, t2):
        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False

        return t1.val == t2.val and self._isMirror(
            t1.left, t2.right) and self._isMirror(
            t1.right, t2.left
        )

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self._isMirror(root.left, root.right)
