'''

'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_list = list(str(x))
        if num_list[0] == '-':
            return False
        
        left = 0
        right = len(num_list) - 1
        while left < right:
            if num_list[left] != num_list[right]:
                return False
            left += 1
            right -= 1
        return True
        
        
        
    

if __name__ == '__main__':
    print(Solution().isPalindrome(x=-121))