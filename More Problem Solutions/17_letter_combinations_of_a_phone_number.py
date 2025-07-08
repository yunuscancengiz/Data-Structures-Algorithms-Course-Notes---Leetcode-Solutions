'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

from typing import List


class Solution:
    digit_index = 0
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []
        if digits == '':
            return result

        total_length = 1
        for digit in digits:
            total_length *= len(digit_map[digit])

        
        def recursion(letters: list, length: int):
            length = int(length / len(letters))
            if not result:
                for letter in letters:
                    result.extend([letter] * length)
            else:
                l_index = 0
                counter = 0
                for index in range(len(result)):
                    result[index] += letters[l_index]
                    counter += 1
                    if counter >= length:
                        counter = 0
                        l_index = l_index + 1 if l_index + 1 < len(letters) else 0
            self.digit_index += 1
            if self.digit_index >= len(digits):
                return result
            return recursion(letters=digit_map[digits[self.digit_index]], length=length)
        recursion(letters=digit_map[digits[self.digit_index]], length=total_length)
        return result
                    

if __name__ == '__main__':
    digits = '2349'
    print(Solution().letterCombinations(digits=digits))
            


        