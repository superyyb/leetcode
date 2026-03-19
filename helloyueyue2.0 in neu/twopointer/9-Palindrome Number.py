#Two-pointer
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        i, j = 0, len(x) - 1
        while i <= j:
            if x[i] != x[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

#Math method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #check whether the reversed number is the same as original one
        if x < 0:
            return False
        res = 0
        original_x = x #Remember to store x before while loop
        while x != 0:
            digit = x % 10
            x //= 10
            res = res * 10 + digit
        return res == original_x



#str transformation
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        return s==s[::-1]
