# Deque class oluştur
# add, remove, addleft, removeleft, size, is_empty, show_last, show_first metodları olsum


class Deque:
    def __init__(self):
        self.elements = []


    def add_right(self, element):
        self.elements.append(element)


    def add_left(self, element):
        self.elements.insert(index=0, object=element)


    def remove_right(self):
        return self.elements.pop()
    

    def remove_left(self):
        return self.elements.pop(0)
    

    def size(self):
        return len(self.elements)
    

    def is_empty(self):
        return self.elements == []
    

    def show_last(self):
        return self.elements[-1]
    

    def show_first(self):
        return self.elements[0]
    

    def show_deque(self):
        return self.elements