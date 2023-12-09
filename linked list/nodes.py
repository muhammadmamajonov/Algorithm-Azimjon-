# [3, 4, 5, 6, 8]
class Node:
    def __init__(self, value:int):
        self.value = value
        self.next = None
    
#node_5 = Node(8)
node_4 = Node(6)
node_3 = Node(5)
node_2 = Node(4)
head = Node(3)


head.next = node_2
node_2.next = node_3
node_3.next = node_4