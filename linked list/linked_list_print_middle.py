# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
# [3, 4, 5, 6, 8]
class Node:
    def __init__(self, value:int):
        self.value = value
        self.next = None
    
#node_5 = Node(8)
node_4 = Node(6)
node_3 = Node(5)
node_2 = Node(4)
node_1 = Node(3)


node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
#node_4.next = node_5


def print_middle(head: Node):
    fast = slow = head
   
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    print(slow.value)