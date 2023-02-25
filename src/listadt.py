import array

class DynamicArrayList:

    def __init__(self, size : int) -> None:
        self.size = size
        self.array = array('i', [-1] * self.size)  # initialize the array with 0

    def insert(self, index : int , value) -> None:
        # check if number of elements in array = size of array
        n = 0                                   
        while self.array[n] != -1:
            n += 1

        # resize if true 
        if n == len(self.array):
            self.size = 2 * n
            arr = array('i', [-1] * self.size)
            for i in range(n):
                arr[i] = self.array[i]
            self.array = arr    

        # add element at index and shift the elements after it to the right
        for i in range(index+1,self.size):
            self.array[i] = self.array[i-1]
        self.array[index] = value

    def delete(self, index : int) -> None:
        # delete element and shift elements left
        for i in range(index,self.size-1):
            self.array[i] = self.array[i+1]
        self.array[self.size-1] = 0    

        # count number of elements
        n = 0                                   
        while self.array[n] != -1:
            n += 1

        # if len >= 3n, reduce array to half size
        if len(self.array) >= 3*n:
            self.size = 2 * n
            arr = array('i', [-1] * self.size)
            for i in range(n):
                arr[i] = self.array[i]
            self.array = arr    

    def get(self, index : int):
        return self.array[index]

    def size(self) -> int:
        return len(self.array)

    def display(self) -> str:
        val = []
        for i in range(self.size):
            val.append(self.array[i])
        return val            

class Node:

    def __init__(self, data : int) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        # head : pointing to start of list, initialized to none as list is empty initially
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

    def delete(self, index : int) -> None:
        if index == 0:
            self.head = self.head.next                  # if you remove the head, the next node is assigned as the new head
        else:
            i = self.head                               
            count = 0
            while count < index - 1 and i.next != None: # traverse through the list to find the index
                i = i.next
                count += 1
            i.next = i.next.next                        # update the next pointer  

    def get(self, index : int):
        i = self.head
        count = 0
        while count < index and i != None:              # traverse through the list to find the index
            i = i.next
            count += 1
        return i.data                                   # return data of node at that index

    def size(self) -> int:
        count = 0
        i = self.head
        while i.next != None:                           # traverse to find end of list
            count += 1
            i = i.next
        return (count + 1)                              # since the last node is not being counted, we return the count+1

    def display(self) -> str:
        val = []
        i = self.head
        while i != None:                                # keep adding the values to val list
            val.append(i.data)
            i = i.next
        return val                                      # return val list ie a list of values from linkedlist


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
