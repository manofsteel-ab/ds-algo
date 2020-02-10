# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def _maxInRange(self, l, r, arr):
        if l < 0 or r > len(arr) - 1:
            return -1

        mx = l
        for i in range(l, r + 1):
            if arr[i] > arr[mx]:
                mx = i
        return mx

    def _create(self, left, right, arr):
        if right < left:
            return None
        mx_index = self._maxInRange(left, right, arr)
        if mx_index == -1:
            return None
        root = TreeNode(arr[mx_index])
        root.left = self._create(left, mx_index - 1, arr)
        root.right = self._create(mx_index + 1, right, arr)
        return root

    def buildTree(self, A):
        root = self._create(0, len(A) - 1, A)
        return root