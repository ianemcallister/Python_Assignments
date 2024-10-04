# Challenge 18
# Create a Binary Search Tree (BST) in Python or R, 
# and upload your code to GitHub.

class Node:
    def __init__(self, key):
        self.key = key # Value of the node
        self.left = None # Reference to the left child
        self.right = None # Reference to the right chidl node

class BinarySearchTree:
    def __init__(self):
        self.root = None    # Reference to the root node of the BST

    def insert(self, key):
        if self.root is None: # If the tree is empty
            self.root = Node(key) # Create a new node and set it as the root
        else:
            self._insert_recursive(self.root, key) # Call the recursive insert function with the root

    def _insert_recursive(self, node, key):
        if key < node.key: # If the key is less than the current node's key
            if node.left is None: # If the left child is empty
                node.left = Node(key) # Create a new node and set it as the left child
            else:
                self._insert_recursive(node.left, key) # Recursivly insert in the left subtree
        else:
            if node.right is None: # If the right child is empty
                node.right = Node(key) # Create a new node and set it as the right child
            else:
                self._insert_recursive(node.right, key) # Recursively insert in the right subtree
    
    def search(self, key):
        return self._search_recursive(self.root, key) # Call the recursive search function with the root

    def _search_recursive(self, node, key):
        if node is None or node.key == key: # If the node is none or the key si found
            return node     # Return the node (found) or Node (not found)
        if key < node.key: # If the key is less than the current node's key
            return self._search_recursive(node.left, key) # Recursivly search in the left subtree
        else:
            return self._search_recursive(node.right, key) # Recursively searh in the right subtree

# Test the binary Search tree
bst = BinarySearchTree() # Create a new BST object

# Insert nodes
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)

# Search for a key
print(bst.search(4).key) # Print the key of the found node (4)
print(bst.search(10)) # Print None (not found)