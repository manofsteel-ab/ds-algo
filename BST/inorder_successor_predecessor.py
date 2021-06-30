

class BST:


    def _get_leftmost_node(self, node):
        if not node:
            return node

        while node.left:
            node = node.left
        return node

    def _get_rightmost_node(self,node):
        if not node:
            return node

        while node.right:
            node = node.right
        return node

    def find_successor_with_parent(self, node):
        if node.right:
            return self._get_leftmost_node(self.right)
        else:
            parent = node.parent
            while parent:
                if parent.left == node:
                    break
                node = parent
                parent = node.parent
            return parent

    def find_successor_without_parent(self, root, val):
        """
        1 - Do inorder traversal store in array, then find val in arr and
        return next element
        2 - while traversing keep maintain successor
        """

        successor = None

        while root and root.val!=val:
            if root.val>val:
                successor = root
                root = root.left
            else:
                root = root.right
        if not root:
            return None

        if not root.right:
            return successor

        return self._get_leftmost_node(root.right)

    def fin_predecessior(self, root, val):
        if not root:
            return

        predecessor = None

        while root and root.val!=val:

            if root.val<val:
                predecessor = root
                root = root.right
            else:
                root = root.left
        if not root:
            return None

        if not root.left:
            return predecessor

        return self._get_rightmost_node(root.left)
