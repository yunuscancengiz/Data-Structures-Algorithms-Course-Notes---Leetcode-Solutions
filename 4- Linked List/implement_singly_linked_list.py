class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

first_node = Node(10)
second_node = Node(20)
third_node = Node(30)

# next ile bağlantıları kur
first_node.next = second_node
second_node.next = third_node

# first node üzerinden third node'un değerini oku
print(first_node.next.next.value)   # output: 30

