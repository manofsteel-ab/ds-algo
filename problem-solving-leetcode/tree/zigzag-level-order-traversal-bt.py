# your code goes here
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        if not A:
            return []
        currentQueue = []
        nextQueue = []
        currentFlow = 'ltr'
        ans = []
        currentQueue.append(A)
        while currentQueue:
            _sz = len(currentQueue)
            traversed_nodes = []
            for i in range(0, _sz):
                node = currentQueue.pop()
                traversed_nodes.append(node.val)
                if currentFlow == 'ltr':
                    if node.left:
                        nextQueue.append(node.left)
                    if node.right:
                        nextQueue.append(node.right)
                else:
                    if node.right:
                        nextQueue.append(node.right)
                    if node.left:
                        nextQueue.append(node.left)
            if currentFlow == 'ltr':
                currentFlow = 'rtl'
            else:
                currentFlow = 'ltr'
            currentQueue, nextQueue = nextQueue, currentQueue
            ans.append(traversed_nodes)

        return ans
