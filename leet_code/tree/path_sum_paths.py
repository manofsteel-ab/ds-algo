# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers

    def _getPaths(self, root, total, sum_so_far, path, res):
        if not root:
            return

        path.append(root.val)
        sum_so_far += root.val

        if sum_so_far == total and not (root.left or root.right):
            res.append(path[:])
        self._getPaths(root.left, total, sum_so_far, path, res)
        self._getPaths(root.right, total, sum_so_far, path, res)
        path.pop()

    def pathSum(self, root, sum_val):
        res = []
        self._getPaths(root, sum_val, 0, [], res)
        return res
