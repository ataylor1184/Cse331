class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        Insert a node into the BST based on value
        :param: value of node
        :return: no return
        """
        ins_node = Node(value)
        if self.size == 0:
            self.root = ins_node
        p = self.search(value, self.root) #checking if node is already in the tree
        if value == p.value:
            p = ins_node
            if self.get_size() > 1:
                self.size -= 1
        elif value < p.value:
            ins_node.parent = p
            p.left = ins_node
        else:
            ins_node.parent = p
            p.right = ins_node
        self.size += 1

    def remove(self, value):
        """
        Remove a node into the BST based on value
        :param: value of node
        :return: returns None if tree is empty
        """
        if self.root is None: #empty tree
            return None
        elif self.root.value == value: # removing the root node
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                temp_parent = self.root
                delete_node = self.root.right
                while delete_node.left:
                    temp_parent = delete_node
                    delete_node = delete_node.leftChild
                self.root.value = delete_node.value
                if delete_node.right:
                    if temp_parent.value > delete_node.value:
                        delete_node.left = delete_node.right
                    elif temp_parent.value < delete_node.value:
                        temp_parent.right = delete_node.right
                else:
                    if delete_node.value < temp_parent.value:
                        temp_parent.left = None
                    else:
                        temp_parent.right = None
            self.size -= 1
            return None
        parent = None
        node = self.root
        while node and node.value != value:
            parent = node
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
        if node is None or node.value != value: #test if value exists in tree
            return None
        elif node.left is None and node.right is None: #node being removed has no children
            if value < parent.value:
                parent.left = None
            else:
                parent.right = None
            self.size -= 1
            return None
        elif node.left and node.right is None: #node being removed has 1 left child
            if value < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
            self.size -= 1
            return None
        elif node.left is None and node.right: #node being removed has 1 right child
            if value < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right
            self.size -= 1
            return None
        else:         #node being removed has both left and right children
            self.size -= 1
            temp_parent = node
            delete_node = node.right
            while delete_node.left:
                temp_parent = delete_node
                delete_node = delete_node.left
            node.value = delete_node.value
            if delete_node.right:
                if temp_parent.value > delete_node.value:
                    temp_parent.left = delete_node.right
                elif temp_parent.value < delete_node.value:
                    temp_parent.right = delete_node.right
            else:
                if delete_node.value < temp_parent.value:
                    temp_parent.left = None
                else:
                    temp_parent.right = None


    def search(self, value, node):
        """
        Search for node in the BST based on value
        :param: value to search for and node to start from
        :return: returns the node with the value, or None
        """
        if self.root is None:
            return None
        if value == node.value:
            return node
        elif (value < node.value and node.left is not None):
            return self.search(value, node.left)
        elif (value > node.value and node.right is not None):
            return self.search(value, node.right)
        return node

    def inorder(self, node):
        """
        Traverses and Displays BST inorder
        :param: starting node
        :return: generator object of inorder traversal
        """
        if self.root is not None:
            if node.left is not None:
                yield from self.inorder(node.left)
            yield node.value
            if node.right is not None:
                yield from self.inorder(node.right)

    def preorder(self, node):
        """
        Traverses and Displays BST preorder
        :param: starting node
        :return: generator object of preorder traversal
        """
        if self.root is not None:
            yield node.value
            yield from self.preorder(node.left) if node.left is not None else()
            yield from self.preorder(node.right) if node.right is not None else()

    def postorder(self, node):
        """
        Traverses and Displays BST postorder
        :param: starting node
        :return: generator object of postorder traversal
        """
        if self.root is not None:
            yield from self.postorder(node.left) if node.left != None else()
            yield from self.postorder(node.right) if node.right != None else()
            yield node.value

    def depth(self, value):
        """
        Displays depth of a node with given value
        :param: integer value of a node
        :return: -1 if node does not exist, integer depth otherwise
        """
        count = 0
        node = self.search(value, self.root)
        if node is None or node.value != value:
            return -1
        parent = node.parent
        while parent is not None:
            count += 1
            parent = parent.parent
        return count

    def height(self, node):
        """
        Displays height of the node
        :param: starting node
        :return: -1 if tree is empty, 0 if tree has 1 node, integer height otherwise
        """
        if self.root is None:
            return -1
        if self.size == 1:
            return 0
        if self.is_leaf(node):
            return 0
        else:
            return 1+  max(self.height(c) for c in self.children(node))

    def min(self, node):
        """
        Returns the minimum value in a tree
        :param: starting node
        :return: smallest node of tree
        """
        if self.root is None:
            return None
        else:
            if node.left is not None:
                return self.min(node.left)
            if node.left is None:
                return node

    def max(self, node):
        """
        Returns the maximum value in a tree
        :param: starting node
        :return: largest node of tree
        """
        if self.root is None:
            return None
        else:
            if node.right is not None:
                return self.max(node.right)
            if node.right is None:
                return node

    def get_size(self):
        """
        Displays size of tree
        :return: integer number of nodes
        """
        return self.size

    def is_perfect(self, node):
        """
        Determines if tree is a perfect tree
        :param: starting node
        :return: boolean True or False
        """
        if self.size == 0:
            return True
        if self.size == (pow(2, self.height(node)+1)-1):
            return True
        return False

    def is_degenerate(self):
        """
        Determines if tree is a degenerate tree
        :param: starting node
        :return: boolean True or False
        """
        if self.size != 0 and self.size == (self.height(self.root)+1):
            return True
        return False

    def is_leaf(self, node):
        """
        Determines if the node is a leaf node
        :param: node
        :return: boolean True or False
        """
        return node.left is None and node.right is None

    def children(self, node):
        """
        Returns both children of a node
        :param: node
        :return: generator object of all children of the node
        """
        if node.left is not None:
            yield node.left
        if node.right is not None:
            yield node.right
bst = BinarySearchTree()
bst.insert(13)
bst.insert(20)
bst.insert(17)
bst.insert(10)
bst.insert(21)
bst.insert(7)
bst.insert(12)

bst.remove(7)
bst.remove(10)
bst.remove(21)
bst.remove(20)
bst.remove(13)

print(bst.size)
print(bst.root)