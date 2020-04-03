class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insertAtFront(self, val):
        newNode = Node(val)
        if self.head:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode

    def findNode(self, val):
        head = self.head

        while head:
            if head.val == val:
                return head
            head = head.next
        return None

    def remove(self, node):
        if not node:
            return
        prev = node.prev
        nxt = node.next
        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev
        if node == self.head:
            self.head = nxt
        del node

    def display(self):
        head=self.head
        while head:
            print(head.val),
            head = head.next
        print("\n")
dlist = DoublyLinkedList()
dlist.insertAtFront(1)
dlist.insertAtFront(2)
dlist.insertAtFront(3)
dlist.insertAtFront(4)
dlist.display()
d = dlist.findNode(2)
dlist.remove(d)
dlist.display()
