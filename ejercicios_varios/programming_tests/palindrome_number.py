'''Given an integer x, return true if x is a 
palindrome, and false otherwise.'''


class Solution(object):
    def isPalindrome(self, x):
        string_num = str(x)
        reverse = string_num[::-1]
        if reverse == string_num:
            return True
        else:
            return False

solution = Solution()
print(solution.isPalindrome(12321))  
print(solution.isPalindrome(12345))