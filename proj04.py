"""
# Project 4
# Name: Alex Taylor
# PID: A53347473
"""

class Stack:
    """
    Stack class
    """
    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        """
        Displays the number of elements in the stack
        :return: integer number of elements in stack
        """
        return self.size

    def is_empty(self):
        """
        Displays True or False if the stack is empty or not
        :return: boolean True or False
        """
        if self.size:
            return False
        return True

    def top(self):
        """
        Displays the last element added to the stack
        :return: integer number of last element 
        """
        if self.is_empty():
            return None
        return self.data[self.size - 1]

    def push(self, val):
        """
        Adds a element to the top of the stack
        :param: integer value to add
        :return: No return
        """
        if self.size == self.capacity:
            self.grow()
        self.data[self.size] = val
        self.size += 1

    def pop(self):
        """
        Removes a element from the top of the stack
        :return: Integer element that was removed
        """
        if self.is_empty():
            return None
        removed = self.data[self.size-1]
        self.data[self.size-1] = None
        self.size -= 1
        if self.size <= self.capacity // 2 and self.capacity >= 4:
            self.shrink()
        return removed

    def grow(self):
        """
        Doubles capacity of stack if needed
        :return: No return
        """
        new = Stack()
        new.capacity = self.capacity * 2
        new.data = [None] * new.capacity
        new.size = 0
        for i in range(0,self.size):
            new.push(self.data[i])
        self.capacity = new.capacity
        self.data = new.data
        self.size = new.size
        del new

    def shrink(self):
        """
        Decreases the capacity of stack if needed
        :return: No return
        """
        mid = self.capacity // 2
        del self.data[mid:]
        self.capacity /= 2
        self.capacity = mid

def reverse(stack):
    """
    Reverses the elements of the stack
    :param: Stack 
    :return: A new stack in reversed order
    """
7    new = Stack()
    new.capacity = stack.capacity
    new.data = [None] * new.capacity
    new.size = 0
    for i in range(stack.size -1, -1, -1):
        new.push(stack.data[i])
    del stack
    return new

def replace(stack, old, new):
    """
    Replaces all copies of a value in a stack with a new value
    :param: Stack, integer value to replace, integer value being added
    :return: Stack with adjusted values
    """
    for i in range(0,stack.size):
        if stack.data[i] == old:
            stack.data[i] = new
    return stack
