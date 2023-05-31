import random
import sys
from typing import Any, Optional


class Node(object):
    '''A node in a skiplist. It stores a (key, value) pair along with pointers
    for each level in its tower.

    The key is used to compare nodes. The tower automatically includes level 0.
    '''

    def __init__(self, data: (Any, Any), height: int = 0) -> None:
        '''Construct node with given data and of given height.

        The height is the largest level, starting from 0, of the tower.

        Parameters:
        - self: mandatory reference to this object
        - data: the (key, value) pair to store in this node
        - height: the number of levels in the tower (excludes level 0)

        Returns:
        None
        '''

        self.node_key, self.key_value = data # key is the first element in the tuple, value is the second element in the tuple
        self.num_of_levels = height # height is the number of levels in the tower
        self.next = [None] * (height) # next is a list of pointers to the next node in the skiplist

    def __repr__(self) -> str:
        '''Returns the representation of this node.

        Implement any representation that helps you debug.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this node's string representation.
        '''
        return f'Node({self.node_key}, {self.key_value}, {self.num_of_levels})'

    def __str__(self) -> str:
        '''Returns a string representation of this node.

        See the link below for the difference between the __repr__ and __str__
        methods: https://www.geeksforgeeks.org/str-vs-repr-in-python/

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this node's string representation.
        '''
        return str(self.__repr__())

    def height(self) -> int:
        '''Returns the height of this node's tower.

        The height is the largest level, starting from 0, of the tower.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the height of this node's tower.
        '''
        return len(self.next)

    def key(self) -> Any:
        '''Returns the key stored in this node.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the key stored in this node.
        '''
        return self.node_key

    def value(self) -> Any:
        '''Returns the value stored in this node.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the value stored in this node.
        '''
        return self.key_value

    def add_level(self, forward: Optional["Node"] = None) -> None:
        '''Adds a level to this node which points to forward.

        Parameters:
        - self: mandatory reference to this object
        - forward: the node that this node will point to in the new level.

        Returns:
        None.
        '''
        self.next.append(forward)
