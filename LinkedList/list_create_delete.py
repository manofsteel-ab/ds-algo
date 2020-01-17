class Node:
	"""docstring for ClassName"""
	def __init__(self, value):
		self.value = value
		self.next = None

	def get_data(self):
		return self.value

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next


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


	def displayItems(self):
		current_node = self.head
		while current_node:
			print(current_node.value),
			current_node = current_node.next

		print

	def search(self, value):
		current_node = self.head
		found = False
		while current_node:
			if current_node.value == value:
				found = True
				break
			else:
				current_node = current_node.next

		if current_node is None:
			raise ValueError("Data not found")

		return current_node

	def resursive_search(self, head, value):
		" return true if value present else return false "
		if not head:
			return False
		
		if head.value == value:
			return True

		else:
			return self.resursive_search(head.next, value)

	def delete(self, value):
		current_node = self.head
		previous_node = None

		found = False

		while current_node and not found:
			if current_node.value == value:
				found = True
				break
			else:
				previous_node = current_node
				current_node = current_node.next

		if current_node is None:
			raise ValueError("Data not found")

		if previous_node is None:
			self.head = current_node.get_next()
		else:
			previous_node.set_next(current_node.get_next())

		return self.head





list = LinkedList()
list.push(5)
list.push(4)
list.push(1)
list.displayItems()
list.push(6)
list.displayItems()
print(list.resursive_search(list.head, 1))
print(list.search(6).value)

list.delete(6)

list.displayItems()

list.delete(6)

# Outputs are

# 1 4 5
# 6 1 4 5
# True
# 6
# 1 4 5
# Traceback (most recent call last):
#   File "list_create_delete.py", line 118, in <module>
#     list.delete(6)
#   File "list_create_delete.py", line 91, in delete
#     raise ValueError("Data not found")
# ValueError: Data not found
		