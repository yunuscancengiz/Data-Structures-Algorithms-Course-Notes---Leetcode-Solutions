class HashTable:

    def __init__(self, size: int=13):
        self.size = size
        self.slots = [None] * size
        


    def hash_function(self, key):
        hash_ = 0
        for letter in key:
            hash_ = (hash_ + ord(letter) * 19) % self.size
        return hash_
    

    def set_item(self, key, value):
        index = self.hash_function(key=key)
        if self.slots[index] == None:
            self.slots[index] = []
        self.slots[index].append([key, value])


    def get_item(self, key):
        index = self.hash_function(key=key)
        if self.slots[index]:
            for registered_key, registered_value in self.slots[index]:
                if registered_key == key:
                    return registered_value
        return None
    

    def get_keys(self):
        keys = []
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                for j in range(len(self.slots[i])):
                    keys.append(self.slots[i][j][0])
        return keys
    

    def print_table(self):
        for key, value in enumerate(self.slots):
            print(f'{key} --> {value}')
        print('-' * 20)


    

if __name__ == '__main__':
    hashtable = HashTable()
    hashtable.set_item(key='Apple', value=100)
    hashtable.set_item(key='Banana', value=150)
    hashtable.set_item(key='Melon', value=250)

    hashtable.print_table()

    hashtable.set_item(key='Watermelon', value=300)
    hashtable.set_item(key='Strawberry', value=100)
    hashtable.set_item(key='Lemon', value=150)

    hashtable.print_table()

    print(hashtable.get_item(key='Watermelon'))

    print(hashtable.get_keys())

    hashtable.set_item(key='Doner', value='500')

    hashtable.print_table()