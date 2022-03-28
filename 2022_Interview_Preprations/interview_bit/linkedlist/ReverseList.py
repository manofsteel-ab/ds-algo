class ReverseList:

    def without_recursion(self, head):
        if not head:
            return None

        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def with_recursion(self, curr, prev, head):
        if not head:
            return head
        # if reached at end
        if curr is None:
            head = prev
            return head
        head = self.with_recursion(curr.next, curr, head)
        curr.next = prev
        return head

    def reverse(self, head):
        if not head:
            return None
