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

        size = len(elements) * 2 # initializing size to twice the length of the elements list
        self.set = [None] * size # initializing set with None values
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
        hash_value = hash(element) % len(self.set) # getting the hash value of the element

        if element not in self.set:
            index = hash_value
            if index > len(self.set):
                self.set.insert(index, element)
                done = True
            else:
                while type(self.set[index - 1]) == tuple: # not empty
                    index += 1
                    if index > len(self.set): # if index is greater than the length of the list
                        self.set.insert(index, element) # insert the element at the end of the list
                        done = True
                        break
                if done == False:
                    self.set.insert(index, element)

    def discard(self, element: Any) -> None:
        """Removes element from this set.

        there is noting to be done if element is not present in this set.

        Args:
        - self: manadatory reference to this object.
        - element: the element to remove from this set

        Returns:
        None
        """
        if element in self.set: # if element is in the list only then we can remove it
            self.set.remove(element)

    def __iter__(self):
        """Makes this set iterable.

        There are many different ways to implement this. Choose one that works
        for you.

        Args:
        - self: manadatory reference to this object.
        """
        return iter([element for element in self.set if element is not None]) # iterating over the list and returning the elements that are not None


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

    def __init__(self) -> None:
        """Initializes this dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        none
        """
        self.dict = {}

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
        self.dict[key] = newvalue # adding the key and value to the dictionary

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

        if key in self.dict: # if the key is in the dictionary
            return self.dict[key] # return the value
        else:
            return default # else return the default value
    
    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.

        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """
        pair_list = [] # creating an empty list
        for key in self.dict: # iterating over the keys in the dictionary
            pair_list.append((key, self.dict[key])) # appending the key and value to the list
        return pair_list # returning the list

    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """
        self.dict = {} # clearing the dictionary

class LinearDict(MyDict):
    '''Overrides and implementes the methods defined in MyDict. Uses a linear
    probing hash table to implement the dictionary.
    '''

    def __init__(self) -> None:
        """Initializes this dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        none
        """
        self.dict = {}  # creating an empty dictionary

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
        self.dict[key] = newvalue # adding the key and value to the dictionary

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

        if key in self.dict:    # if the key is in the dictionary
            return self.dict[key]  # return the value
        else:   
            return default # else return the default value

    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.

        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """
        pair_list = [] # creating an empty list
        for key in self.dict: # iterating over the keys in the dictionary
            pair_list.append((key, self.dict[key])) # appending the key and value to the list
        return pair_list # returning the list

    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """
        self.dict = {}  # clearing the dictionary
