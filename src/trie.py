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
        words = {}
        for val in prefix: 
            if val in node.children: 
                node = node.children[val] 
            else:
                return words
            word += val
        
        if node.end:
            words[word] = node.locations

        for child, next_child in node.children.items():
            child_completions = self.prefix_complete("", next_child, word + child)
            words.update(child_completions)
    
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