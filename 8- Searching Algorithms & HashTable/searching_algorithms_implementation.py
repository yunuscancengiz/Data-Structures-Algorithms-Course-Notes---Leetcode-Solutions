class Search:

    def __init__(self, numbers: list, num: int, is_ordered: bool=False):
        self.numbers = numbers
        self.num = num
        self.is_ordered = is_ordered


    def sequential(self):
        for num in self.numbers:
            if num == self.num:
                return True
            if self.is_ordered:
                if num > self.num:
                    return False
        return False
    

    def binary(self):
        if not self.is_ordered:
            self.numbers.sort()
            self.is_ordered = True

        found = False
        first_pointer = 0
        last_pointer = len(self.numbers) - 1
        mid = len(self.numbers) // 2

        while first_pointer <= last_pointer and not found:
            mid = (first_pointer + last_pointer) // 2
            if self.num > self.numbers[mid]:
                first_pointer = mid + 1
            elif self.num < self.numbers[mid]:
                last_pointer = mid - 1
            else:
                found = True
        return found