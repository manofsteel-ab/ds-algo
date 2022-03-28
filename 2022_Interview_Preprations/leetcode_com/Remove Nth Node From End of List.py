# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def _wihout_length_calculations(self, head, n):

        if not head:
            return
        p2 = head

        counter = 0

        while counter < n and p2:
            p2 = p2.next
            counter += 1
        if p2 is None:
            head = head.next
        else:
            p1 = head
            while p2.next:
                p1 = p1.next
                p2 = p2.next
            p1.next = p1.next.next
        return head

    def _with_length(self, head, n):
        if not head:
            return

        sz = 0
        # calculate the size of list
        curr = head
        while curr:
            sz += 1
            curr = curr.next

        # find out sz-k-1th node

        curr = head
        prev = None
        counter = 0
        while counter < sz - n:
            prev = curr
            curr = curr.next
            counter += 1

        if prev is None:
            curr = curr.next
            head = curr
        else:
            prev.next = curr.next
        return head

    def removeNthFromEnd(self, head, n):

        return self._wihout_length_calculations(head, n)

