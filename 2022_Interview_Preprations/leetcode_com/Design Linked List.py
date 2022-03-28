class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def printList(self):
        temp = self.head
        print ("count is ", self.cnt)
        while temp:
            print(temp.val,)
            temp = temp.next
        print ("\n")

    def __init__(self):
        self.head = None
        self.cnt = 0

    def get(self, index):
        if index >= self.cnt:
            return -1
        temp = self.head
        counter = 0
        while counter < index:
            counter += 1
            temp = temp.next
        # print ("index ")
        # print (index)
        # self.printList()
        return temp.val

    def addAtHead(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        self.cnt += 1
        # print ("addAtHead")
        # self.printList()


    def addAtTail(self, val):
        temp = Node(val)
        if self.head is None:
            self.head = temp
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = temp
        self.cnt += 1
        # print ("addAtTail")
        # self.printList()

    def addAtIndex(self, index, val):
        if index > self.cnt or index < 0:
            return
        newNode = Node(val)
        # 1>2>3>4
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            counter = 0
            prev = None
            while counter < index:
                counter += 1
                prev = temp
                temp = temp.next
            if temp is None:
                prev.next = newNode
            else:
                prev.next = newNode
                newNode.next = temp
        self.cnt += 1
        # print ("addAtIndex")
        # self.printList()

    def deleteAtIndex(self, index):
        if self.head is None or index >= self.cnt:
            return
        deletedNode = None
        if index == 0:
            deletedNode = self.head
            self.head = self.head.next
        else:
            counter = 0
            curr = self.head
            prev = None
            while counter < index:
                counter += 1
                prev = curr
                curr = curr.next
            deletedNode = curr
            prev.next = curr.next
        self.cnt -= 1
        del deletedNode
        # print ("deleteAtIndex")
        # self.printList()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
