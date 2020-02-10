# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers

    def _getPaths(self, root, total, path, res):
        if not root:
            return

        path.append(root.val)

        if sum(path) == total and not (root.left or root.right):
            res.append(path[:])
        self._getPaths(root.left, total, path, res)
        self._getPaths(root.right, total, path, res)
        path.pop()

    def pathSum(self, root, sum_val):
        res = []
        self._getPaths(root, sum_val, [], res)
        return res
