"""
Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return

        if node.next is None:
            node = None

        nxt = node.next
        node.val = nxt.val
        node.next = nxt.next

