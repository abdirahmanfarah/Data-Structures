# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is less than current value, go left
        if value < self.value:
            # check if there is a self.left
            if self.left:
                self.left.insert(value)
            else:
                # add node to empty empty space
                self.left = BinarySearchTree(value)
        # if value is more than current value, go right
        else:
            #check if there is a right node
            if self.right:
                self.right.insert(value) 
            else:
                #add node to empty space
                self.right = BinarySearchTree(value)
        # if tree has no value, add value
        # if self is None:
        #     self.value = BinarySearchTree(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target is equal to self.value, reture true
        if target == self.value:
            return True
        
        # if target is less than self.value, go left
        if target < self.value:
            # Check if there is a left node
            if self.left:
                # if there is a left node, return the it so we can begin at the top again.
               return self.left.contains(target)
            # if there is no left node, return False
            else:
                return False
        elif target > self.value:
            # Check if there is a right node
            if self.right:
                # if there is a right node, recurse through to the top
                return self.right.contains(target)
            else:
                return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        # max variable 
        max_value = self.value
        # if there is no right node, root value is max, return root
        if not self.right:
            return max_value
            
        # if there is a right node, go to right node
        if self.right:
            return self.right.get_max()
        # if not, root value is max, return max
        else:
            # return max
            return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
