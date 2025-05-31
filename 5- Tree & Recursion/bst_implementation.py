# BINARY SEARCH TREE Implementation

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree():

    def __init__(self, root=None):
        self.root = root


    def insert(self, value):
        new_node = Node(value=value)
        if self.root is None:
            self.root = new_node
            return True
        
        temp_node = self.root   # kök değeri koru
        while True:
            if new_node.value == temp_node.value:
                return False

            if new_node.value < temp_node.value:
                if temp_node.left is None:
                    temp_node.left = new_node
                    return True
                temp_node = temp_node.left  # eğer solda değer varsa temp node'u onunla güncelle ki onun solunu kontrol edebilsin
            else:
                if temp_node.right is None:
                    temp_node.right = new_node
                    return True
                temp_node = temp_node.right

        
    def contains(self, value):
        temp_node = self.root
        while temp_node:
            if value < temp_node.value:
                temp_node = temp_node.left
            elif value > temp_node.value:
                temp_node = temp_node.right
            else:
                return True
        return False
    

    def minimum_node(selftemp_node):
        while temp_node.left:
            temp_node = temp_node.left
        return temp_node.value
    

    def maximum_node(self, temp_node):
        while temp_node.right:
            temp_node = temp_node.right
        return temp_node.value
                


if __name__ == '__main__':
    bst = BinarySearchTree()
    print(bst.insert(45))
    print(bst.insert(32))
    print(bst.insert(53))
    print(bst.insert(65))

    print(bst.contains(48))
    print(bst.contains(53))
    print(bst.minimum_node())


        
