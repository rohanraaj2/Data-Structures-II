import array

class DynamicArrayList:

    def __init__(self) -> None:
        pass

    def insert(index : int , value) -> None:
        pass

    def delete(index : int) -> None:
        pass

    def get(index : int):
        pass

    def size() -> int:
        pass

    def display() -> str:
        pass    


class Node:

    def __init__(self, data : int) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        # head : pointing to start of list
        # initialized to none as list is empty initially
        self.head = None

    def insert(self, index : int , value : int) -> None:
        node = Node(value)                              # create a new node using Node class

        if index == 0:                                  # if index is 0, that means add at the start of the list
            node.next = self.head
            self.head = node
        else:                                           
            i = self.head                               # if not empty, traverse through the list to find the tail
            count = 0
            while count < index-1 and i.next != None:
                i = i.next    
                count += 1
            node.next = i.next
            i.next = node                               # assign the node to the tail of the list

    def delete(index : int) -> None:
        pass

    def get(index : int):
        pass

    def size() -> int:
        pass

    def display() -> str:
        pass 


def load(file_path, out_file):
    """
    Loads and performs the operations specified in the input file on either a dynamic array list or a linked list.

    :param file_path: the path of the input file
    :type file_path: str
    :param out_file: the name of the output file
    :type out_file: str
    """
    with open(file_path, 'r') as file:
        data_structure = file.readline().strip()
        operations = file.readlines()
        out = []
        if data_structure == "array":
            ds = DynamicArrayList()
        else:
            ds = LinkedList()
        for op in operations:
            op = op.strip().split()
            if op[0] == "delete":
                ds.delete(int(op[1]))
            elif op[0] == "get":
                out.append(ds.get(int(op[1])))
            elif op[0] == "size":
                out.append(ds.size())
            elif op[0] == "display":
                out.append(ds.display())
            elif op[0] == "insert":
                ds.insert(int(op[1]), int(op[2]))
            
        with open(out_file, 'w') as f:
            for item in out:
                f.write("%s\n" % item)
