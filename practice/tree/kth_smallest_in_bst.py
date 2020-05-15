# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, root, k):
        count = 0
        ans = -10000
        curr = root
        while curr:
            if curr.left == None:
                count += 1
                if count == k:
                    ans = curr.val
                curr = curr.right
            else:  # if left subtree exist
                prev = curr.left
                # find rightmost in left subtree
                while prev.right != None and prev.right != curr:
                    prev = prev.right

                if prev.right == None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    count += 1
                    if count == k:
                        ans = curr.val
                    curr = curr.right
        return ans
