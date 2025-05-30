
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# bağlantıları next ve prev ile kur
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2

# 3. node'dan biribci node'a kadar gel sonra 2. node'u oku
print(node3.prev.prev.next.value)