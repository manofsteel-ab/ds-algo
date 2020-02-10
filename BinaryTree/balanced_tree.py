# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced_approach1(self, A):
        if A is None or A.left is None and A.right is None:
            return 1
        queue = [A]
        while len(queue) > 0:
            T = queue.pop()
            if T.left:
                queue.append(T.left)
                if not T.right and (T.left.left or T.left.right):
                    return 0
            if T.right:
                queue.append(T.right)
                if not T.left and (T.right.left or T.right.right):
                    return 0
        return 1

    def isBalanced_approach2(self, A):
        if not A:
            return 1

        lh = self.height(A.left)
        rh = self.height(A.right)

        if abs(lh - rh) > 1:
            return 0

        return self.isBalanced_approach2(A.left) and self.isBalanced_approach2(A.right)

    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))