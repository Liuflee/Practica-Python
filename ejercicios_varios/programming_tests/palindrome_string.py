'''Given an string x, return true if x is a 
palindrome, and false otherwise.'''


class Solution(object):
    def isPalindrome(self, x):
        string = x.lower()
        reverse = string[::-1]
        if reverse == string:
            return True
        else:
            return False

solution = Solution()
print(solution.isPalindrome("Hola"))  
print(solution.isPalindrome("HooH"))


#Segunda forma

class Solution(object):
    def isPalindrome(self, x):
        string = str(x).lower()
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        
        return True


solution = Solution()
print(solution.isPalindrome("Hola"))  
print(solution.isPalindrome("HooH"))