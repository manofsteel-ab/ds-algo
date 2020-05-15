
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

	def swap_left_right(self):
		temp = self.left
		self.left = self.right
		self.right = temp


class BSTree:
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
				print (node.value,)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			print 

	def search(self, root, key):
		if not root or root.value == key:
			return root
		
		if key < root.value:
			return self.search(root.left, key)

		else:
			return self.search(root.right, key)


	def insert(self, root, key):
		if root == None:
			return Node(key)

		if root.value > key:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		return root


if __name__ == '__main__':
	b_tree = BSTree()
	b_tree.root = b_tree.insert(b_tree.root, 30)
	b_tree.root = b_tree.insert(b_tree.root, 20)
	b_tree.root = b_tree.insert(b_tree.root, 40)
	b_tree.root = b_tree.insert(b_tree.root, 70)
	b_tree.root = b_tree.insert(b_tree.root, 60)
	b_tree.root = b_tree.insert(b_tree.root, 80)
	b_tree.level_order_traversal_approach2()
    



