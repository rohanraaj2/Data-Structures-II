from typing import Any


class MySet(object):
    '''An abstract class that provides a set interface which is just sufficient
    for the implementation of this assignment.
    '''

    def __init__(self, elements: [Any]) -> None:
        """Initializes this set with elements.

        Each element in elements must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - elements: this set is populated with these elements.

        Returns:
        None
        """

        pass

    def add(self, element: Any) -> None:
        """Adds element to this set.

        element must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - element: the element to add to this set

        Returns:
        None
        """

        pass

    def discard(self, element: Any) -> None:
        """Removes element from this set.

        there is noting to be done if element is not present in this set.

        Args:
        - self: manadatory reference to this object.
        - element: the element to remove from this set

        Returns:
        None
        """
        
        pass
    
    def __iter__(self):
        """Makes this set iterable.

        There are many different ways to implement this. Choose one that works
        for you.

        Args:
        - self: manadatory reference to this object.
        """

        pass

class ChainedSet(MySet):
    '''Overrides and implementes the methods defined in MySet. Uses a chained
    hash table to implement the set.
    '''

    def __init__(self, elements: [Any]) -> None:
        """Initializes this set with elements.

        Each element in elements must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - elements: this set is populated with these elements.

        Returns:
        None
        """
        self.set = [[] for _ in range(len(elements))] # initializing set with empty lists
        for element in elements:
            self.add(element)

    def add(self, element: Any) -> None:
        """Adds element to this set.

        element must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - element: the element to add to this set

        Returns:
        None
        """
        hash_value = hash(element) % len(self.set) # getting the hash value of the element
        chain = self.set[hash_value] # getting the list at the index of the hash value
        if element not in chain:
            chain.append(element) 

    def discard(self, element: Any) -> None:
        """Removes element from this set.

        there is noting to be done if element is not present in this set.

        Args:
        - self: manadatory reference to this object.
        - element: the element to remove from this set

        Returns:
        None
        """
        chain = self.set[hash(element) % len(self.set)] # getting the list at the index of the hash value
        if element in chain:
            chain.remove(element)

    def __iter__(self):
        """Makes this set iterable.

        There are many different ways to implement this. Choose one that works
        for you.

        Args:
        - self: manadatory reference to this object.
        """
        for chain in self.set:
            yield from chain # yield from is used to iterate over the elements in the list


class LinearSet(MySet):
    '''Overrides and implementes the methods defined in MySet. Uses a linear
    probing hash table to implement the set.
    '''

    def __init__(self, elements: [Any]) -> None:
        """Initializes this set with elements.

        Each element in elements must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - elements: this set is populated with these elements.

        Returns:
        None
        """

        # initializing size to twice the length of the elements list
        size = len(elements) * 2
        self.set = [None] * size  # initializing set with None values
        for element in elements:
            self.add(element)

    def add(self, element: Any) -> None:
        """Adds element to this set.

        element must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - element: the element to add to this set

        Returns:
        None
        """
        index = 0
        done = False
        # getting the hash value of the element
        hash_value = hash(element) % len(self.set)

        if element not in self.set:
            index = hash_value
            if index > len(self.set) - 1:
                self.set[index] = element
                done = True
            else:
                while self.set[index] is not None:  # not empty
                    index += 1
                    # if index is greater than the length of the list
                    if index > len(self.set) - 1:
                        # insert the element at the end of the list
                        self.set.append(element)
                        done = True
                        break
                if not done:
                    self.set[index] = element

    def discard(self, element: Any) -> None:
        """Removes element from this set.

        there is noting to be done if element is not present in this set.

        Args:
        - self: manadatory reference to this object.
        - element: the element to remove from this set

        Returns:
        None
        """
        if element in self.set:  # if element is in the list only then we can remove it
            self.set.remove(element)

    def __iter__(self):
        """Makes this set iterable.

        There are many different ways to implement this. Choose one that works
        for you.

        Args:
        - self: manadatory reference to this object.
        """
        return iter([element for element in self.set if element is not None])  # iterating over the list and returning the elements that are not None

