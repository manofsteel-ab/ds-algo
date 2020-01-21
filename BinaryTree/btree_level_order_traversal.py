
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


class BTree:
	"""docstring for BTree"""
	def __init__(self):
		self.root = None,
		self.static_counter = 0

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

	def to_mirror_using_recursion(self, current_node):
		if not current_node:
			return
		self.to_mirror_using_recursion(current_node.left)
		self.to_mirror_using_recursion(current_node.right)

		current_node.swap_left_right()

	def to_mirror_using_level_order_traversal(self, current_node):
		if not current_node:
			return

		queue = []
		queue.append(current_node)

		while len(queue) > 0:
			node = queue.pop(0)
			node.swap_left_right()
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

	def to_mirror(self, approach='recursive'):
		if approach == 'recursive':
			self.to_mirror_using_recursion(self.root)
		else:
			self.to_mirror_using_level_order_traversal(self.root)

	def leaf_boundtry_traversal(self, root):
		'''
              to print all leaf node
                 a - print leaf nodes in left subtree
                 b - print leaf nodes in righ subtree
		'''
		if not root:
			return
		
		if root.left:
			self.leaf_boundtry_traversal(root.left)

		if root.right:
			self.leaf_boundtry_traversal(root.right)


		if not root.left and not root.right:
			print root.value,

	def right_boundry_traversal(self, root):
		'''
		    if right present go right
		    else if left present go left
		    else - ignore leaf node condition

		    because for right boundry - we have to print in bottom up manner
		'''
		if not root:
			return


		if root.right:
			self.right_boundry_traversal(root.right)
			print root.value,

		elif root.left:
			self.right_boundry_traversal(root.right)
			print root.value

		# else:
			# ignore leaf nodes to avoid duplication

	def left_boundry_traversal(self, root):
		''' 
            ignore leaf node to avoid, duplication
		'''

		if not root:
			return

		if root.left:
			print root.value,
			self.left_boundry_traversal(root.left)

		elif root.right:
			print root.value,
			self.left_boundry_traversal(root.right)

		# else:
			# do nothing - leaf node 

	def boundry_traversal(self):
		''' 
		   Break this into three part
		    1 - print the left boundry in top - down manner
		    2 - print leaf nodes from left to right
		         a - print all leaf node from left to right for left subtree
		         b - print all node from left to right for right subtree
		    3 - print right boundry down - top manner 
		'''

		if self.root is None:
			return

		print self.root.value,

		self.left_boundry_traversal(self.root.left)
		self.leaf_boundtry_traversal(self.root.left)
		self.leaf_boundtry_traversal(self.root.right)
		self.right_boundry_traversal(self.root.right)

	def build_tree(self, start_index, end_index, inorder=[], preorder=[]):
		"""
		 Recursive function to construct binary of size len from 
		 Inorder traversal in[] and Preorder traversal pre[].  Initial values 
		 of start_index and end_index should be 0 and len -1.  The function doesn't 
		 do any error checking for cases where inorder and preorder 
		 do not form a tree 
		"""
		if start_index > end_index:
			return None

		new_node = Node(preorder[self.static_counter])
		self.static_counter = self.static_counter + 1

		if start_index == end_index:
			return new_node

		idx = self.search_in_arr(inorder, start_index, end_index, new_node.value)

		new_node.left = self.build_tree(start_index, idx-1, inorder, preorder)
		new_node.right = self.build_tree(idx+1, end_index, inorder, preorder)

		return new_node

	def search_in_arr(self, arr, start, end, key):
		for x in xrange(start,end+1):
			if arr[x] == key:
				return x
		return None


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
	# b_tree.to_mirror(approach='level_order_traversal')
	# b_tree.level_order_traversal_approach2()
	b_tree.boundry_traversal()




