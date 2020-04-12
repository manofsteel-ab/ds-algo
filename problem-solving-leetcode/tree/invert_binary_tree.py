# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
        if not root:
            return None

        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # root.left, root.right = root.right, root.left

        q = []

        q.append(root)

        while q:
            front = q[0]
            q.pop(0)

            front.left, front.right = front.right, front.left

            if front.left:
                q.append(front.left)

            if front.right:
                q.append(front.right)

        return root
