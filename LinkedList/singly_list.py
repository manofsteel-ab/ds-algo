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

		return count


	def display_items(self):
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

	def nth_node_from_end_approach1(self, n):
		# count lenth of list, then return len-n+1'th node
		list_sz = self.size()
		if n>list_sz:
			raise ValueError("Index out of bounds")
		counter = 0
		current_node = self.head

		while counter<list_sz-n:
			current_node = current_node.next
			counter = counter + 1

		return current_node.value

	def nth_node_from_end_approach2(self, n):
		#  Using two pointers 1,2,3,4,5
		node1 = self.head
		node2 = self.head

		while n>0 and node1:
			node1 = node1.next
			n = n-1

		if n>0:
			raise ValueError("Index out of bounds")


		while node1:
			node2 = node2.next
			node1 = node1.next

		return node2.value

	def nth_node_from_end(self, n, approach_type=1):
		if approach_type == 1:
			return self.nth_node_from_end_approach1(n)
		if approach_type == 2:
			return self.nth_node_from_end_approach2(n)

	def find_middle_node(self):
		if not self.head or not self.head.next:
			return self.head
		
		slow_pointer = self.head
		fast_pointer = self.head

		while fast_pointer and fast_pointer.next:
			slow_pointer = slow_pointer.next
			fast_pointer = fast_pointer.next.next

		return slow_pointer.value

	def detect_loop_using_set(self):
		s = set()
		current_node = self.head
		while current_node:
			if current_node in s:
				return True

			s.add(current_node)
			current_node = current_node.next

		return False

	def detect_loop_using_slow_fast_pointer(self):
		slow_pointer = self.head
		fast_pointer = self.head

		while slow_pointer and fast_pointer and fast_pointer.next:
			slow_pointer = slow_pointer.next
			fast_pointer = fast_pointer.next.next
			if slow_pointer == fast_pointer:
				return True

		return False

	def reverse(self, current_node):
		prev = None
		if not current_node or not current_node.next: 
			return current_node

		while current_node:
			next_node = current_node.next
			current_node.next = prev
			prev = current_node
			current_node = next_node

		return prev

	def even_before_odds_approach1(self):
		#  get last node, now traverse from start if node is odd then move it to end and shift end

		last_node = self.head
		first_odd = None
		first_even = None
		if not last_node or not last_node.next:
			return last_node

		while last_node.next:
			last_node = last_node.next

		current_node = self.head

		prev = None
		while current_node and current_node!=first_odd:
			next_node = current_node.next
			if current_node.value %2 == 1:
				if not first_odd:
					first_odd = current_node
				if prev is None:
					temp = current_node
					last_node.next = temp
					last_node = temp
					last_node.next = None
					current_node = next_node
				else:
					temp = current_node
					prev.next = next_node
					current_node = next_node
					last_node.next = temp
					last_node = temp
					last_node.next = None
			else:
				if not first_even:
					first_even = current_node
				prev = current_node
				current_node = next_node
		return first_even

	def even_before_odds_approach2(self):
		#  split list into two linked list, one containing even nodes and other contains odd nodes,
		#   and finally attach them to get desired list
		invalidation = [
		   not self.head,
		   self.head and not self.head.next
		]
		if any(invalidation):
			return self.head
		
		event_start_node = None
		event_end_node = None
		odd_start_node = None
		odd_end_node = None
		current_node = self.head

		while current_node:
			if current_node.value %2 == 1:
				if odd_start_node is None:
					odd_start_node = current_node
					odd_end_node = odd_start_node
				else:
					odd_end_node.next = current_node
					odd_end_node = odd_end_node.next
			else:
				if event_start_node is None:
					event_start_node = current_node
					event_end_node = event_start_node
				else:
					event_end_node.next = current_node
					event_end_node = event_end_node.next

			current_node = current_node.next

		if not odd_start_node or not event_start_node:
			return self.head

		if odd_start_node:
			event_end_node.next = odd_start_node

		return event_start_node

	def remove_duplicates(self):
		#  this is algorith is to remove duplicate from soreted list
		if not self.head or not self.head.next:
			return
		current_node = self.head
		while current_node and current_node.next:
			if current_node.value == current_node.next.value:
				current_node.next = current_node.next.next
			else:
				current_node = current_node.next

	def remove_duplicates_unsoreted(self):
		if not self.head or not self.head.next:
			return
		s = set()

		current_node = self.head

		while current_node and current_node.next:
			s.add(current_node.value)
			if current_node.next.value in s:
				current_node.next = current_node.next.next
			else:
				current_node = current_node.next

	def swap_nodes(self, x, y):
		# case 1 if no of items in list < 2
		if not self.head and not self.head.next:
			return
		# case 2 - x==y
		if x == y:
			return

		curr_x = None
		prev_x = None
		curr_y = None
		prev_y = None

		prev = None
		current_node = self.head
		while current_node:
			if current_node.value == x:
				prev_x = prev
				curr_x = current_node
			if current_node.value == y:
				prev_y = prev
				curr_y = current_node

			if curr_x and curr_y:
				break
			
			prev = current_node
			current_node = current_node.next 

		# case 3 - if x or y does not exist

		if not curr_x or not curr_y:
			return

		# case 4 - if x or y is first node conditions

		if prev_x is None: # if x is first node, then after swap y would be first node
		   self.head = curr_y
		else:  # if x is not first node then prev of x should point to y
			prev_x.next = curr_y


		if prev_y is None: # if y is head of list, then after swap x would be first node
			self.head = curr_x
		else:  # prev of y should point to x
			prev_y.next = curr_x

		# swap the next pointers for boath

		temp = curr_x.next
		curr_x.next = curr_y.next
		curr_y.next = temp
		

list = LinkedList()
# list.push(7)
# list.push(5)
list.push(4)
list.push(1)
# list.push(1)
list.push(6)
list.push(5)
list.push(7)
list.display_items()
# print(list.resursive_search(list.head, 1))
# print(list.search(6).value)

# list.delete(6)

# list.display_items()

# list.delete(6)

# print(list.nth_node_from_end(1, approach_type=1))
# print(list.nth_node_from_end(1, approach_type=2))

# print(list.find_middle_node())

# list.head = list.reverse(list.head)
# list.display_items()
# list.head = list.even_before_odds_approach2()
# list.remove_duplicates()
# list.remove_duplicates_unsoreted()
list.swap_nodes(6,5)
list.display_items()
		