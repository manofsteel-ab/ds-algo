# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # def postOrder(self, root, ans):
    #     if not root:
    #         return
    #     self.postOrder(root.left, ans)
    #     self.postOrder(root.right, ans)
    #     ans.append(root.val)
    def postorderTraversal(self, A):
        ans = []
        if not A:
            return ans
        # self.postOrder(A, ans)
        stack = [A]

        while len(stack) > 0:
            top = stack[-1]
            if top.right:
                stack.append(top.right)

        return ans
