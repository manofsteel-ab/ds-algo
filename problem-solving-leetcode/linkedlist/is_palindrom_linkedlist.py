# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def _checkPalindrom(self, head_1, head_2):
        if not head_2 or not head_1[0]:
            return True
        flag = self._checkPalindrom(head_1, head_2.next)
        val1 = head_1[0].val
        val2 = head_2.val
        head_1[0] = head_1[0].next
        if val1 == val2 and flag:
            return True
        else:
            return False

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        headCopy = head
        return self._checkPalindrom([headCopy], headCopy)
