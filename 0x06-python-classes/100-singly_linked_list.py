#!/usr/bin/python3
""" Node defines a node of a singly linked list """


class Node:
    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with data and a reference to the next node.
        Args:
            data: The data value of the node.
            next_node: The reference to the next node (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data value of the node.
        Returns:
            The data value.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.
        Args:
            value: The data value to be set.
        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the reference to the next node.
        Returns:
            The reference to the next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node.
        Args:
            value: The reference to the next node.
        Raises:
            TypeError: If the value is neither None nor a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    def __init__(self):
        """
        Initializes an empty SinglyLinkedList object.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the singly linked list in the correct
        sorted position (increasing order).
        Args:
            value: The data value of the new Node to be inserted.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the singly linked list.
        Returns:
            The string representation of the list,
            with one node number per line.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
