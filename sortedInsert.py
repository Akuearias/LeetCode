#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    new_head = DoublyLinkedListNode(node_data=data)
    if data < llist.data:
        new_head.next = llist
        llist.prev = new_head
        return new_head

    dummy = llist

    while dummy.data < data and dummy.next and dummy.next.data < data:
        dummy = dummy.next

    if not dummy.next:
        dummy.next = new_head
        llist.tail = new_head
        dummy.next.prev = dummy

    else:
        dummy2 = dummy.next
        dummy.next = new_head
        dummy2.prev = new_head
        new_head.prev = dummy
        new_head.next = dummy2

    return llist