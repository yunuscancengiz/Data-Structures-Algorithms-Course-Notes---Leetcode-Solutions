class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeTraversal:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value=value)
        if self.root is None:
            self.root = new_node
            return True
        
        temp_node = self.root
        while True:
            if new_node.value < temp_node.value:
                if temp_node.left is None:
                    temp_node.left = new_node
                    return True
                temp_node = temp_node.left
            elif new_node.value > temp_node.value:
                if temp_node.right is None:
                    temp_node.right = new_node
                    return True
                temp_node = temp_node.right
            else:
                return False
            

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
    

    def min_node(self):
        temp_node = self.root
        while temp_node:
            temp_node = temp_node.left
        return temp_node
    

    def max_node(self):
        temp_node = self.root
        while temp_node:
            temp_node = temp_node.right
        return temp_node
    

    def BFS(self):
        # append temp node to my_queue
        # append temp node's value to values list
        # append temp node's left and right nodes to the queue
        # pop temp node from queue
        my_queue = []   # FIFO list
        values = []

        temp_node = self.root
        my_queue.append(temp_node)
        while len(my_queue) > 0:
            temp_node = my_queue.pop(0)
            values.append(temp_node.value)
            if temp_node.left is not None:
                my_queue.append(temp_node.left)
            if temp_node.right is not None:
                my_queue.append(temp_node.right)
        return values
    

    def DFS_preorder(self):
        values = []

        def traverse(current_node):
            values.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node=current_node.left)
            if current_node.right is not None:
                traverse(current_node=current_node.right)
        traverse(current_node=self.root)
        return values
    

    def DFS_postorder(self):
        values = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node=current_node.left)
            if current_node.right is not None:
                traverse(current_node=current_node.right)
            values.append(current_node.value)
        traverse(current_node=self.root)
        return values
    

    def DFS_inorder(self):
        values = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node=current_node.left)
            values.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node=current_node.right)
        traverse(current_node=self.root)
        return values

    


if __name__ == '__main__':
    values = [38, 19, 69, 12, 24, 59, 95]
    my_tree = TreeTraversal()
    for value in values:
        my_tree.insert(value=value)

    print(values)
    print(my_tree.BFS())
    print(my_tree.DFS_preorder())
    print(my_tree.DFS_postorder())
    print(my_tree.DFS_inorder())
    