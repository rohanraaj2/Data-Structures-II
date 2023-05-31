class AVLTreeNode:

    def __init__(self, key, value) -> None:
        self.key = key                          # keyword by which searching and sorting will occur
        self.value = value                      # list of tuples containing (doc_index, sentence_index)
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def __init__(self) -> None:
        self.root = None

    def insert (self, key:str, value: tuple[int,int]) -> None:
        # Inserts a (doc id, sen id) tuple into the AVL Tree with the given keyword

        node = AVLTreeNode(key,value)           # create a node to add in the tree
        self.root = self._insert(self.root, node) 

    def search (self, key:str) -> list[tuple[int,int]] :
        # Searches for a keyword in the AVL Tree and returns a list of (doc id, sen id) corresponding to the keyword. 
        # Returns an empty list if the keyword is not found.
        temp = self.root

        while temp != None:
            if key == temp.key:
                return temp.value
            elif key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right       
            
        return []

    def rotate_left(self, node:AVLTreeNode) -> AVLTreeNode:
        # Performs a left rotation on the subtree rooted at the given node.
        right_child = node.right
        right_left_child = right_child.left

        right_child.left = node
        node.right = right_left_child

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        right_child.height = max(self._get_height(right_child.left), self._get_height(right_child.right)) + 1

        return right_child
        pass

    def rotate_right(self, node:AVLTreeNode) -> AVLTreeNode:
        # Performs a right rotation on the subtree rooted at the given node.
        left_child = node.left
        left_right_child = left_child.right

        left_child.right = node
        node.left = left_right_child

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        left_child.height = max(self._get_height(left_child.left), self._get_height(left_child.right)) + 1

        return left_child
        pass

    def display(self) -> list[str]:
        # Performs an in-order traversal on the AVL Tree and returns a list of keys.
        tree = []
        self._inorder_traversal(self.root,tree)     
        return tree                         

    # helper functions to make coding easier
    def _insert(self, node:AVLTreeNode, node_to_insert:AVLTreeNode) -> AVLTreeNode:

        if node != None:
            if node_to_insert.key < node.key:
                node.left = self._insert(node.left, node_to_insert)

            elif node_to_insert.key > node.key:
                node.right = self._insert(node.right, node_to_insert)
                
            else:
                return node

            # update the node height
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

            # check balance factor and rotate if necessary
            bf = self._get_balance_factor(node)

            # left left case
            if bf > 1 and node_to_insert.key < node.left.key:
                return self.rotate_right(node)
            
            # right right case
            if bf < -1 and node_to_insert.key > node.right.key:
                return self.rotate_left(node)
            
            # left right case
            if bf > 1 and node_to_insert.key > node.left.key:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            
            # right left case
            if bf < -1 and node_to_insert.key < node.right.key:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
            
            return node 
        
        else:
            return node_to_insert 
        pass

    def _get_height(self, node: AVLTreeNode) -> int:
        # returns height of node
        if node != None:
            return node.height
        else:
            return 0
    
    def _get_balance_factor(self, node: AVLTreeNode) -> int:
        if node != None:
            return self._get_height(node.left) - self._get_height(node.right)
        else:
            return 0    
        
    def _update_height(self, node: AVLTreeNode, inserted_node: AVLTreeNode) -> None:
        # Updates the height of each node in the tree from the inserted node up to the root

        if node == None:
            return
        else:
            # Update the height of the current node
            node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

            # Recursively update the height of the parent nodes up to the root
            if node == inserted_node:
                return
            elif inserted_node.key < node.key:
                self._update_height(node.left, inserted_node)
            else:
                self._update_height(node.right, inserted_node)  

    def _inorder_traversal(self, node:AVLTreeNode, tree:list):
        if node != None:
            self._inorder_traversal(node.left,tree)
            tree.append(node.key)
            self._inorder_traversal(node.right,tree)
        return  

# testing

# A = AVLTree()
# # Left Rotation - right right case
# print("Inserting 8")
# A.insert(8,1)
# print("Inserting 9")
# A.insert(9,1)
# print("Inserting 10")
# A.insert(10,2)  
# A.search(8)
# A.display()             

# B = AVLTree()
# # Right Rotation
# print("Inserting 10")
# B.insert(10,1)
# print("Inserting 9")
# B.insert(9,1)
# print("Inserting 8")
# B.insert(8,2)

# C = AVLTree()
# # Right - Left Rotation
# print("Inserting 10")
# C.insert(10,1)
# print("Inserting 12")
# C.insert(12,2)
# print("Inserting 11")
# C.insert(11,3)


# D = AVLTree()
# # Left - Right Rotation
# print("Inserting 10")
# D.insert(10,1)
# print("Inserting 8")
# D.insert(8,2)
# print("Inserting 9")
# D.insert(9,3)