# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def _getMiddleNode(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, list_1, list_2):
        if not list_1:
            return list_2
        if not list_2:
            return list_1

        result = None

        if list_1.val <= list_2.val:
            result = list_1
            result.next = self._merge(list_1.next, list_2)
        else:
            result = list_2
            result.next = self._merge(list_1, list_2.next)
        return result

    def _mergeSort(self, head):
        if not head or not head.next:
            return head

        middle = self._getMiddleNode(head)
        next_to_middle = middle.next
        middle.next = None
        left = self._mergeSort(head)
        right = self._mergeSort(next_to_middle)
        return self._merge(left, right)

    def sortList(self, head: ListNode) -> ListNode:
        return self._mergeSort(head)
