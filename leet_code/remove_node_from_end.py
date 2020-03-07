# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n: int):

        fast = head
        i = 0
        while fast and i < n:
            fast = fast.next
            i += 1

        slow = head
        # print(fast.val)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        if not fast:
            head = head.next
        else:
            slow.next = slow.next.next

        return head