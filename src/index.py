import math
from document import Document

class InvertedIndex:

    def __init__(self, docs: list) -> None:
        self.inverted_index = {}
        self.list_of_docs = docs
        self.doc_size = {}
        self.number_of_documents = len(docs)
        self._create_inverted_index(docs)

    def query(self, terms:str, k: int) -> list[tuple[int,str]]:
        # returns a sorted list of 2-tuples (or pairs) representing the ranked list of documents
        list_of_terms = terms.strip().split()
        number_of_words = len(list_of_terms)

        for term in list_of_terms:
            self._calculating_score(term)

        document_score = []
        for key, value in self.scores.items():
            document_score.append((key, value))
            
        document_score.sort(key=lambda x: x[1], reverse=True)

        ranked_list = []
        rank = 1
        for document in document_score:
            document_id = document[0]
            ranked_list.append((rank, document_id))
            rank += 1

        return ranked_list[:k]

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
            self.doc_size[document_id] = sum(len(x)
                                           for x in doc.terms.values())

            for word in doc:
                word_frequency = len(doc.terms[word])

                if word not in self.inverted_index.keys():  
                    self.inverted_index[word] = [(document_id, word_frequency)]
                else:
                    if self.inverted_index[word][-1][0] != document_id:
                        self.inverted_index[word].append(
                            (document_id, word_frequency))
                    
    def _calculating_score(self, word):
        scores = {}
        if word in self.inverted_index.keys():
            # total docs it has appeared in
            total_docs_word = len(self.inverted_index[word])
            inverse_document_frequency = math.log(
                self.number_of_documents/total_docs_word)
            # return self.inverted_index[word]
            for doc in self.inverted_index[word]:
                term_frequency = doc[1] / self.doc_size[doc[0]]
                tf_idf = term_frequency * inverse_document_frequency
                scores[doc[0]] = scores.get(doc[0], 0) + tf_idf
        self.scores = scores