# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def _create_bst(self, start_index, end_index, arr):
        if start_index > end_index:
            return None
        mid = (start_index + end_index) / 2;
        root = TreeNode(arr[mid])
        root.left = self._create_bst(start_index, mid - 1, arr)
        root.right = self._create_bst(mid + 1, end_index, arr)
        return root

    def sortedArrayToBST(self, A):
        if not A:
            return None
        return self._create_bst(0, len(A) - 1, A)