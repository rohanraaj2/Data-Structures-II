import math
from document import Document

class InvertedIndex:

    def __init__(self, docs: list) -> None:
        # creates an inverted index from a list of documents
        self.inverted_index = {}
        self.doc_size = {}
        self.number_of_documents = len(docs) # to be used in score calculation
        self._create_inverted_index(docs)

    # helper functions

    def _create_inverted_index(self, docs): # creates the inverted index that we will be using
        for doc in docs: # for each document
            document_id = doc.doc_id 
            self.doc_size[document_id] = sum(len(x) for x in doc.terms.values()) # stores the size of each document in terms of number of words
            for word in doc: # for each word in the document, we store the document id and the frequency of the word in the dictionary
                word_frequency = len(doc.terms[word]) # number of times the word appears in the document by calculating the length of the number of values in the dictionary terms having the key word

                if word not in self.inverted_index.keys(): # if the word is not in the inverted index, we add it
                    self.inverted_index[word] = [(document_id, word_frequency)]
                else: # the word is already in the inverted index
                    if self.inverted_index[word][-1][0] != document_id: # if the document id is not the same as the last document id in the list of tuples for that word
                        self.inverted_index[word].append((document_id, word_frequency)) # we add the document id and the frequency of the word in the dictionary to the list of tuples for that word

    def _calculating_score(self, word): # calculates the score for each document containing the word
        if word in self.inverted_index.keys():
            total_docs_word = len(self.inverted_index[word]) # total number of documents containing the word
            inverse_document_frequency = math.log(self.number_of_documents/total_docs_word) 
            for doc in self.inverted_index[word]: # for each document containing the word
                term_frequency = doc[1] / self.doc_size[doc[0]] 
                tf_idf = term_frequency * inverse_document_frequency
                self.scores[doc[0]] = self.scores.get(doc[0], 0) + tf_idf # we add the tf-idf score to the score of the document. If the document is not in the dictionary, tf-idf is added to 0

    # main functions
    
    def query(self, terms:str, k: int) -> list[tuple[int,str]]: # returns a sorted list of 2-tuples (or pairs) representing the ranked list of documents
        list_of_terms = terms.strip().split() # caters for multiple terms and spaces
        self.scores = {}

        for term in list_of_terms: # for each term in the query
            self._calculating_score(term)

        document_score = []
        for key, value in self.scores.items(): # creates a list of tuples in the form (document_id, score)
            document_score.append((key, value))
            
        document_score.sort(key=lambda x: x[1], reverse=True) # sorts the list of tuples in descending order of score

        ranked_list = []
        rank = 1
        for document in document_score: # creates a list of tuples in the form (rank, document_id)
            document_id = document[0]
            ranked_list.append((rank, document_id))
            rank += 1

        return ranked_list[:k] # returns the top k documents

    def and_query(self, query1:str, query2:str, k: int) -> list[tuple[int,str]]: # returns the intersection of the ranked list of documents for query1 and query2

        common_docs = []
        query1_doc_list = [element[1] for element in self.query(query1, k)] # list of doc_id for query1
        query2_doc_list = [element[1] for element in self.query(query2, k)] # list of doc_id for query2

        for doc in query1_doc_list:
            if doc in query2_doc_list: # if the document is in both lists, we add it to the list of common documents
                common_docs.append(doc)
        common_docs.sort()

        ranked_list = []
        rank = 1
        for doc_id in (common_docs): # creates a list of tuples in the form (rank, document_id)
            ranked_list.append((rank, doc_id))
            rank += 1

        return ranked_list

    def or_query(self, query1:str, query2:str, k: int) -> list[tuple[int,str]]: # returns the union of the ranked list of documents for query1 and query2

        query1_doc_list = [element[1] for element in self.query(query1, k)] # list of doc_id for query1
        query2_doc_list = [element[1] for element in self.query(query2, k)] # list of doc_id for query2

        union_list = query1_doc_list

        for doc in query2_doc_list: # adds the documents in query2 not in query1 to the union list
            if doc not in union_list:
                union_list.append(doc)

        union_list.sort()

        ranked_list = []
        rank = 1
        for doc_id in (union_list): # creates a list of tuples in the form (rank, document_id)
            ranked_list.append((rank, doc_id))
            rank += 1

        return ranked_list

    