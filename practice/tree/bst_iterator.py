class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.push(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return bool(self.stack)

    # @return an integer, the next smallest number
    def next(self):
        ans = self.stack.pop()
        self.push(ans.right)
        return ans.val

    def push(self, root):
        while root:
            self.stack.append(root)
            root = root.left