# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Two elements of a binary search tree (BST) are swapped by mistake.
Tell us the 2 values swapping which the tree will be restored.
"""

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorder(self, root, s):
        if root == None:
            return

        if root.left != None:
            self.inorder(root.left, s)
        s.append(root.val)

        if root.right != None:
            self.inorder(root.right, s)

    def recoverTree(self, root):
        s = []
        err = []
        self.inorder(root, s)
        a = s[:]
        s.sort()
        for i in range(len(s)):
            if s[i] != a[i]:
                err.append(s[i])
                err.append(a[i])
                break
        return err

