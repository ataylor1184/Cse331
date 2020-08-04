"""
# Project 5
# Name: Alex Taylor
# PID: A53347473
"""

class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        """
        Prints the relevant information about the Circular Queue
        :return: No return
        """
        print("head ", self.head)
        print("tail ", self.tail)
        print("data ", self.data)
        print("capacity ", self.capacity)
        print("size ", self.size)
        return ""

    def is_empty(self):
        """
        Determines if Queue is empty
        :return: True if queue is empty, False Otherwise
        """
        return self.size <= 0

    def __len__(self):
        """
        Determines the length of the queue
        :return: integer number of elements
        """
        return self.size

    def first_value(self):
        """
        Determines the value of the first number in the queue
        :return: integer value of first number or none if queue is empty
        """
        if self.is_empty:
            return None
        return self.data[self.head]

    def enqueue(self, val):
        """
        Appends the value to the back of the Circular Queue
        :param: integer value to be entered
        :return: No return
        """
        if self.size + 1 == self.capacity:
            self.grow()
        self.size += 1
        self.data[self.tail] = val
        self.tail = (self.head + self.size) % self.capacity

    def dequeue(self):
        """
        Pops the top item in the Circular Queue
        :return: None if Queue is empty, Otherwise the integer popped
        """
        if (self.size <= 0):
            return None
        return_data = self.data[self.head]
        self.data[self.head] = None
        self.head = (1 + self.head) % (self.capacity)
        self.size -= 1
        if (self.size <= (self.capacity//4) and self.capacity != 4):
            self.shrink()
        return return_data

    def grow(self):
        """
        Increases the capacity of Circular Queue if needed
        :return: No return
        """
        old = self.data
        size = self.capacity
        self.capacity *= 2
        self.data = [None] * self.capacity
        front = self.head
        for i in range(0, self.size):
            self.data[i] = old[front]
            front = (1 + front) % (size)
        self.tail = (self.head + self.size) % self.capacity
        self.head = 0

    def shrink(self):
        """
        Decreases the capacity of Circular Queue if needed
        :return: No return
        """
        old = self.data
        self.data = [None] * (self.capacity // 2)
        front = self.head
        for i in range(self.size):
            self.data[i] = old[front]
            front = (1 + front) % (self.capacity * 2)
        self.head = 0
        self.tail = (self.head + self.size) % self.capacity
        self.capacity = (self.capacity // 2)

queue = CircularQueue(8)

for i in range(7):
	queue.enqueue(7-i)
	
queue.dequeue()
queue.dequeue()

print(queue)
#assert queue.data == [None,None,5,4,3,2,1,None]
#assert queue.dequeue() == 5