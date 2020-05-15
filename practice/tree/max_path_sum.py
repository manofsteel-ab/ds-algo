# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _getSum(self, root, ans: list):
        if not root:
            return 0
        left_sum = max(self._getSum(root.left, ans),0)
        right_sum = max(self._getSum(root.right, ans), 0)
        ans[0] = max(ans[0] , left_sum + right_sum + root.val)
        return max(left_sum, right_sum, 0) + root.val

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = [float('-inf')]
        self._getSum(root, ans)
        return ans[0]
        
