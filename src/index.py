import math
from document import Document

class InvertedIndex:

    def __init__(self, docs: list) -> None:
        self.inverted_index = {}
        self.list_of_docs = docs
        self.doc_size = {}
        self._create_inverted_index(docs)

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
        pass

    def or_query(self, query1:str, query2:str, k: int) -> list[tuple[int,str]]:
        # returns the union of the ranked list of documents for query1 and query2
        return []
    

    # helper functions

    def _create_inverted_index(self, docs):
        # creates the inverted index that we will be using
        for doc in docs:
            document_id = doc.doc_id

            for word in doc.terms:  
                self.doc_size[id] += len(word)
                word_frequency = len(doc.terms[word])

                if word not in self.inverted_index.keys():  
                    self.inverted_index[word] = {}  
                    
                # calculate the tf.idf of the word 
                tf = (len(doc.terms[word])/len(doc.terms)) 
                idf = self._idf(docs, word) 
                tfidf = tf * idf  

                # add the tfidf for each doc for each word
                self.inverted_index[word][document_id] = (tfidf)
        pass

    def _idf(self, docs : Document, word):
        df = 0 

        for doc in docs: 
            if word in doc.terms:
                df += 1

        idf = math.log(len(docs)/df)  
        return idf