class MyDict(object):
    '''An abstract class that provides a dictionary interface which is just
    sufficient for the implementation of this assignment.
    '''
    def __init__(self) -> None:
        """Initializes this dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        none
        """

        pass

    def __setitem__(self, key: Any, newvalue: Any) -> None:
        """Adds (key, newvalue) to the dictionary, overwriting any prior value.

        dunder method allows assignment using indexing syntax, e.g.
        d[key] = newvalue

        key must be hashable by pytohn.

        Args:
        - self: manadatory reference to this object.
        - key: the key to add to the dictionary
        - newvalue: the value to store for the key, overwriting any prior value 

        Returns:
        None
        """
        pass

    def get(self, key: Any, default: Any = None) -> Any:
        """Returns the value stored for key, default if no value exists.

        key must be hashable by pytohn.

        Args:
        - self: manadatory reference to this object.
        - key: the key whose value is sought.
        - default: the value to return if key does not exist in this dictionary

        Returns:
        the stored value for key, default if no such value exists.
        """

        pass

    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.

        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """
        
        pass

    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """

        pass

class ChainedDict(MyDict):
    '''Overrides and implementes the methods defined in MyDict. Uses a chained
    hash table to implement the dictionary.
    '''

    def __init__(self, size=10) -> None:
        """Initializes this dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        none
        """
        self.size = size # size of the hash table
        self.hash_table = [[] for _ in range(size)] # initializing the hash table with empty lists
        self.num_pairs = 0 # number of key-value pairs in the dictionary

    def __setitem__(self, key: Any, newvalue: Any) -> None:
        """Adds (key, newvalue) to the dictionary, overwriting any prior value.

        dunder method allows assignment using indexing syntax, e.g.
        d[key] = newvalue

        key must be hashable by pytohn.
        
        Args:
        - self: manadatory reference to this object.
        - key: the key to add to the dictionary
        - newvalue: the value to store for the key, overwriting any prior value 

        Returns:
        None
        """
        index = hash(key) % self.size # finding the index of the hash table where the key-value pair should be stored
        chain = self.hash_table[index] # the list at the index of the hash table
        for index, (key_in_chain, value_in_chain) in enumerate(chain): # iterating over the list
            if key_in_chain == key: # if the key is already present in the list, then we update the value
                chain[index] = (key, newvalue) 
                return
        chain.append((key, newvalue)) # if the key is not present in the list, then we append the key-value pair to the list
        self.num_pairs += 1 # incrementing the number of key-value pairs in the dictionary
        
        if self.num_pairs / self.size >= 0.75: # if the load factor is greater than or equal to 0.75, then we resize the hash table
            self._resize(self.size * 2) # resizing the hash table by doubling its size

    def get(self, key: Any, default: Any = None) -> Any:
        """Returns the value stored for key, default if no value exists.

        key must be hashable by pytohn.
        
        Args:
        - self: manadatory reference to this object.
        - key: the key whose value is sought.
        - default: the value to return if key does not exist in this dictionary

        Returns:
        the stored value for key, default if no such value exists.
        """
        index = hash(key) % self.size # finding the index of the hash table where the key-value pair should be stored
        chain = self.hash_table[index] # the list at the index of the hash table
        for key_in_chain, value_in_chain in chain: 
            if key_in_chain == key: # if the key is present in the list, then we return the value
                return value_in_chain
        return default # if the key is not present in the list, then we return the default value

    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.
        
        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """

        pair_list = []  # creating an empty list
        for lists in self.hash_table: # iterating over the hash table
            for tuples in lists: # iterating over the lists in the hash table
                if tuples is not None: # if the list is not empty, then we append the key-value pairs to the list
                    pair_list.append(tuples)
        return pair_list  # returning the list

    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """
        self.hash_table = [[] for _ in range(self.size)] # initializing the hash table with empty lists
        self.num_pairs = 0 # number of key-value pairs in the dictionary

    def _resize(self, new_size: int) -> None:

        new_table = [[] for _ in range(new_size)] # creating a new hash table with the new size
        for chain in self.hash_table:
            for key, value in chain: # iterating over the lists in the hash table
                new_chain = new_table[hash(key) % new_size]
                new_chain.append((key, value)) # appending the key-value pair to the list at the index of the new hash table
        self.hash_table = new_table # updating the hash table
        self.size = new_size

