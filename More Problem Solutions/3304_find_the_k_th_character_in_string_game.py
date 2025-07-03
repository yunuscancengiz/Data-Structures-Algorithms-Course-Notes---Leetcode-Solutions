'''
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.

 

Example 1:

Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".
Example 2:

Input: k = 10

Output: "c"

 

Constraints:

1 <= k <= 500

'''

import string

class Solution:
    def kthCharacter(self, k: int) -> str:
        def recursion(word_list: list):
            new_list = []
            for index in word_list:
                index = index + 1 if index + 1 < len(alphabet) else 0
                new_list.append(index)
            word_list = word_list + new_list

            if k <= len(word_list):
                return alphabet[word_list[k - 1]]
            return recursion(word_list=word_list)
            
        alphabet = {index: char for index, char in enumerate(list(string.ascii_lowercase))}
        word_list = [0]
        return recursion(word_list=word_list)
            
        


if __name__ == '__main__':
    k = 5
    print(Solution().kthCharacter(k=k))