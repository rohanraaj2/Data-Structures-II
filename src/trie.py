from document import Document

class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.end = False
        pass

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,word):
        pass

    def prefix_complete(self, prefix:str, node:TrieNode = None, word: str = "") -> list[tuple[int,int,str]]:
        # returns a dict in which each key is a completion from the corpus and the corresponding value is a list of 3-tuples representing ID, start and end index
        
        pass 
