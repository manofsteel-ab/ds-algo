# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def _getInorderList(self, root, elements):
        if not root:
            return
        self._getInorderList(root.left, elements)
        elements.append(root.val)
        self._getInorderList(root.right, elements)

    def _recusiveTraverslSolution(self, root, k):
        inorderPath = []
        self._getInorderList(root, inorderPath)
        return inorderPath[k - 1]

    def _morrisTraversalSol(self, root, k):
        current = root

        while current:
            if not current.left:
                k -= 1
                if k == 0:
                    return current.val
                else:
                    current = current.right
            else:
                temp = current.left
                while temp.right and temp.right != current:
                    temp = temp.right

                if not temp.right:
                    temp.right = current
                    current = current.left
                else:
                    k -= 1
                    if k == 0:
                        return current.val
                    else:
                        temp.right = None
                        current = current.right

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # return self._recusiveTraverslSolution(root, k)
        return self._morrisTraversalSol(root, k)
