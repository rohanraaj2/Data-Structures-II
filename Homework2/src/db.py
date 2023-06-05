from typing import List, Optional
from src.skiplist import SkipList
import csv
# import os


class Table(object):
    '''A table that stores records and allows creation of an index on the
    records according to the values of a specified attribute. The index is used
    to efficiently retrieve records using key values. The index can be
    re-initialized in run-time using a different attribute.
    '''

    def __init__(self) -> None:
        '''Initialize this table with an empty index.

        The index is initialized with an empty skiplist.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        None
        '''
        self.index = SkipList()

    def read(self, csvfile: str) -> None:
        '''Read and store records from the given CSV file.

        Parameters:
        - self: mandatory reference to this object
        - csvfile: path to a csv file that contains the records

        Returns:
        None
        '''
        # Initializing the records list
        self.records = []

        # Opening the CSV file in read mode and encoding it as utf-8 to avoid errors with special characters in the file name
        file = open(csvfile, 'r', encoding='utf-8')

        # Reading the CSV file
        reader = csv.reader(file)

        # Getting the next line in the CSV file
        self.next_line = next(reader)

        for row in reader:  # Iterating over each row in the CSV file
            self.records.append(row)  # Adding the row to the records list

        # Closing the CSV file
        file.close()

    def create_index(self, attribute: str) -> None:
        '''Construct an index using values of the specified attribute.

        attribute must be one of the column headers from the CSV file from which
        the records were read. all values for attribute must be unique.

        Any existing index is lost and a new one is constructed. The constructed
        index is empty if no records are currently stored.

        The index stores (key, value) pairs where the keys are the values of
        attribute. The value is the location, e.g. index, of the corresponding
        record. Note that the value is not the record itself.

        Parameters:
        - self: mandatory reference to this object
        - attribute: the attribute whose values are to be the keys in the index

        Returns:
        None
        '''
        # Resetting the index
        self.index.reset()

        # Getting the index of the attribute
        ix = self.next_line.index(attribute)

        for line in range(len(self.records)):  # Iterating over each record
            # Inserting the key and value into the index
            self.index.insert((self.records[line][ix], line))

    def select(self, key: str) -> Optional[List[str]]:
        '''Return the record corresponding to the given key, None in case of
        error.

        The index is used to find the record. An error occurs if the index is
        not yet created or the key in invalid. This is indicated by a return of
        None.

        Parameters:
        - self: mandatory reference to this object
        - key: the key whose corresponding value is sought

        Returns:
        The record corresponding to key, None in case of error.
        '''
        if self.index.size() == 0:  # If the index is empty,
            return None
        else:
            if self.index.find(key) is None:  # If the key is not found in the index,
                return None
            else:  # If the key is found in the index,
                return self.records[self.index.find(key)]  # Return the record

    def select_range(self, start: str, end: str) -> Optional[List[List[str]]]:
        '''Returns the records corresponding to the keys in the range
        [start,end] inclusive, None in case of error.

        An error occurs if no index has been created, start or end is not a valid
        key in the index, or start is not less than end.

        Parameters:
        - self: mandatory reference to this object
        - start: the starting key value in the range of keys
        - end: the ending key value in the range of keys

        Returns:
        The records in the order of the keys in the range [start,end], None in
        case of error.
        '''
        # Initializing the list of records
        records_of_range = []

        # if the index is empty or start is greater than end, we return None
        if self.index.size() == 0 or start > end:
            return None

        # Finding the indexes of the start and end keys
        indexlist = self.index.find_range(str(start), str(end))

        # If we do not get the indexes, we return None
        if indexlist == None:
            return None

        # Iterating over the indexes and appending the records to the list records_of_range
        for i in indexlist:
            records_of_range.append(self.records[i])

        return records_of_range

    def delete(self, key: str) -> Optional[List[str]]:
        '''Deletes the record corresponding to key from the table and the index.
        Returns the deleted record, None in case of error.

        An error occurs if no index has been created, or key does not exist in
        it.

        Parameters:
        - self: mandatory reference to this object
        - from: the starting key value in the range of keys
        - to: the ending key value in the range of keys

        Returns:
        The deleted record,  None in case of error.
        '''

        # Storing the index of the key in key_index
        key_index = self.index.find(key)

        # If the key is not found in the index, we return None
        if key_index is None:
            return None

        # Deleting the key from the index
        self.index.remove(key)

        # Returning the record
        return self.records.pop(key_index)
