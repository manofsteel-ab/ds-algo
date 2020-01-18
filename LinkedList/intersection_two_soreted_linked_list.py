'''
    find intersection of two sorted singly linked list
'''

class Node:
	"""docstring for ClassName"""
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:
	"""docstring for ClassName"""
	def __init__(self):
		self.head = None


	def push(self, value):
		new_node = Node(value)
		if self.head:
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = new_node

		return self.head


	def size(self):
		count=0
		current_node = self.head
		while current_node:
			count = count + 1
			current_node = current_node.next

		return count

	def display_items(self):
		current_node = self.head
		while current_node:
			print(current_node.value),
			current_node = current_node.next

		print

	def merge_two_list(self, list1, list2):
		#  merge two sorted list
		last_node = None
		self.head = None

		while list1 and list2:
			if list1.value < list2.value:
				value = list1.value
				list1 = list1.next
			else:
				value = list2.value
				list2 = list2.next

			new_node = Node(value)

			if not self.head:
				self.head = new_node
				last_node = self.head
			else:
				last_node.next = new_node
				last_node = last_node.next

		if list1:
			while list1:
				new_node = Node(list1.value)
				list1 = list1.next
				last_node.next = new_node
				last_node = last_node.next
		
		if list2:
			while list2:
				new_node = Node(list2.value)
				list2 = list2.next
				last_node.next = new_node
				last_node = last_node.next

if __name__ == '__main__':
	list1 = LinkedList()
	list1.push(2)
	list1.push(1)
	list1.display_items()
	list2 = LinkedList()
	list2.push(4)
	list2.push(3)
	list2.push(2)

	list3 = LinkedList()
	list3.merge_two_list(list1.head, list2.head)
	list3.display_items()


		