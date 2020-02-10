# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        q = [root]
        while q:
            sz = len(q)
            prev = q.pop(0)
            if prev.left:
                q.append(prev.left)
            if prev.right:
                q.append(prev.right)
            for i in range(0, sz - 1):
                curr = q.pop(0)
                prev.next = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                prev = curr

            prev.next = None
        return root
