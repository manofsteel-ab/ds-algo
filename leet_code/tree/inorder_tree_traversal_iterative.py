# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def _recusiveInorder(self, root, traversed_node):
        if not root:
            return

        self._recusiveInorder(root.left, traversed_node)
        traversed_node.append(root.val)
        self._recusiveInorder(root.right, traversed_node)
        return traversed_node

    def _iterativeInorder(self, root, traversed_node):
        if not root:
            return

        current = root
        while current:
            print(current.val)
            if not current.left:
                traversed_node.append(current.val)
                current = current.right
            else:
                temp = current.left

                while temp.right and temp.right != current:
                    temp = temp.right

                if temp.right is None:
                    temp.right = current
                    current = current.left
                else:
                    temp.right = None
                    traversed_node.append(current.val)
                    current = current.right
        return traversed_node

    def inorderTraversal(self, root: TreeNode):
        return self._iterativeInorder(root, [])
