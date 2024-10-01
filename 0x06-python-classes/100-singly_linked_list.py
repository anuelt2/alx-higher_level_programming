#!/usr/bin/python3
"""Define a node class"""


class Node:
    """A class representing a node"""

    def __init__(self, data, next_node=None):
        """Initialize a node, with data and next_node"""
        self.data = data
        self.next_node = next_node

    """Private instance attribute for data"""
    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """Private instance attribute for next_node"""
    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""
        if (value is not None) and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Define a singly linked list class"""


class SinglyLinkedList:
    """A class representing a singly linked list"""

    def __init__(self):
        """Initialize a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Public instance method that inserts new node"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Method that prints list"""
        data_str = []
        temp = self.__head
        while temp is not None:
            data_str.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(data_str)
