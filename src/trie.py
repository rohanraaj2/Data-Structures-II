from document import Document

class TrieNode:

    def __init__(self, val) -> None:
        self.val = val
        self.children = {}
        self.end = False
        self.locations = []
        pass

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode('')

    def prefix_complete(self, prefix:str, node:TrieNode = None, word: str = "") -> dict[str,list[tuple[str,int,int]]]:
        # returns a dict in which each key is a completion from the corpus and the corresponding value is a list of 3-tuples representing ID, start and end index
        node = self.root
        words = {}                              # empty dictionary to store completions and their locations
        for val in prefix:                      # iterating through the chars in the prefix      
            if val in node.children:            # move to next node if it exists in children of char
                node = node.children[val] 
            else:
                return words                    # return empty dictionary if character is not found in the trie
            word += val                         # updates the word by adding the char 

        words = self._get_collection(node, word) # calls a recursive function to get collection of all words
        return words

    # helper functions

    def _insert_word(self, word, doc, location):
        # inserts a new word in the trie
        node = self.root

        for val in word:
            if val not in node.children:
                node.children[val] = TrieNode(val)
            node = node.children[val]
        node.end = True

        if len(location) != 0:
            for i in range(len(location)):
                start = location[i][0]
                end = location[i][1]
                node.locations.append((doc, start, end))

    def add_document(self, doc : Document):
        # inserts a new doc in the trie
        # inserting a new doc means inserting each word from the doc 
        for word in doc:
            self._insert_word(word, doc.doc_id, doc[word])

    def _get_collection(self, node : TrieNode, prefix : str) -> dict[str, list[tuple[str, int, int]]]:
        # returns a collection of all the words in the trie
        collection = {} 
        if node.end: 
            collection[prefix] = node.locations 

        for child in node.children.values(): 
            collection.update(self._get_collection(child, prefix + child.val))  # recursively calls itself with the child of node and the updated prefix

        return collection        