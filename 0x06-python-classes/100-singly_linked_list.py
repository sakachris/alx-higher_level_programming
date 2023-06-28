#!/usr/bin/python3

""" class node to define singly linked list """


class Node:
    """
    Args:
        __data: integer data to a linked list
        __next_node: poiner to next_node
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def next_node(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) or not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Args:
        __head: first node
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        lst = ""
        temp = self.__head
        while temp is not None:
            lst += "\n".join(str(temp.data))
            temp = temp.next_node
        return lst

    def sorted_insert(self, value):
        """
        inserts new node
        """
        add_node = Node(value, self.__head)
        temp = self.__head
        if temp is None:
            self.__head = add_node
            return
        if value < temp.data:
            add_node.next_node = self.__head
            self.__head = add_node
            return
        while temp.next_node is not None:
            if value < temp.next_node.data:
                break
            temp = temp.next_node
        add_node.next_node = temp.next_node
        temp.next_node = add_node
        return
