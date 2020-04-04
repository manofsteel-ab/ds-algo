# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        result, path = [], []
        def search(root, K):
            if (not root) or (K < 0):
                return
            if K == 0:
                result.append(root.val)
                return
            search(root.left, K-1)
            search(root.right, K-1)
        def find_path(root):
            if not root:
                return False
            if root == target:
                path.append((root, -1))
                return True
            if find_path(root.left):
                path.append((root, 0))
                return True
            if find_path(root.right):
                path.append((root, 1))
                return True
            return False
        find_path(root)
        for dist in range(min(K+1, len(path))):
            node, choice = path[dist]
            if dist == 0 or dist == K:
                search(node, K-dist)
                continue
            if choice == 0:
                search(node.right, K-dist-1)
            elif choice == 1:
                search(node.left, K-dist-1)
        return result
