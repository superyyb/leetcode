class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == "+":
                stack.append((stack[-1]+stack[-2]))
            elif char == "C":
                stack.pop()
            elif char == "D":
                stack.append(2*stack[-1])
            else:
                stack.append(int(char))
        total = 0
        while stack:
            total += stack.pop()
        return total