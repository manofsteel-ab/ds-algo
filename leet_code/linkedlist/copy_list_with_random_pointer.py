"""
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomListO_1(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # add new node after old nodes
        temp = head
        while temp:
            newNode = Node(temp.val)
            newNode.next = temp.next
            temp.next = newNode
            temp = temp.next.next

        # adjust random pointer
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        # adjust next pointer of copied node and detach old next pointer
        ans = head.next
        temp = head
        while temp.next:
            nxt = temp.next
            temp.next = temp.next.next
            temp = nxt
        return ans
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        mp = {} # old node->new node mapping

        temp = head
        while temp:
            newNode = Node(temp.val)
            mp[temp] = newNode
            temp = temp.next

        copyHead = mp[head]
        ans = copyHead
        temp=head
        while temp:
            if temp.next:
                copyHead.next = mp[temp.next]
            if temp.random:
                copyHead.random = mp[temp.random]

            temp = temp.next
            copyHead = copyHead.next
        return ans
