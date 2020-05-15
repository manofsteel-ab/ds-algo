# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def _getSum(self, root, val):
        if not root:
            return 0

        val1 = 10 * val + root.val

        if not root.left and not root.right:
            return val1
        else:
            return self._getSum(root.left, val1) + self._getSum(root.right,
                                                                val1)

    def sumNumbers(self, A):
        return self._getSum(A, 0) % 1003
