class HashNode:
    """
    DO NOT EDIT
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None]*capacity


    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True


    def __repr__(self):
        pass


    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity


    def insert(self, key, value):
        """
        Inserts a key,value hash node into the hash table
        :param key: the string key of the node
        :param value: the integer value of node
        """
        if float(self.size/self.capacity) > .75:    #check if need to grow
            self.grow()
        if key != None and key.strip() and value is not None:  #checks if key is not None
            index = self.quadratic_probe(key)       #finding adjusted index
            if self.table[index] != None:           #if a node exists at this index...
                if self.table[index].key == key:    #if the node we are adding has same key...
                    self.table[index].value = value #updates value
            elif self.table[index] == None:         #if there is no node at this index...
                ins_node = HashNode(key,value)      #creates node to insert
                self.size += 1                      #update size
                self.table[index]= ins_node         #add node

    def quadratic_probe(self, key):
        """
        Finds the correct empty index to insert the node at
        :param key: the string key of the node
        :return: index of where to place node, or -1 if key does not exist
        """
        probed_index = self.hash_function(key)
        if not key:
            return -1
        for i in range(0,self.capacity):
            if self.table[i] is not None:
                if self.table[i].key == key:
                    return probed_index
        probe_val = 0
        while self.table[probed_index] is not None:
            probe_val += 1
            probed_index = (probed_index + probe_val*probe_val) % self.capacity
        return probed_index

    def find(self, key):
        """
        Finds the node if it is in the hashtable
        :param key: the string key of the node
        :return: the hash node, or False if key or node does not exist
        """
        if not key:
            return False
        for i in range(0,self.capacity):
            if self.table[i] is not None:
                if self.table[i].key == key:
                    return self.table[i]
        return False

    def lookup(self, key):
        """
        Finds the node if it is in the hashtable
        :param key: the string key of the node
        :return: the value of the hash node, or False if key or node does not exist
        """
        if self.find(key):
            return self.find(key).value
        return False


    def delete(self, key):
        """
        Removes the node from the hash table
        :param key: the string key of the node
        """
        i=0
        while i < int(self.capacity):
            if self.table[i] is not None:
                if self.table[i].key == key:
                    self.table[i] = None
            i += 1
        self.size -= 1

    def grow(self):
        """
        doubles capacity and rehashes the table
        """
        self.capacity *= 2 
        self.rehash()

    def rehash(self):
        """
        rehashes the table's contents
        """
        temp_table = self.table
        self.table = [None]*self.capacity
        self.size = 0
        for node in temp_table:
            if node is not None:
                self.insert(node.key,node.value)


def string_difference(string1, string2):
        """ 
        Creates a set of the difference between the two strings using hashtables
        :param string1, string2: two strings
        :return: a set of the differences between both strings
        """
        ht_1 = HashTable()
        ht_2 = HashTable()
        difference_set = set()
        difference_value = 0
        for char in string1:    #adding characters to a hashmap while counting duplicates
            value = 1
            if ht_1.find(char):
                value += 1
            ht_1.insert(char,value)
        for char in string2:
            value = 1
            if ht_2.find(char):
                value += 1
            ht_2.insert(char,value)
        for i in range(0,ht_1.capacity):     #for char in first hash table
            if ht_1.table[i] is not None:
                if ht_2.find(ht_1.table[i].key):  #if a matching letter is found
                    difference_value = ht_1.table[i].value - ht_2.find(ht_1.table[i].key).value #subtract number of letters
                    if difference_value > 0:
                        difference_set.add(difference_value*ht_1.table[i].key)
                else:
                    difference_set.add(ht_1.table[i].key)
        for i in range(0,ht_2.capacity):     #for char in first hash table
            if ht_2.table[i] is not None:
                if ht_1.find(ht_2.table[i].key):  #if a matching letter is found
                    difference_value =  ht_2.table[i].value - ht_1.find(ht_2.table[i].key).value #subtract number of letters
                    if difference_value > 0:
                        difference_set.add(difference_value*ht_2.table[i].key)
                else:
                    difference_set.add(ht_2.table[i].key)       #if no matching letter is found
        return difference_set
    
