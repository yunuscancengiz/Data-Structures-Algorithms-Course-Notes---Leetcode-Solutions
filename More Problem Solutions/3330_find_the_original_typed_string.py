'''
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

 

Example 1:

Input: word = "abbcccc"

Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

Example 2:

Input: word = "abcd"

Output: 1

Explanation:

The only possible string is "abcd".

Example 3:

Input: word = "aaaa"

Output: 4

 

Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.
'''


class Solution:
    def possibleStringCount(self, word: str) -> int:
        result = 1
        word = list(word)
        count_map = {}
        
        prev = None
        consecutive = False
        indexes = []
        for index, letter in enumerate(word):
            if prev:
                if prev == letter:
                    if not indexes:
                        indexes = [index - 1]
                    indexes.append(index)
                    consecutive = True
                    if index >= len(word) - 1:
                        if prev not in count_map.keys():
                            count_map[prev] = []
                        count_map[prev].append(indexes)
                        consecutive = False
                        indexes = []
                else:
                    if consecutive:
                        if prev not in count_map.keys():
                            count_map[prev] = []
                        count_map[prev].append(indexes)
                        consecutive = False
                        indexes = []
            prev = letter

        for letter, indexes_list in count_map.items():
            for l in indexes_list:
                result += (len(l) - 1)
        return result

if __name__ == '__main__':
    word = 'eejeeu'
    #word = "abbcccc"
    print(Solution().possibleStringCount(word=word))
