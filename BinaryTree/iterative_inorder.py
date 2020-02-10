# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # def inorder(self, root, ans):
    #     if not root:
    #         return
    #     self.inorder(root.left, ans)
    #     ans.append(root.val)
    #     self.inorder(root.right, ans)
    def inorderTraversal(self, A):
        ans = []
        # self.inorder(A, ans)
        # return ans
        stack = []
        current_node = A
        while True:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                if stack:
                    element = stack.pop()
                    ans.append(element.val)
                    current_node = element.right
                else:
                    return ans
