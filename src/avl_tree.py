# import nltk

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

    def  insert (self, key:str, value: tuple[int,int]) -> None:
        # Inserts a (doc id, sen id) tuple into the AVL Tree with the given keyword

        node = AVLTreeNode(key,value)           # create a node to add in the tree

        # add the node as you would in binary tree
        # case 1: tree is empty
        if (self.root == None):
            self.root = node
            return                              # no need to go ahead in the function

        # case 2: node is smaller than existing node
        # case 3: node is larger than existing node
        else:
            temp = self.root
            while temp != None:
                parent = temp
                if key < temp.key:
                    temp = temp.left
                elif key > temp.key:  
                    temp = temp.right  
            temp = node 

            if key < parent.key:
                parent.left = temp
            else:
                parent.right = temp           

        # update the height of each node in the tree
        self._update_height(self.root, node)                                             

        # check balance factor and rotate if necessary
        bf = self._get_balance_factor(self.root)
        
        # left-left case working
        if bf > 1 and (key < self.root.left.key):
            self.root = self.rotate_right(self.root)

        # right-right case working
        elif bf < -1 and key >= parent.right.key:
            self.root = self.rotate_left(parent)

        # left-right case
        elif bf > 1 and key >= parent.left.key:
            parent.left = self.rotate_left(parent.left)
            self.root = self.rotate_right(parent)

        # right-left case working
        elif bf < -1 and (key < self.root.right.key):
            self.root.right = self.rotate_right(self.root.right)
            self.root = self.rotate_left(self.root)    

    def search (self, key:str) -> list[tuple[int,int]] :
        # Searches for a keyword in the AVL Tree and returns a list of (doc id, sen id) corresponding to the keyword. 
        # Returns an empty list if the keyword is not found.
        temp = self.root

        while temp != None:
            if key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right       
            else:
                return temp.value
            return []
        pass

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

        temp = self.root
        prev = None
        parent = None

        while temp != None:
            if prev == parent:
                if temp.left != None:
                    next = temp.left
                elif temp.right != None:
                    next = temp.right
                else:
                    next = parent
            elif prev == temp.left:
                if temp.right != None:
                    next = temp.right
                else:
                    next = parent
            else:
                next = parent

            tree.append(temp.key)
            prev = temp
            temp = next      

        return tree                         

    # helper functions to make coding easier

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

# testing

# A = AVLTree()
# # Left Rotation - right right case
# print("Inserting 8")
# A.insert(8,1)
# print("Inserting 9")
# A.insert(9,1)
# print("Inserting 10")
# A.insert(10,2)                

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