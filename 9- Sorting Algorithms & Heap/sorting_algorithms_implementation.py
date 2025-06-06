class SortingAlgorithms:

    def __init__(self):
        self.numbers = [29, 11, 21, 5, 28, 11, 15, 26, 49, 16]


    def bubble_sort(self, numbers=None):
        if numbers is None:
            numbers = self.numbers

        for i in range(len(numbers)):
            swapped = False
            for j in range(0, len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    swapped = True
            if not swapped:
                break
        return numbers
    

    def selection_sort(self, numbers=None):
        if numbers is None:
            numbers = self.numbers

        for i in range(len(numbers) - 1):
            min_index = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            if i != min_index:
                numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        return numbers
                    

    def selection_sort_with_recursion(self, numbers=None):
        if numbers is None:
            numbers = self.numbers

        def sort(min_index=0):
            if min_index >= len(numbers):
                return numbers

            min_value_index = min_index
            for index in range(min_index, len(numbers)):
                if numbers[index] < numbers[min_value_index]:
                    min_value_index = index
            numbers[min_index], numbers[min_value_index] = numbers[min_value_index], numbers[min_index]
            min_index += 1
            return sort(min_index=min_index)
        sort()
        return numbers
    

    def insertion_sort(self, numbers=None):
        if numbers is None:
            numbers = self.numbers

        for i in range(1, len(numbers)):
            temp = numbers[i]
            j = i - 1
            while temp < numbers[j] and j > -1:
                numbers[j + 1] = numbers[j]
                numbers[j] = temp
                j -= 1
        return numbers
                

if __name__ == '__main__':
    sorting = SortingAlgorithms()
    #print(sorting.bubble_sort())
    
    #print(sorting.selection_sort_with_recursion())
    #print(sorting.selection_sort())
    print(sorting.insertion_sort())