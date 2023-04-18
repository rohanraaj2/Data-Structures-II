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
        return document_score[:k]
            # idf = math.log(self.number_of_documents / len(self.inverted_index[term]))

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
            self.doc_size[document_id] = sum(len(x)
                                           for x in doc.terms.values())

            for word in doc.terms:
                self.doc_size[document_id] += len(word)
                word_frequency = len(doc.terms[word])

                if word not in self.inverted_index.keys():  
                    self.inverted_index[word] = [(document_id, word_frequency)]
                else:
                    if self.inverted_index[word][-1][0] != document_id:
                        self.inverted_index[word].append(
                            (document_id, word_frequency))
                    
                # calculate the tf.idf of the word 
                # tf = (len(doc.terms[word])/len(doc.terms)) 
                # idf = self._idf(docs, word) 
                # tfidf = tf * idf  

                # # add the tfidf for each doc for each word
                # self.inverted_index[word][document_id] = (tfidf)

    def _calculating_score(self, word):
        # df = 0 
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
        # for doc in docs: 
        #     if word in doc.terms:
        #         df += 1

        # idf = math.log(len(docs)/df)  
        # return idf