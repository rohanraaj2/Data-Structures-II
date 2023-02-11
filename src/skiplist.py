import random
import sys
from typing import Any, Optional


class Node(object):
    '''A node in a skiplist. It stores a (key, value) pair along with pointers
    for each level in its tower.

    The key is used to compare nodes. The tower automatically includes level 0.
    '''
    
    def __init__(self, data: (Any,Any), height: int=0) -> None:
        '''Construct node with given data and of given height.

        The height is the largest level, starting from 0, of the tower.

        Parameters:
        - self: mandatory reference to this object
        - data: the (key, value) pair to store in this node
        - height: the number of levels in the tower (excludes level 0)

        Returns:
        None
        '''
        pass

    def __repr__(self) -> str:
        '''Returns the representation of this node.

        Implement any representation that helps you debug.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this node's string representation.
        '''
        pass

    def __str__(self) -> str:
        '''Returns a string representation of this node.

        See the link below for the difference between the __repr__ and __str__
        methods: https://www.geeksforgeeks.org/str-vs-repr-in-python/

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this node's string representation.
        '''
        return self.__repr__()
    
    def height(self) -> int:
        '''Returns the height of this node's tower.

        The height is the largest level, starting from 0, of the tower.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the height of this node's tower.
        '''
        pass

    def key(self) -> Any:
        '''Returns the key stored in this node.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the key stored in this node.
        '''
        pass

    def value(self) -> Any:
        '''Returns the value stored in this node.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the value stored in this node.
        '''
        pass

    def add_level(self, forward: Optional[Node] = None) -> None:
        '''Adds a level to this node which points to forward.

        Parameters:
        - self: mandatory reference to this object
        - forward: the node that this node will point to in the new level.

        Returns:
        None.
        '''
        pass


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
        pass
        
    def __len__(self) -> int:
        '''Returns the number of pairs stored in this skiplist.

        dunder method allows calling len() on this object.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the number of pairs stored in this skiplist.
        '''
        pass

    def __repr__(self) -> str:
        '''Returns a string representation of this skiplist.

        Implement any representation that helps you debug.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this skiplist's string representation.
        '''
        pass
    
    def __str__(self) -> str:
        '''Returns a string representation of this skiplist.

        See the link below for the difference between the __repr__ and __str__
        methods: https://www.geeksforgeeks.org/str-vs-repr-in-python/

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this skiplist's string representation.
        '''
        return self.__repr__()

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
        pass

    def _find_prev(self, key: Any) -> Node:
        '''Returns the node in the skiplist that contains the predecessor key.

        Parameters:
        - self: mandatory reference to this object
        - key: the key being searched for

        Returns:
        the node in the skiplist that contains the predecessor key.
        '''
        pass

    def reset(self) -> None:
        '''Empty the skiplist.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        None
        '''
        pass

    def height(self) -> int:
        '''Returns the height of the skiplist.

        The height is the largest level of the sentinel's tower.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the height of this skiplist.
        '''
        pass

    def find(self, key: Any) -> Optional[Any]:
        '''Returns the value stored in this skiplist corresponding to key, None
        if key does not exist in this skiplist.

        Parameters:
        - self: mandatory reference to this object
        - key: the key whose value is sought

        Returns:
        the stored value for key, None if key does not exist in this skiplist.
        '''
        pass

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
        pass

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
        pass

    def insert(self, data: (Any,Any)) -> None:
        '''Inserts a (key value) pair in this skiplist, overwrites the old value
        if key already exists.

        Parameters:
        - self: mandatory reference to this object
        - data: the (key, value) pair

        Returns:
        None
        '''
        pass

    def size(self) -> int:
        '''Returns the number of pairs stored in this skiplist.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the number of pairs stored in this skiplist.
        '''
        pass
    
    def is_empty(self) -> bool:
        '''Returns whether the skiplist is empty.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        True if no pairs are stored in this skiplist, False otherwise.
        '''
        pass

