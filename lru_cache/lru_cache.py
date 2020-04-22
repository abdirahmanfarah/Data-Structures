import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, key, limit=10):
        self.limit = limit
        # current size
        self.size = 0
        # store key and value in hashtable
        self.hash = {}
        # Get methods from doublylinkedlist
        self.storage = DoublyLinkedList()
        # storage dict
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if value of key is none, return none
        if key == None:
            return None
        # if key is present, return value, and use method 'move-to-end'
        
        elif key in self.hash:
            node = self.hash[key]
            # self.storage.remove_from_head()
            self.storage.move_to_end(node)
            return node.value[1]

        # move key-value pair to end of list

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # variable to store key-pair values
        # add a new key-value pairs
        if key in self.hash:
            node = self.hash[key]
            node.value = (key, value)
            self.storage.move_to_end(node)
            return
        # new keyvalue is most recently used == tail
        # if cache is max, oldest entry == head is overwritten
        if self.size == self.limit:
            # var to get the value of head
            oldest_entry = self.storage.head.value[0]
            # delete the head's value
            del self.hash[oldest_entry]
            # remove from head
            self.storage.remove_from_head()
            self.size -= 1
        # if key already exists, overwrite old value with new value
        self.storage.add_to_tail((key, value))
        self.hash[key] = self.storage.tail
        self.size +=1
