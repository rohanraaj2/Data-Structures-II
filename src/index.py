import math
from document import Document

class InvertedIndex:

    def __init__(self, docs: list) -> None:
        self.list_of_docs = docs

    def query(self, terms:str, k: int) -> list[tuple[int,str]]:
        # returns a sorted list of 2-tuples (or pairs) representing the ranked list of documents
        list_of_words = terms.split()
        number_of_words = len(list_of_words)

        # x = self.list.__contains__
        c = 0
        document_list = []
        documents_dictionary = {}
        for i in self.list_of_docs:
            c += 1
            # print ("Document:", c)
            t = 0
            for j in i:
                if j == list_of_words[0]:
                    t += 1
                    document_list.append("Doc" + str(c))
                    documents_dictionary["Doc" + str(c)] = t
                    # print(j, "(found)")
                    # print()
            # print ("document end")
        print (document_list)
        print (documents_dictionary)
        # for word_number in range(len(list_of_words)):
        # x = [([k, terms])]
        # x.sort()
        # print (x)
        return document_list


    def and_query(self, query1:str, query2:str, k: int) -> list[tuple[int,str]]:
        # returns the intersection of the ranked list of documents for query1 and query2
        return []


    def or_query(self, query1:str, query2:str, k: int) -> list[tuple[int,str]]:
        # returns the union of the ranked list of documents for query1 and query2
        return []