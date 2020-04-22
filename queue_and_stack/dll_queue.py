import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Queue is first in and first out
class Queue:
    def __init__(self, storage=DoublyLinkedList()):
        # Why is our DLL a good choice to store our elements?
        self.storage = storage
        self.size = 0
    # Add item to the back of the queue
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
    # remove item from the front
    def dequeue(self):
        if self.size == 0:
            return 
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    # return length of items in queue
    def len(self):
        # len starts out at 0
        if self.size == 0:
            return 0
        else:
            return self.size
