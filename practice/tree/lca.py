# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def getLCA(self, root, n1, n2, v):
        if not root:
            return None

        if root.val == n1:
            v[0] = True
            return root

        if root.val == n2:
            v[1] = True
            return root

        left_lca = self.getLCA(root.left, n1, n2, v)
        right_lca = self.getLCA(root.right, n1, n2, v)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca is not None else right_lca

    def find(self, root, val):
        if not root:
            return False

        if root.val == val or self.find(root.left, val) or self.find(root.right,
                                                                     val):
            return True
        else:
            return False

    def lca(self, root, p, q):
        v = [False, False]
        lca = self.getLCA(root, p, q, v)
        if (v[0] and v[1] or v[0] and self.find(lca, q) or v[1] and self.find(
                lca, p)):
            return lca.val
        return -1

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution2:
    def getPath(self, root, path, search_item):
        if not root:
            return False
        path.append(root)
        if root.val == search_item:
            return root
        if (root.left and self.getPath(root.left, path, search_item)) or (
                root.right and self.getPath(root.right, path, search_item)):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        self.getPath(root, path1, p.val)
        self.getPath(root, path2, q.val)
        if not path1 or not path2:
            return -1
        # print(path1)
        # print(path2)
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i].val != path2[i].val:
                break
            i += 1
        # print(path1[i-1])
        return path1[i - 1]