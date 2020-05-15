"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' =
    None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):
        if not root:
            return root

        queue = [root]

        while queue:
            queue_sz = len(queue)
            prev = None
            while queue_sz > 0:
                element = queue.pop(0)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)

                if not prev:
                    prev = element
                else:
                    prev.next = element
                    prev = element
                queue_sz -= 1
        return root


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = 
    None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution1:

    def _getNext(self, node):
        next_right = node.next
        while next_right:
            if next_right.left:
                return next_right.left
            if next_right.right:
                return next_right.right
            next_right = next_right.next
        return None

    def connect(self, root):
        if not root:
            return root

        current = root

        while current:
            temp = current
            while temp:
                if temp.left:
                    if temp.right:
                        temp.left.next = temp.right
                    else:
                        temp.left.next = self._getNext(temp)
                if temp.right:
                    temp.right.next = self._getNext(temp)
                temp = temp.next
            if current.left:
                current = current.left
            elif current.right:
                current = current.right
            else:
                current = self._getNext(current)
        return root

