# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:49:41 2023

@author: DIGITAL CITY
"""
 
class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None
        
    
def print_elements(head: Node) -> None:
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next
        

node_5 = Node(8)
node_4 = Node(6)
node_3 = Node(5)
node_2 = Node(4)
node_1 = Node(3)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

