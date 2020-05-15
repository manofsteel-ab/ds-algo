# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        if not root or root==x or root==y:
            return False


        queue = [root]

        while queue:
            current_level_size = len(queue)
            same_parent= False
            x_parent = None
            y_parent = None
            # print('\n')
            while current_level_size>0:
                current_node = queue.pop(0)
                # print(current_node.val,end=' ')
                left = current_node.left
                right = current_node.right
                if left:
                    queue.append(left)
                    if left.val == x:
                        x_parent = current_node
                    if left.val == y:
                        y_parent = current_node
                if right:
                    queue.append(right)
                    if right.val == x:
                        x_parent = current_node
                    if right.val == y:
                        y_parent = current_node
                current_level_size-=1
            if x_parent is not None and x_parent == y_parent:
                return False
            if x_parent is not None and y_parent is not None:
                return True
        return False
