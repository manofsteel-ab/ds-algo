# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root, k):
        dic = set()
        from collections import deque
        queue = deque([root])

        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                if k-node.val in dic:
                    return 1
                else:
                    dic.add(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return 0
