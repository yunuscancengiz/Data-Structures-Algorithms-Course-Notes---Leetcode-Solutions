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
    

    def merge_sort(self, numbers=None): # Time Complexity: O(n log n)
        if numbers is None:
            numbers = self.numbers
        
        def sort(arr: list):    # Time Complexity: O(log n)
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = sort(arr=arr[:mid])
            right = sort(arr=arr[mid:])
            return merge(left=left, right=right)
        
        def merge(left: list, right: list):     # Time Complexity: O(n)
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return sort(arr=numbers)
    

    def quick_sort(self, numbers=None, left=0, right=None):
        if numbers is None:
            numbers = self.numbers

        def pivot(pivot_index, end_index):
            swap_index = pivot_index
            pivot_value = numbers[pivot_index]
            for i in range(pivot_index + 1, end_index + 1):
                if numbers[i] < pivot_value :
                    swap_index += 1
                    numbers[swap_index], numbers[i] = numbers[i], numbers[swap_index]
            numbers[pivot_index], numbers[swap_index] = numbers[swap_index], numbers[pivot_index]
            return swap_index
        
        if right is None:
            right = len(numbers) - 1

        if left < right:
            swap_index = pivot(pivot_index=left, end_index=right)
            self.quick_sort(numbers=numbers, left=left, right=swap_index - 1)
            self.quick_sort(numbers=numbers, left=swap_index + 1, right=right)
        return numbers
        

    def heap_sort(self, numbers=None):
        if numbers is None:
            numbers = self.numbers

        def heapify(arr: list, n: int, i: int):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[largest] < arr[left]:
                largest = left

            if right < n and arr[largest] < arr[right]:
                largest = right

            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]
                heapify(arr=arr, n=n, i=largest)

        # max heap
        n = len(numbers)
        for i in range(n // 2 -1, -1, -1):
            heapify(arr=numbers, n=n, i=i)

        # swap
        for i in range(n - 1, 0, -1):
            numbers[i], numbers[0] = numbers[0], numbers[i]
            heapify(arr=numbers, n=i, i=0)
        return numbers
    

if __name__ == '__main__':
    sorting = SortingAlgorithms()
    #print(sorting.bubble_sort())
    
    #print(sorting.selection_sort_with_recursion())
    #print(sorting.selection_sort())
    #print(sorting.insertion_sort())

    #print(sorting.merge_sort())
    #print(sorting.quick_sort())
    print(sorting.heap_sort())