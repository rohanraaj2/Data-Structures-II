import math
from document import Document

class InvertedIndex:

    def __init__(self, docs: list) -> None:
        # creates an inverted index from a list of documents
        self.inverted_index = {}
        self.doc_size = {} # indicates the size of each document in terms of number of words
        self.number_of_documents = len(docs) # to be used in score calculation
        self._create_inverted_index(docs)

    def query(self, terms:str, k: int) -> list[tuple[int,str]]:
        # returns a sorted list of 2-tuples (or pairs) representing the ranked list of documents
        list_of_terms = terms.strip().split() # caters for multiple terms and spaces
        self.scores = {}

        for term in list_of_terms:
            self._calculating_score(term) 

        document_score = []
        for key, value in self.scores.items(): 
            document_score.append((key, value))
            
        document_score.sort(key=lambda x: x[1], reverse=True) # sorts the list of tuples in descending order of score

        ranked_list = []
        rank = 1
        for document in document_score:
            document_id = document[0]
            ranked_list.append((rank, document_id))
            rank += 1

        return ranked_list[:k]

    def and_query(self, query1:str, query2:str, k: int) -> list[tuple[int,str]]:
        # returns the intersection of the ranked list of documents for query1 and query2

        common_docs = []
        query1_doc_list = [element[1] for element in self.query(query1, k)]  # list of doc_id for query1
        query2_doc_list = [element[1] for element in self.query(query2, k)]

        for doc in query1_doc_list:
            if doc in query2_doc_list:
                common_docs.append(doc)

        ranked_list = []
        rank = 1
        for doc_id in (sorted(common_docs)):
            ranked_list.append((rank, doc_id))
            rank += 1

        return ranked_list

    def or_query(self, query1:str, query2:str, k: int) -> list[tuple[int,str]]:
        # returns the union of the ranked list of documents for query1 and query2
        query1_doc_list = [element[1] for element in self.query(query1, k)]  # list of doc_id for query1
        query2_doc_list = [element[1] for element in self.query(query2, k)]
        union_list = query1_doc_list
        for doc in query2_doc_list:
            if doc not in union_list:
                union_list.append(doc)
        union_list.sort()

        ranked_list = []
        rank = 1
        for doc_id in (sorted(union_list)):
            ranked_list.append((rank, doc_id))
            rank += 1

        return ranked_list

    # helper functions

    def _create_inverted_index(self, docs):
        # creates the inverted index that we will be using
        for doc in docs:
            document_id = doc.doc_id
            self.doc_size[document_id] = sum(len(x) for x in doc.terms.values())
            for word in doc:
                word_frequency = len(doc.terms[word])

                if word not in self.inverted_index.keys():  
                    self.inverted_index[word] = [(document_id, word_frequency)]
                else:
                    if self.inverted_index[word][-1][0] != document_id:
                        self.inverted_index[word].append((document_id, word_frequency))
                    
    def _calculating_score(self, word):
        if word in self.inverted_index.keys():
            total_docs_word = len(self.inverted_index[word]) # total docs it has appeared in
            inverse_document_frequency = math.log(self.number_of_documents/total_docs_word)
            for doc in self.inverted_index[word]:
                term_frequency = doc[1] / self.doc_size[doc[0]]
                tf_idf = term_frequency * inverse_document_frequency
                self.scores[doc[0]] = self.scores.get(doc[0], 0) + tf_idf