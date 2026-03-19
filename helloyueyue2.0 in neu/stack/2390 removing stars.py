#Optimal solution
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

#My solution
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char .isalpha():
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        return ''.join(stack)