# import nltk

class AVLTreeNode:
    pass

class AVLTree:

    def __init__(self) -> None:
        pass

    def  insert (self,key:str,value: tuple[int,int]) -> None:
        # Inserts a (doc id, sen id) tuple into the AVL Tree with the given keyword
        pass

    def search (self,key:str) -> list[tuple[int,int] ] :
        # Searches for a keyword in the AVL Tree and returns a list of (doc id, sen id) corresponding to the keyword. 
        # Returns an empty list if the keyword is not found.
        pass

    def rotate_left(self,node:AVLTreeNode) -> None:
        # Performs a left rotation on the subtree rooted at the given node.
        pass

    def rotate_right(self,node:AVLTreeNode) -> None:
        # Performs a right rotation on the subtree rooted at the given node.
        pass

    def display(self) -> list[str] :
        # Performs an in-order traversal on the AVL Tree and returns a list of keys.
        pass

    pass