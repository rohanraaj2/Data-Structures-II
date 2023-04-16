import math
from document import Document

class InvertedIndex:

    def __init__(self, Any: list) -> None:
        self.list = Any
        # print (Any)
        

    def query(self, terms:str, k: int) -> list[tuple[int,str]]:
        # returns a sorted list of 2-tuples (or pairs) representing the ranked list of documents
        list_of_words = terms.split()
        number_of_words = len(list_of_words)
        c = 0
        document_list = []
        for i in self.list:
            c += 1
            print ("Document:", c)
            for j in i:
                if j == list_of_words[0]:
                    document_list.append(("Document: ", c))
                    print(j, "(found)")
                    # print()
            print ("document end")
        print (document_list)
        # for word_number in range(len(list_of_words)):
        # x = [([k, terms])]
        # x.sort()
        # print (x)
        # return x


    def and_query(self, query1:str, query2:str, k: int) -> list[tuple[int,str]]:
        # returns the intersection of the ranked list of documents for query1 and query2
        return []


    def or_query(self, query1:str, query2:str, k: int) -> list[tuple[int,str]]:
        # returns the union of the ranked list of documents for query1 and query2
        return []