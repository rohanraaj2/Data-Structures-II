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
        self.set = [[] for _ in range(len(elements))]
        for i in elements:
            # print (i)
            self.add(i)
            # self.x = hash(i) % len(elements)
            # print("HV: ", self.x)
            # self.set.insert(self.x, i)
        # print (elements)
        # print (self.set)
        # self.set = elements.copy()

    def add(self, element: Any) -> None:
        """Adds element to this set.

        element must be hashable by python.

        Args:
        - self: manadatory reference to this object.
        - element: the element to add to this set

        Returns:
        None
        """
        self.hash_value = hash(element) % len(self.set)
        # print ("chain add")
        chain = [element]
        if element not in self.set:
            if self.hash_value > len(self.set):
                self.set.insert(self.hash_value, chain)
            else:
                desired_place_data = self.set[self.hash_value]
                if type(desired_place_data) == tuple:
                    chain.append(element)
                    self.set[self.hash_value] = chain
                    # self.set.insert(self.hash_value, chain)
            # print(self.set)
                    # chain = [desired_place_data, element]
                    # self.set[self.hash_value] = chain
                # elif type(desired_place_data) == list:
                #     desired_place_data.append(element)

    def discard(self, element: Any) -> None:
        """Removes element from this set.

        there is noting to be done if element is not present in this set.

        Args:
        - self: manadatory reference to this object.
        - element: the element to remove from this set

        Returns:
        None
        """
        # print ("discard")
        if element in self.set:
            # print("before:", self.set)
            self.set.remove(element)
            # print("after:", self.set)

    def __iter__(self):
        """Makes this set iterable.

        There are many different ways to implement this. Choose one that works
        for you.

        Args:
        - self: manadatory reference to this object.
        """
        return iter(self.set)


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

        self.set = []
        for i in elements:
            # print (i)
            self.x = hash(i) % len(elements)
            # print("HV: ", self.x)
            self.set.insert(self.x, i)
        # print (elements)
        # print (self.set)
        # self.set = elements.copy()

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
        self.hash_value = hash(element) % len(self.set)

        if element not in self.set:
            index = self.hash_value 
            if index > len(self.set):
                self.set.insert(index, element)
                done = True
            else:
                while type (self.set[index - 1]) == tuple:
                    index += 1
                    if index > len(self.set):
                        self.set.insert(index, element)
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
        # print ("discard")
        if element in self.set:
            # print("before:", self.set)
            self.set.remove(element)
            # print("after:", self.set)

    def __iter__(self):
        """Makes this set iterable.

        There are many different ways to implement this. Choose one that works
        for you.

        Args:
        - self: manadatory reference to this object.
        """
        return iter(self.set)


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
        if type(hash(key) == int):
            self.dict[key] = newvalue

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

        for k in self.dict:
            if k == key:
                return self.dict[key]
        return default
    
    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.

        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """
        pair_list = []
        for key in self.dict:
            # print (key)
            pair_list.append((key, self.dict[key]))
        # print (pair_list)
        return pair_list

    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """
        self.dict.clear()



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
        if type(hash(key) == int):
            self.dict[key] = newvalue

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

        for k in self.dict:
            if k == key:
                return self.dict[key]
        return default

    def items(self) -> [(Any, Any)]:
        """Returns the key-value pairs of the dictionary as tuples in a list.

        Args:
        - self: manadatory reference to this object.

        Returns:
        the key-value pairs of the dictionary as tuples in a list.
        """
        pair_list = []
        for key in self.dict:
            # print (key)
            pair_list.append((key, self.dict[key]))
        # print (pair_list)
        return pair_list

    def clear(self) -> None:
        """Clears the dictionary.

        Args:
        - self: manadatory reference to this object.

        Returns:
        None.
        """
        self.dict.clear()
