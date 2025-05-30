# Kendimiz bir Stack class'ı oluşturalım
# push, pop, show_last, is_empty, size metodları olsun

class Stack():
    def __init__(self):
        self.stack = []

    
    def push(self, item):
        self.stack.append(item)

    
    def pop(self):
        return self.stack.pop()


    def show_last(self):
        return self.stack[-1]
    

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    

    def size(self):
        return len(self.stack)