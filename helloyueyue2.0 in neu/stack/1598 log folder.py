#stack space: O(n)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #use len(stack) to represent to moves back to main folder
        stack = []
        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
                else:
                    continue
            elif log == './':
                continue
            else:
                stack.append(log)
        return len(stack)

#space O(1)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        move = 0
        for log in logs:
            if move > 0 and log == '../':
                move -= 1
            elif log != './' and log != '../':
                move += 1
        return move