
# Node data structure
class Node:

	def __init__(self, key):
		self.value = key
		self.left = None
		self.right = None


	def set_letf(self,key):
		self.left = Node(key)

	def set_right(self, key):
		self.right = Node(key)

	def set_value(self, key):
		self.value = key

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right


class BTree:
	"""docstring for BTree"""
	def __init__(self):
		self.root = None


	def get_height(self, t_node):
		# return height of tree from given node(t_node)
		if not t_node:
			return 0

		l_height = self.get_height(t_node.get_left())
		r_height = self.get_height(t_node.get_right())

		if l_height>r_height:
			return l_height + 1
		else:
			return r_height + 1

	def print_node_at_given_height(self, t_node, height):
		#  print node value at given height
		if not t_node:
			return
		if  height == 1:
			print t_node.value, 
		
		self.print_node_at_given_height(t_node.left, height-1)
		self.print_node_at_given_height(t_node.right , height-1)

	def level_order_traversal(self):
		# level order traversal for binary tree, print node value at each level
		# time complexity is O(N^2), space complexity O(N) for skewed tree for balanced tree call stack uses O(logn) space
		root = self.root
		if not root:
			return
		height = self.get_height(root)
		for i in range(1, height + 1):
			self.print_node_at_given_height(root, i)
			print 

	def level_order_traversal_approach2(self):
		#  traverse b tree in - level order
		root = self.root
		if not root:
			return

		# using list as queue
		queue = []
		# pushing root node in queue
		queue.append(root)

		while len(queue) > 0:
			q_size = len(queue)
			for i in range(0, q_size):
				node = queue.pop(0)
				print node.value,
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			print 


if __name__ == '__main__':
	b_tree = BTree()
	root = Node(1)
	b_tree.root = root
	root.set_letf(2)
	root.set_right(3)
	root.left.set_letf(4)
	root.left.set_right(5)
	root.right.set_letf(6)
	root.right.set_right(7)
	# print(b_tree.get_height(b_tree.root))
	# b_tree.print_node_at_given_height(b_tree.root, 3)
	b_tree.level_order_traversal_approach2()




