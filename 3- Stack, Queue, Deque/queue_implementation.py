# Queue class'ı oluştur
# dequeue, enqueue, is_empty, show_last, size metodları olsun

class Queue:
    def __init__(self):
        self.elements = []

    
    def enqueue(self, element):
        self.elements.insert(index=0, object=element)


    def dequeue(self):
        return self.elements.pop()
    

    def is_empty(self):
        return self.elements == []
    

    def show_last(self):
        return self.elements[0]
    

    def size(self):
        return len(self.elements)
    
    