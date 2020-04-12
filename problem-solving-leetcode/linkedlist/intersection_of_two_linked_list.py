# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def _getLinkedListSize(self, head):
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        return count

    def getIntersectionNode(self, headA, headB):
        list1_sz = self._getLinkedListSize(headA)
        list2_sz = self._getLinkedListSize(headB)
        firstCommonNode = None
        sz_diff = list1_sz - list2_sz
        startA = headA
        startB = headB
        if sz_diff > 0:
            while sz_diff > 0:
                startA = startA.next
                sz_diff -= 1
        else:
            while sz_diff < 0:
                startB = startB.next
                sz_diff += 1

        while startA and startB:
            if startA == startB:
                firstCommonNode = startA
                break
            else:
                startA = startA.next
                startB = startB.next

        return firstCommonNode