class LinearDict(MyDict):
    '''Overrides and implementes the methods defined in MyDict. Uses a linear
    probing hash table to implement the dictionary.
    '''

    def __init__(self, size=10) -> None:
        """Initializes this dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        none
        """
        self.size = size # size of the hash table
        self.hash_table = [None] * size # initializing the hash table with None
        self.num_pairs = 0 # number of key-value pairs in the dictionary

    def __setitem__(self, key: Any, newvalue: Any) -> None:
        """Adds (key, newvalue) to the dictionary, overwriting any prior value.

        dunder method allows assignment using indexing syntax, e.g.
        d[key] = newvalue

        key must be hashable by pytohn.
        
        Args:
        - self: manadatory reference to this object.
        - key: the key to add to the dictionary
        - newvalue: the value to store for the key, overwriting any prior value 

        Returns:
        None
        """
        index = hash(key) % self.size # finding the index of the hash table where the key-value pair should be stored
        while self.hash_table[index] is not None: # while the index is not empty
            if self.hash_table[index][0] == key: # if the key is already present in the hash table, then we update the value
                self.hash_table[index] = (key, newvalue)
                return
            index = (index + 1) % self.size # if the key is not present in the hash table, then we increment the index by 1
        self.hash_table[index] = (key, newvalue) # if the index is empty, then we add the key-value pair to the hash table
        self.num_pairs += 1 # incrementing the number of key-value pairs in the dictionary
        
        if self.num_pairs / self.size >= 0.75: # if the load factor is greater than or equal to 0.75, then we resize the hash table
            self._resize(self.size * 2) # resizing the hash table by doubling its size

    def get(self, key: Any, default: Any = None) -> Any:
        """Returns the value stored for key, default if no value exists.

        key must be hashable by pytohn.
        
        Args:
        - self: manadatory reference to this object.
        - key: the key whose value is sought.
        - default: the value to return if key does not exist in this dictionary

        Returns:
        the stored value for key, default if no such value exists.
        """
        index = hash(key) % self.size # finding the index of the hash table where the key-value pair should be stored
        while self.hash_table[index] is not None: # while the index is not empty
            if self.hash_table[index][0] == key: # if the key is present in the hash table, then we return the value
                return self.hash_table[index][1] 
            index = (index + 1) % self.size # if the key is not present in the hash table, then we increment the index by 1
        return default # if the index is empty, then we return the default value

    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.
        
        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """

        pair_list = []  # creating an empty list
        for tuples in self.hash_table:  # iterating over the keys in the dictionary
            if tuples is not None: # if the list is not empty, then we append the key-value pairs to the list
                pair_list.append(tuples)
        return pair_list  # returning the list

    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """
        self.hash_table = [None] * self.size # initializing the hash table with None
        self.num_pairs = 0 

    def _resize(self, new_size: int) -> None:
            
        new_table = [None] * new_size # creating a new hash table with the new size
        for key, value in self.items(): # iterating over the lists in the hash table
            index = hash(key) % new_size # finding the index of the hash table where the key-value pair should be stored
            while new_table[index] is not None: # finding the next empty index in the hash table
                index = (index + 1) % new_size 
            new_table[index] = (key, value) # appending the key-value pair to the list at the index of the new hash table
        self.hash_table = new_table # updating the hash table
        self.size = new_size # updating the size of the hash table
