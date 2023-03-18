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

        # case 2: node is smaller than existing node
        # case 3: node is larger than existing node
        else:
            temp = self.root
            while (temp != None):
                parent = temp
                if (key < temp.key):
                    temp = temp.left
                elif (key > temp.key):  
                    temp = temp.right  
                    
            temp = node 
            if (key < parent.key):
                parent.left = temp
            else:
                parent.right = temp           

        # check heights and rotate if necessary
        

        # case 1: left-left
            

        # case 2: right-right
        # case 3: left-right
        # case 4: right- left


    def search (self, key:str) -> list[tuple[int,int] ] :
        # Searches for a keyword in the AVL Tree and returns a list of (doc id, sen id) corresponding to the keyword. 
        # Returns an empty list if the keyword is not found.
        pass

    def rotate_left(self, node:AVLTreeNode) -> AVLTreeNode:
        # Performs a left rotation on the subtree rooted at the given node.
        pass

    def rotate_right(self, node:AVLTreeNode) -> AVLTreeNode:
        # Performs a right rotation on the subtree rooted at the given node.
        pass

    def display(self) -> list[str] :
        # Performs an in-order traversal on the AVL Tree and returns a list of keys.
        pass
