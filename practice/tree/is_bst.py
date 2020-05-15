import math 
  
# A binary tree node has data,  
# pointer to left child and  
# a pointer to right child  
class Node:  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None
      
def isBSTUtil(root, prev): 
      
    # traverse the tree in inorder fashion  
    # and keep track of prev node 
    if (root != None): 
        if (isBSTUtil(root.left, prev) == True): 
            return False
  
        # Allows only distinct valued nodes  
        if (prev != None and
            root.data <= prev.data): 
            return False
  
        prev = root 
        return isBSTUtil(root.right, prev) 
      
    return True
  
def isBST(root): 
    prev = None
    return isBSTUtil(root, prev) 
  
# Driver Code 
if __name__ == '__main__': 
    root = Node(3)  
    root.left = Node(2)  
    root.right = Node(5)  
    root.right.left = Node(1)  
    root.right.right = Node(4)  
    #root.right.left.left = Node(40) 
      
    if (isBST(root) == None): 
        print("Is BST") 
    else: 
        print("Not a BST") 