# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _getUpperBoundIndex(self, arr, target):
        for index,val in enumerate(arr):
            if val>target:
                return index
        return len(arr)

    def _buildTree(self, preorder, index):
        if not preorder:
            return
        root = TreeNode(preorder[index])
        upperBoundIndex = self._getUpperBoundIndex(preorder,preorder[index])
        leftTree = preorder[index+1:upperBoundIndex]
        rightTree = preorder[upperBoundIndex:]
        root.left = self._buildTree(leftTree, 0)
        root.right = self._buildTree(rightTree, 0)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        return self._buildTree(preorder,0)