class SkipList(object):
    '''A skiplist of nodes containing (key, value) pairs. Nodes are ordered
    according to keys. Keys are unique, reinserting an existing key overwrites
    the value.

    The skiplist contains a sentinel node by default and the height of the
    sentinel node is the height of the list.
    '''

    def __init__(self) -> None:
        '''Construct empty skiplist.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        None
        '''
        # The head of the skiplist is a sentinel node with a height of 0 by default
        self.head = Node((None, None))
        # The size of the skiplist is 0 by default which represents the number of nodes in the skiplist
        self.size_of_skiplist = 0

    def __len__(self) -> int:
        '''Returns the number of pairs stored in this skiplist.

        dunder method allows calling len() on this object.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the number of pairs stored in this skiplist.
        '''
        return self.size_of_skiplist

    def __repr__(self) -> str:
        '''Returns a string representation of this skiplist.

        Implement any representation that helps you debug.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this skiplist's string representation.
        '''
        # The next node is the first node in the skiplist following the sentinel node
        node = self.head.next[0]
        
        # The values list stores the string representation of each node in the skiplist and is initialized to an empty list
        values = []

        # The while loop iterates through the skiplist and appends the string representation of each node to the values list
        while node is not None: # The while loop terminates when the next node is None
            values.append(str(node)) # The string representation of each node is appended to the values list
            node = node.next[0] # we move to the next node in the skiplist
        return str([{', '.join(values)}]) # The values list is returned as a string

    def __str__(self) -> str:
        '''Returns a string representation of this skiplist.

        See the link below for the difference between the __repr__ and __str__
        methods: https://www.geeksforgeeks.org/str-vs-repr-in-python/

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this skiplist's string representation.
        '''
        return str(self.__repr__())

    def _search_path(self, key: Any) -> [Node]:
        '''Returns the search path in this skiplist for key.

        The search path contains one node for each level of the skiplist
        starting from the highest and ending at level 0. The node for each
        level is the one corresponding to a descend in the search path.

        Parameters:
        - self: mandatory reference to this object
        - key: the key being searched for

        Returns:
        the descend nodes at each level of the skiplist, ordered from highest
        level to level 0.
        '''
        # The path list stores the descend nodes at each level of the skiplist and is initialized to an empty list
        path = []

        # The current_node variable stores the current node in the skiplist and is initialized to the sentinel node
        current_node = self.head

        # The level variable stores the current level of the skiplist and is initialized to the height of the skiplist - 1
        level = self.height() - 1

        # The while loop iterates through the skiplist and appends the descend node at each level to the path list
        while level >= 0: # The while loop terminates when the level is less than 0
            while current_node.next[level] is not None and current_node.next[level].key() <= key: # The while loop terminates when the next node is None or the next node's key is greater than the key being searched for
                current_node = current_node.next[level] # current_node is updated to the next node in the skiplist
            path.append(current_node)
            level -= 1 # we move to the lower level of the skiplist
        return path

    def _find_prev(self, key: Any) -> Node:
        '''Returns the node in the skiplist that contains the predecessor key.

        Parameters:
        - self: mandatory reference to this object
        - key: the key being searched for

        Returns:
        the node in the skiplist that contains the predecessor key.
        '''
        # The current_node variable stores the current node in the skiplist and is initialized to the sentinel node
        current_node = self.head

        # The level variable stores the current level of the skiplist and is initialized to the height of the skiplist - 1
        level = self.height() - 1

        # The while loop iterates through the skiplist and returns the node that contains the predecessor key
        while level >= 0:  # The while loop terminates when the level is less than 0
            while current_node.next[level] is not None and current_node.next[level].key() < key: # The while loop terminates when the next node is None or the next node's key is greater than or equal to the key being searched for
                current_node = current_node.next[level] # current_node is updated to the next node in the skiplist
            level -= 1 # we move to the lower level of the skiplist
        return current_node

    def reset(self) -> None:
        '''Empty the skiplist.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        None
        '''
        # The sentinel node is reinitialized to a sentinel node with a height of 0 by default
        self.head = Node((None, None))

        # The size of the skiplist is reinitialized to 0
        self.size_of_skiplist = 0

    def height(self) -> int:
        '''Returns the height of the skiplist.

        The height is the largest level of the sentinel's tower.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the height of this skiplist.
        '''
        return self.head.num_of_levels

    def find(self, key: Any) -> Optional[Any]:
        '''Returns the value stored in this skiplist corresponding to key, None
        if key does not exist in this skiplist.

        Parameters:
        - self: mandatory reference to this object
        - key: the key whose value is sought

        Returns:
        the stored value for key, None if key does not exist in this skiplist.
        '''
        # we find the previous node to the node that contains the key
        prev = self._find_prev(key)
        if prev.next[0] is not None and prev.next[0].key() == key: # if the next node which represents the node that contains the key is not None and the key of the next node is equal to the key being searched for
            return prev.next[0].value() # we return the value of that node
        return None

    def find_range(self, key1: Any, key2: Any) -> [Any]:
        '''Returns the values stored in this skiplist corresponding to the keys
        between key1 and key2 inclusive in sorted order of keys.

        Parameters:
        - self: mandatory reference to this object
        - key1: starting key in the range of keys whose value is sought
        - key2: ending key in the range of keys whose value is sought

        Returns:
        the stored values for the keys between key1 and key2 inclusive in sorted
        order of keys.
        '''
        # we initialize an empty list to store the values of the nodes in the given range
        values_of_range = []

        # we find the previous node to the node that contains the first key
        current_key = self._find_prev(key1).next[0]

        # we find the previous node to the node that contains the second key
        end_key = self._find_prev(key2).next[0]

        # we iterate through the skiplist and append the values of the nodes in the given range to the list
        while current_key != end_key: # the while loop terminates when the current node is equal to the node that contains the second key which marks the end of the range
            values_of_range.append(current_key.value()) # we append the value of the current node to the list
            current_key = current_key.next[0] # we update the current node to the next node in the skiplist

        # we append the value of the last node in the range to the list
        values_of_range.append(current_key.value())

        # we sort the list in ascending order
        values_of_range.sort()

        return values_of_range

    def remove(self, key: Any) -> Optional[Any]:
        '''Returns the value stored for key in this skiplist and removes
        (key, value) from this skiplist, returns None if key is not stored in
        this skiplist.

        Parameters:
        - self: mandatory reference to this object
        - key: the key to be removed

        Returns:
        the stored value for key in this skiplist, None if key does not exist
        in this skiplist
        '''
        # we find the previous node to the node that contains the key
        prev = self._find_prev(key)

        # we remove the node that contains the key and return the value of that node
        if prev.next[0] is not None and prev.next[0].key() == key: # if the next node which represents the node that contains the key is not None and the key of the next node is equal to the key being searched for
            value = prev.next[0].value() # we store the value of the node that contains the key
            current_node = prev.next[0] # we store the node that contains the key
            for i in range(current_node.num_of_levels): # we iterate through the tower of the node that contains the key
                prev.next[i] = current_node.next[i].next[i] # we update the next node of the previous node to the next node of this node
            self.size_of_skiplist -= 1 # we decrement the size of the skiplist by 1 as we removed a node
            
            # we return the value of the node that contains the key
            return value 
        # we return None if the key is not in the skiplist
        return None

    def _random_level(self) -> int:
        '''Returns a random level for a new node.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        a random level for a new node.
        '''
        # we initialize the level to 1
        level = 1

        # we generate a random number between 0 and 1 and if the number is 1, we increment the level by 1
        while random.randint(0, 1) == 1: # the while loop terminates when the random number is 0
            level += 1
        return level

    def insert(self, data: (Any, Any)) -> None:
        '''Inserts a (key value) pair in this skiplist, overwrites the old value
        if key already exists.

        Parameters:
        - self: mandatory reference to this object
        - data: the (key, value) pair

        Returns:
        None
        '''
        # we store the key and value of the data
        key, value = data

        # we find the previous node to the node that contains the key
        path = (self._search_path(key))


        path.reverse() # we reverse the path since the search path function returns the path in reverse order starting from the highest level to the lowest level


        level = self._random_level() # we generate a random level for the new node
        new_node = Node(data, level) # we create a new node having the random level generated above

        # we add levels to the head node if the random level generated is greater than the height of the skiplist
        while self.height() < level: # the while loop terminates when the height of the skiplist is greater than or equal to the random level generated 
            self.head.add_level(new_node) 
            self.head.num_of_levels += 1 

        # we add the new node to the skiplist
        for step in range(len(path)): 
            if step < level: # we add the new node to the skiplist only if the step is less than the random level generated
                new_node.next[step] = path[step].next[step] # we update the next node of the new node to the next node of the previous node
                path[step].next[step] = new_node # we update the next node of the previous node to the new node
        self.size_of_skiplist += 1 # we increment the size of the skiplist by 1 as we added a node

    def size(self) -> int:
        '''Returns the number of pairs stored in this skiplist.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the number of pairs stored in this skiplist.
        '''
        return self.size_of_skiplist

    def is_empty(self) -> bool:
        '''Returns whether the skiplist is empty.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        True if no pairs are stored in this skiplist, False otherwise.
        '''
        # we return True if the size of the skiplist is 0
        return self.size_of_skiplist == 0
