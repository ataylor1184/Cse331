########################################
# PROJECT: Binary Min Heap and Sort
# Author: Alex Taylor
########################################

class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []


    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        rtr_str = "["
        rtr_str += str(self.table[0])
        for i in range(1, len(self.table)):
            rtr_str += "," + str(self.table[i])
        rtr_str += "]"
        return rtr_str

    def get_size(self):
        """
        returns the size off the heap
        :return integer: length of heap
        """
        return len(self.table)

    def parent(self, position):
        """
        finds the index of the node has a parent
        :param position: the position of the node to evaluate
        :return integer: index of the parent
        """
        return (position - 1) // 2

    def left_child(self, position):
        """
        finds the index of the node has a left child
        :param position: the position of the node to evaluate
        :return integer: index of the left child
        """
        return 2*(position) + 1

    def right_child(self, position):
        """
        finds the index of the right child
        :param position: the position of the node to evaluate
        :return integer: index of the right child
        """
        return 2*(position) + 2

    def has_left(self, position):
        """
        determines if the node has a left child
        :param position: the position of the node to evaluate
        :return boolean: true or false
        """
        return self.left_child(position) < len(self.table)

    def has_right(self, position):
        """
        determines if the node has a right child
        :param position: the position of the node to evaluate
        :return: true or false
        """
        return self.right_child(position) < len(self.table)

    def find(self, value):
        """
        finds a given value in the heap
        :param value: the value to find
        :return i: the index the value is found at, or else none
        """
        for i in range(0, self.get_size()):
            if self.table[i] == value:
                return i
        return None

    def heap_push(self, value):
        """
        adds a given value in the heap
        :param value: the value to add
        :return: no return
        """
        if self.find(value) is None:
            self.table.append(value)
            self.percolate_up(len(self.table) - 1)  # upheap newly added position

    def heap_pop(self, value):
        """
        removes a given value in the heap
        :param value: the value to remove
        :return: no return
        """
        if self.find(value) is not None:
            index = self.find(value)
            self.swap(index, len(self.table) - 1)  # put item at the end
            self.table.pop()
            self.percolate_down(index)

    def pop_min(self):
        """
        removes the lowest element in the heap
        :return: no return
        """
        if self.get_size() == 0:
            return None
        self.swap(0, len(self.table) - 1)  # put minimum item at the end
        item = self.table.pop()  # and remove it from the list;
        self.percolate_down(0)  # then fix new root
        return item

    def swap(self, p1, p2):
        """
        swap the contents at 2 points in the heap
        :param p1, p2: two points in the heap
        :return: no return
        """
        self.table[p1], self.table[p2] = self.table[p2], self.table[p1]

    def percolate_up(self, position):
        """
        Moves a node up the heap to correct position
        :param position: current position in the heap
        :return: no return
        """
        parent = self.parent(position)
        if position > 0 and self.table[position] < self.table[parent]:
            self.swap(position, parent)
            self.percolate_up(parent)  # recur at position of parent

    def percolate_down(self, position):
        """
        Moves a node down the heap to correct position
        :param position: current position in the heap
        :return: no return
        """
        if self.has_left(position):
            left = self.left_child(position)
            small_child = left               # although right may be smaller
            if self.has_right(position):
                right = self.right_child(position)
                if self.table[right] < self.table[left]:
                 small_child = right
            if self.table[small_child] < self.table[position]:
                self.swap(position, small_child)
                self.percolate_down(small_child)    # recur at position of small child

def heap_sort(unsorted):
    """
    Sorts a list by using a heap
    :param unsorted: unsorted list
    :return: the sorted list.
    """
    sort_heap = BinaryMinHeap()
    for i in range(0, len(unsorted)):
        sort_heap.heap_push(unsorted.pop())
    for i in range(0, len(sort_heap.table)):
        unsorted.append(sort_heap.pop_min())
    return unsorted
