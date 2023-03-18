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

        # update heights, check bf and rotate if necessary
        temp = node
        while temp != None:
            temp.height = 1 + max(self._get_height(temp.left), self._get_height(temp.right))
            bf = self._get_height(temp.left) - self._get_height(temp.right)             # balance factor is within range if between -1 < bf < 1

            # case 1: left-left
            if bf > 1 and self._get_balance_factor(temp.left) >= 0:         
                temp = self.rotate_right(temp)  
                self.display()          

            # case 2: right-right
            elif bf > 1 and self._get_balance_factor(temp.left) < 0:
                temp.left = self.rotate_left(temp.left)
                temp = self.rotate_right(temp)
                self.display() 

            # case 3: left-right
            elif bf < -1 and self._get_balance_factor(temp.right) <= 0:
                temp = self.rotate_left(temp)
                self.display() 

            # case 4: right- left
            elif bf < -1 and self._get_balance_factor(temp.right) > 0:
                temp.right = self.rotate_right(temp.right)
                temp = self.rotate_left(temp)
                self.display() 

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
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root
        pass

    def rotate_right(self, node:AVLTreeNode) -> AVLTreeNode:
        # Performs a right rotation on the subtree rooted at the given node.
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root
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
        return node.height
    
    def _get_balance_factor(self, node: AVLTreeNode) -> int:
        return self._get_height(node.left) - self._get_height(node.right)