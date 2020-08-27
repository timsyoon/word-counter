# Author: Timothy Yoon
# Date: August 27, 2020
# Description: This file contains an implementation of a hash map. This hash map
# uses a hash table of buckets, where each bucket contains a linked list of
# hash links. Each hash link stores a key-value pair and a pointer to the next
# link in the list.

# hash_map.py
# ===================================================
# Implement a hash map with chaining
# ===================================================


class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, key, value):
        """
        Create a new node and insert it at the front of the linked list.

        :param key: the key for the new node
        :param value: the value for the new node
        """
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key):
        """
        Remove a node from the linked list.

        :param key: the key of the node that is to be removed
        """
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.size = self.size - 1
                return True
            prev = cur
            cur = cur.next
        return False

    def contains(self, key):
        """
        Search the linked list for a node with the given key.

        :param key: the key of the target node
        :return: the node with the matching key, otherwise None
        """
        if self.head is not None:
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head != None:
            cur = self.head
            out = out + str(self.head)
            cur = cur.next
            while cur != None:
                out = out + ' -> ' + str(cur)
                cur = cur.next
        out = out + ']'
        return out


def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash


def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


class HashMap:
    """
    Create a new hash map with the specified number of buckets.

    :param capacity: the total number of buckets to be created in the hash table
    :param function: the hash function to use for hashing values
    """
    def __init__(self, capacity, function):
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0

    def generate_hash_index(self, key):
        """
        Use the HashMap's hash function to generate a hash index from the
        original key.

        :param key: the original key as a string
        :return: an integer representing the hash index, that is, the index
        of the bucket that the key (and its associated value) should go into
        """
        # If the capacity of the table is zero, return None to prevent modulo by
        # zero errors
        if self.capacity == 0:
            return None

        hash_key = self._hash_function(key)
        index = hash_key % self.capacity  # Between 0 and [# of buckets - 1]
        return index

    def get_tuples(self):
        """
        Helper method for top_words() that returns a list of tuples consisting
        of all key-value pairs in the table.

        :return tuple_list: a list of tuples for each key-value pair in the table
        """
        tuple_list = []  # Will store key-value pairs as tuples

        # Iterate over each bucket in the table
        for bucket in self._buckets:
            # If the bucket is not empty, iterate over its nodes
            if bucket.head is not None:
                cur = bucket.head  # Keep track of the current node
                while cur is not None:
                    # Add the key-value pair to tuple_list as a tuple
                    tuple_list.append((cur.key, cur.value))
                    cur = cur.next  # Go to the next node in the bucket

        return tuple_list

    def clear(self):
        """
        Empty out the hash table and delete all its links. The underlying
        hash table capacity is not changed.
        """
        # If the capacity of the table is 0, return None since there are no
        # nodes to be cleared
        if self.capacity == 0:
            return

        # Clear the buckets
        self._buckets = []

        # Add empty buckets to match the capacity
        for i in range(self.capacity):
            self._buckets.append(LinkedList())

        # Set the size of the table to 0 since all nodes have been removed
        self.size = 0

    def get(self, key):
        """
        Return the value associated with the given key.

        :param key: the key (string) to look for
        :return: the value associated with the key. If the key is not in the
        hash map, return None.
        """
        # If the key is not in the hash map, return None
        if not self.contains_key(key):
            return None

        # If the key is in the hash map, get its associated value
        hash_index = self.generate_hash_index(key)  # Get the hash index
        bucket = self._buckets[hash_index]  # Find the right bucket
        target_node = bucket.contains(key)
        return target_node.value

    def resize_table(self, capacity):
        """
        Resize the hash table to have a number of buckets equal to the given
        capacity. All existing key/value pairs remain in the new table and all
        table links are rehashed in the resizing process.

        :param capacity: the new number of buckets that the table will have
        """
        # Create a new hash table with the updated capacity but the same
        # hash function
        new_table = HashMap(capacity, self._hash_function)

        # Iterate over each bucket in the original table, and for each node, put
        # its rehashed form as a node in the new table
        for bucket in self._buckets:
            # If the bucket is not empty, iterate over its nodes
            if bucket.head is not None:
                cur = bucket.head  # Keep track of the current node
                while cur is not None:
                    # Rehash the original key and put the node in the new table
                    new_table.put(cur.key, cur.value)
                    cur = cur.next  # Go to the next node in the bucket

        # Reset the original table as if it were newly made
        self._buckets = []
        self.capacity = 0
        self.size = 0

        # Copy each bucket from the new table to the original table
        for bucket in new_table._buckets:
            self._buckets.append(bucket)

        # Update the size and capacity of the original table
        self.capacity = capacity
        self.size = new_table.size

    def put(self, key, value):
        """
        Update the given key-value pair in the hash table. If a node with the
        given key already exists, this will just update the value and skip
        traversing. Otherwise, it will create a new node with the given key and
        value and add it to the table bucket's linked list.

        :param key: the key associated with the entry
        :param value: the value associated with the entry
        """
        # If the table has a capacity of 0, return None
        if self.capacity == 0:
            return None

        # If the key exists in the table, update the node that has the key
        if self.contains_key(key):
            hash_index = self.generate_hash_index(key)  # Get the hash index
            bucket = self._buckets[hash_index]  # Find the right bucket

            # Find and update the node that contains the key
            node_to_update = bucket.contains(key)  # Either a node or None
            if node_to_update is not None:
                node_to_update.value = value  # Update the node's value

        # If the key does not exist in the table, create a new node with the
        # given key and value and add it to the right bucket
        else:
            hash_index = self.generate_hash_index(key)  # Get the hash index
            bucket = self._buckets[hash_index]  # Find the right bucket

            # Create a new node and add it to the front of the bucket
            bucket.add_front(key, value)
            self.size += 1  # Increment the size of the table

    def remove(self, key):
        """
        Remove the node with the given key from the table. If no such node
        exists, do nothing.

        :param key: the key belonging to the node that is to be removed
        """
        # If the given key is not in the table, simply return None
        if not self.contains_key(key):
            return

        # If the given key is in the table, remove the node that holds the key
        hash_index = self.generate_hash_index(key)  # Get the hash index
        bucket = self._buckets[hash_index]  # Find the right bucket

        # Remove the target node (adapted from LinkedList's remove method)
        if bucket.head is None:  # If the bucket is empty, return None
            return
        # If the head of the bucket has the target key, remove the head node
        if bucket.head.key == key:
            bucket.head = bucket.head.next  # Remove the head node
            bucket.size -= 1  # Decrement the bucket size
            return

        # If a non-head node has the target key, iterate over the nodes until
        # the node to be removed is reached
        cur = bucket.head.next  # Track the current node
        prev = bucket.head  # Track the previous node
        while cur is not None:
            if cur.key == key:  # If the current node has the target key
                prev.next = cur.next  # Remove the current node from the table
                bucket.size -= 1  # Decrement the bucket size

            # If the current node does not have the target key, move to the
            # next node in the bucket
            prev = cur
            cur = cur.next

        self.size -= 1  # Decrement the size of the table

    def contains_key(self, key):
        """
        Search to see if a key exists within the hash table.

        :param key: the key (string) to look for
        :return: True if the key is found, and False otherwise
        """
        # Iterate over each linked list in the hash table array
        for linked_list in self._buckets:
            # Check each node in the linked list for the key
            if linked_list.contains(key) is not None:
                return True

        return False  # If none of the linked lists has the key, return False

    def empty_buckets(self):
        """
        Return the number of empty buckets in the table.

        :return empty_bucket_count:
        """
        # If the table has a capacity of 0, return 0 since there are no empty
        # buckets
        if self.capacity == 0:
            return 0

        # If the table has buckets, iterate over each bucket and count the
        # number of buckets that are empty
        empty_bucket_count = 0

        # Iterate over each bucket
        for bucket in self._buckets:
            # If the bucket's head is None, the bucket is empty
            if bucket.head is None:
                empty_bucket_count += 1

        return empty_bucket_count

    def table_load(self):
        """
        Return the current hash table load factor (the average number of
        elements in each bucket).

        :return: the ratio of number of links to number of buckets in the
        table as a float
        """
        return self.size / self.capacity

    def __str__(self):
        """
        Print all the links in each of the buckets in the table.
        """
        out = ""
        index = 0
        for bucket in self._buckets:
            out = out + str(index) + ': ' + str(bucket) + '\n'
            index = index + 1
        return out
